# -*- coding: utf-8 -*-
"""CLI entrypoint."""

from os import walk
from os.path import abspath, basename, exists as path_exists
from re import ASCII, match

import click
from config import Config

from wren.change import Change
from wren.pomo import apply_changes, backup_original_mo, get_mo, restore_original_mo

HELP_CFG = "Path to config file."
HELP_UNDO = "If provided, the original names will be reinstated."


@click.command()
@click.argument("changesets", nargs=-1)
@click.option(
    "-c",
    "--config",
    default="./wren.cfg",
    help=HELP_CFG,
    type=click.Path(exists=True),
    show_default=True,
)
@click.option("-u", "--undo", help=HELP_UNDO, is_flag=True)
def rename_ships(changesets, config, undo):
    """wren = Warships RENamer. A utility that can rename ships in the World of Warships game by
    Wargaming.net.

    Applies all changes found in the list of CHANGESETS, as defined in the provided config file.

    Example:

        $ wren radar cyrillic
    """

    try:
        cfg = load_config(config)
        wowsdir = get_warship_directory(cfg)

        if undo:
            restore_original_mo(wowsdir)
            return

        change_prefix = []
        change_replace = []

        for changeset in changesets or default_changesets():
            try:
                changelist = [Change(**change) for change in cfg[f"changesets.{changeset}"]]
                change_prefix.extend(filter(lambda c: c.is_prefix(), changelist))
                change_replace.extend(filter(lambda c: c.is_replace(), changelist))
            except KeyError:
                click.echo(f"WARNING: Changeset {changeset} not found in configuration.")
                continue

        if len(change_prefix) + len(change_replace) == 0:
            click.echo("No changes to apply.")
            return

        backup_original_mo(wowsdir)

        mo_file = get_mo(wowsdir)
        apply_changes(mo_file, change_replace)
        apply_changes(mo_file, change_prefix)
        mo_file.save()
    except Exception as err:
        click.echo("Aborting…")
        restore_original_mo(wowsdir)
        raise err


def default_changesets():
    """Get the default changesets."""
    return ["radarWithRange"]


def get_warship_directory(cfg):
    """Get a string with the path to the WoWs directory."""
    cfg_key = "wowsPath"
    wows_path = cfg[cfg_key]
    bindir = _bindir(wows_path)
    wowsdir = abspath(f"{wows_path}/{bindir}")
    raise_if_not_path_exists(cfg_key, wowsdir)
    return wowsdir


def load_config(config_path):
    """Load and return the config."""
    click.echo(f"Using config from {click.format_filename(config_path)}")
    return Config(abspath(config_path))


def raise_if_not_path_exists(key, path):
    """Raise ClickException if the path at key does not exist."""
    if not path_exists(path):
        raise click.ClickException(f"Invalid value for '{key}': Path '{path}' does not exist")


def _bindir(wows_path):
    """Return the highest numbered subfolder of the WoWs bin directory."""
    # See <https://stackoverflow.com/a/142535>
    bindirs = sorted(next(walk(wows_path))[1])
    bindir = basename(bindirs[-1])
    if not match("^\\d{7}$", bindir, ASCII):
        raise ValueError(f"{bindir} is not a string of 7 digits")
    return bindir
