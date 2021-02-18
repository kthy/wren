# -*- coding: utf-8 -*-
"""Gettext manipulation methods."""

from os import remove
from shutil import copyfile

from filehash import FileHash

LC = "res/texts/en/LC_MESSAGES"


def backup_original_mo(wowsdir):
    """Copy the original `global.mo` to `global.mo.original`."""
    global_mo_path = _global_mo_path(wowsdir)
    backup_mo_path = _backup_mo_path(wowsdir)
    _copyfile_and_checksum(global_mo_path, backup_mo_path)


def compile_mo(workdir):
    """Convert `workdir/global.po` using `msgfmt` into `workdir/global.mo`"""
    raise NotImplementedError


def install_modified_mo(workdir, wowsdir):
    """Copy the new `global.mo` to where the original was."""
    raise NotImplementedError


def prepare_po(workdir):
    """Convert `${wowsPath}/res/texts/en/LC_MESSAGES/global.mo` to `workdir/global.po`"""
    raise NotImplementedError


def restore_original_mo(wowsdir):
    """Reinstate the original `global.mo` from `global.mo.original`."""
    global_mo_path = _global_mo_path(wowsdir)
    backup_mo_path = _backup_mo_path(wowsdir)
    _copyfile_and_checksum(backup_mo_path, global_mo_path)
    remove(backup_mo_path)


def _copyfile_and_checksum(from_path, to_path):
    """Copy a file from from_path to to_path.

    Raises OSError if the new file's checksum doesn't match the original."""
    copyfile(from_path, to_path)
    hasher = FileHash("md5")
    if hasher.hash_file(from_path) != hasher.hash_file(to_path):
        raise OSError("Copy failed, hash mismatch detected")


def _backup_mo_path(wowsdir):
    return f"{_global_mo_path(wowsdir)}.original"


def _global_mo_path(wowsdir):
    return f"{wowsdir}/{LC}/global.mo"
