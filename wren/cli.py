# -*- coding: utf-8 -*-
"""CLI entrypoint."""

from glob import glob
from os.path import join
from re import search

import click
from config import Config

# from subprocess import CalledProcessError, run  # nosec


@click.command()
@click.argument("changesets", nargs=-1)
@click.option(
    "-c", "--config", default="./wren.cfg", type=click.Path(exists=True), show_default=True
)
def rename_ships(changesets, config):
    """This is a doc comment."""

    click.echo(f"Using config from {click.format_filename(config)}")
    cfg = Config(config)
    click.echo(cfg.as_dict())

    if len(changesets) == 0:
        changesets = ["cyrillic", "joker", "radarWithRange"]
    click.echo(f"Searching for {len(changesets)} changesets")
    for changeset in changesets:
        changeset_path = f"changesets.{changeset}"
        click.echo(f'Processing changeset "{changeset_path}"')
        click.echo(cfg[changeset_path])


def glob_files(directory):
    """Return list of non-excluded files in dir and its subdirs."""
    return [f for f in glob(join(directory, "**", "*.cs"), recursive=True) if not exclude(f)]


def exclude(path):
    """Return True if the path should be excluded."""
    return search(r"AssemblyInfo\.cs|Test\.cs|/(bin|obj)/(Debug|Release)/", path)
