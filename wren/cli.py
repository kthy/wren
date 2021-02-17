# -*- coding: utf-8 -*-
"""CLI entrypoint."""

from os.path import exists as path_exists

import click
from config import Config
from shortuuid import uuid

# from subprocess import CalledProcessError, run  # nosec


@click.command()
@click.argument("changesets", nargs=-1)
@click.option(
    "-c", "--config", default="./wren.cfg", type=click.Path(exists=True), show_default=True
)
def rename_ships(changesets, config):
    """Main CLI entrypoint."""

    run_id = uuid()

    try:
        click.echo(f"Using config from {click.format_filename(config)}")
        cfg = Config(config)
        click.echo(cfg.as_dict())

        workdir = cfg["workingDirectory"]
        if not path_exists(workdir):
            raise click.ClickException(
                f"Invalid value for 'workingDirectory': Path '{workdir}' does not exist"
            )
        click.echo(f"Working directory {workdir}/wren-{run_id}")

        # Set default changeset
        if len(changesets) == 0:
            changesets = ["cyrillic", "joker", "radarWithRange"]  # TODO: only radarWithRange
        for changeset in changesets:
            process_changeset(cfg[f"changesets.{changeset}"])
    except Exception as err:
        click.echo(f"Aborting run {run_id}")
        raise err


def process_changeset(changeset_config):
    """Process a changeset."""
    click.echo(changeset_config)
