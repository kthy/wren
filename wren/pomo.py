# -*- coding: utf-8 -*-
"""Gettext manipulation methods."""

from os import remove
from shutil import copyfile

from filehash import FileHash

LC = "res/texts/en/LC_MESSAGES"

def backup_original_mo(wowsdir):
    """Copy the original `global.mo` to `global.mo.original`."""
    global_mo_path = f"{wowsdir}/{LC}/global.mo"
    backup_mo_path = f"{global_mo_path}.original"
    copyfile(global_mo_path, backup_mo_path)
    hasher = FileHash("md5")
    if hasher.hash_file(global_mo_path) != hasher.hash_file(backup_mo_path):
        raise OSError("Copy failed, hash mismatch detected")

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
    global_mo_path = f"{wowsdir}/{LC}/global.mo"
    backup_mo_path = f"{global_mo_path}.original"
    copyfile(backup_mo_path, global_mo_path)
    hasher = FileHash("md5")
    if hasher.hash_file(global_mo_path) != hasher.hash_file(backup_mo_path):
        raise OSError("Copy failed, hash mismatch detected")
    remove(backup_mo_path)
