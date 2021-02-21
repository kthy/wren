# -*- coding: utf-8 -*-
"""Gettext manipulation methods."""

from os import remove
from os.path import exists
from shutil import copyfile, copystat

from filehash import FileHash
from polib import MOFile, mofile

from wren.change import Change


def apply_changes(mo_file: MOFile, changelist: list[Change]):
    """Apply all changes in the provided list of changes to the given MOFile."""
    for change in changelist:
        change.apply(mo_file)


def backup_original_mo(wowsdir, locale):
    """Copy the original `global.mo` to `global.mo.original`."""
    global_mo_path = _global_mo_path(wowsdir, locale)
    backup_mo_path = _backup_mo_path(wowsdir, locale)
    _copyfile_and_checksum(global_mo_path, backup_mo_path)


def get_mo(wowsdir, locale) -> MOFile:
    """Open and return the global MO file in the given directory."""
    return mofile(f"{wowsdir}/res/texts/{locale}/LC_MESSAGES/global.mo")


def restore_original_mo(wowsdir, locale):
    """Reinstate the original `global.mo` from `global.mo.original`."""
    global_mo_path = _global_mo_path(wowsdir, locale)
    backup_mo_path = _backup_mo_path(wowsdir, locale)
    if exists(backup_mo_path):
        _copyfile_and_checksum(backup_mo_path, global_mo_path)
        remove(backup_mo_path)


def _copyfile_and_checksum(from_path, to_path):
    """Copy a file from from_path to to_path.

    Raises OSError if the new file's checksum doesn't match the original."""
    copyfile(from_path, to_path)
    copystat(from_path, to_path)
    hasher = FileHash("md5")
    if hasher.hash_file(from_path) != hasher.hash_file(to_path):
        raise OSError("Copy failed, hash mismatch detected")


def _backup_mo_path(wowsdir, locale):
    return f"{_global_mo_path(wowsdir, locale)}.original"


def _global_mo_path(wowsdir, locale):
    return f"{wowsdir}/res/texts/{locale}/LC_MESSAGES/global.mo"
