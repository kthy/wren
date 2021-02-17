# -*- coding: utf-8 -*-
"""CLI entrypoint."""

from glob import glob
from os.path import abspath, exists as path_exists
from re import ASCII, match
from tempfile import TemporaryDirectory

import click
from config import Config

from wren.change import Change
from wren.pomo import *

# from subprocess import CalledProcessError, run  # nosec


@click.command()
@click.argument("changesets", nargs=-1)
@click.option(
    "-c", "--config", default="./wren.cfg", type=click.Path(exists=True), show_default=True
)
@click.option("-u", "--undo", is_flag=True)
def rename_ships(changesets, config, undo):
    """wren = Warships RENamer.

    A utility that can rename ships in the World of Warships game by Wargaming.net.
    """

    try:
        cfg = load_config(config)
        with get_working_directory(cfg) as workdir:
            wowsdir = get_warship_directory(cfg)

            if undo:
                restore_original_mo(wowsdir)
                return

            if len(changesets) == 0:
                changesets = get_default_changeset()

            backup_original_mo(wowsdir)

            prepare_po(workdir)

            for changeset in changesets:
                apply_changeset(workdir, cfg[f"changesets.{changeset}"])

            compile_mo(workdir)

            install_modified_mo(workdir, wowsdir)
    except Exception as err:
        click.echo("Aborting…")
        restore_original_mo(wowsdir)
        raise err


def apply_change(change):
    """Apply a change."""
    print(change)
    raise NotImplementedError


def apply_changeset(workdir, changeset_config):
    """Apply all changes in a changeset."""
    # TODO: open PO file.
    changes = [Change(**change) for change in changeset_config]
    for change in changes:
        apply_change(change)


def get_default_changeset():
    """Get the default changeset."""
    # TODO: Should only return radarWithRange when done.
    return ["cyrillic", "joker", "radarWithRange"]


def get_warship_directory(cfg):
    """Get a string with the path to the WoWs directory."""
    cfg_key = "wowsPath"
    wows_path = cfg[cfg_key]
    bindir = _bindir(wows_path)
    wowsdir = abspath(f"{wows_path}/{bindir}")
    raise_if_not_path_exists(cfg_key, wowsdir)
    return wowsdir


def get_working_directory(cfg):
    """Get a string with the path to the working directory."""
    cfg_key = "workingDirectory"
    workdir_base = cfg[cfg_key]
    raise_if_not_path_exists(cfg_key, workdir_base)
    workdir = TemporaryDirectory(prefix="wren-", dir=workdir_base)
    click.echo(f"Working directory {workdir.name}")
    return workdir


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
    bindir = sorted(glob(wows_path))[-1]
    assert match("^\\d{7}$", bindir, ASCII)
    assert bindir == "3471783"
    return bindir
