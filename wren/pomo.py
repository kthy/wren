# -*- coding: utf-8 -*-
"""Gettext manipulation methods."""

def backup_original_mo(wowsdir):
    """Rename the original `global.mo` to `global.mo.original`."""
    # TODO: Checksum file after moving.
    raise NotImplementedError


def compile_mo(workdir):
    """Convert `workdir/global.po` using `msgfmt` into `workdir/global.mo`"""
    raise NotImplementedError


def install_modified_mo(workdir, wowsdir):
    """Copy the new `global.mo` to where the original was."""
    raise NotImplementedError


def prepare_po(workdir):
    """Convert `${wowsPath}/res/texts/en/LC_MESSAGES/global.mo` to `workdir/global.po`"""
    raise NotImplementedError


def restore_original_mo(workdir, wowsdir):
    """Reinstate the original `global.mo` from `global.mo.original`."""
    # TODO: Checksum file after moving.
    raise NotImplementedError
