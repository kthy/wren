# -*- coding: utf-8 -*-
"""Test the gettext manipulation methods."""

from os import remove
from os.path import exists

from fixtures import fixture_wowsdir  # pylint: disable=unused-import

from wren.pomo import backup_original_mo, restore_original_mo

LC = "res/texts/en/LC_MESSAGES"


def test_backup_original_mo(wowsdir):
    """Test the backup_original_mo method."""
    assert exists(wowsdir)
    assert exists(f"{wowsdir}/{LC}/global.mo")
    assert not exists(f"{wowsdir}/{LC}/global.mo.original")
    backup_original_mo(wowsdir, "en")
    assert exists(f"{wowsdir}/{LC}/global.mo")
    assert exists(f"{wowsdir}/{LC}/global.mo.original")


def test_restore_original_mo(wowsdir):
    """Test the restore_original_mo method"""
    assert not exists(f"{wowsdir}/{LC}/global.mo.original")
    backup_original_mo(wowsdir, "en")
    remove(f"{wowsdir}/{LC}/global.mo")
    assert not exists(f"{wowsdir}/{LC}/global.mo")
    restore_original_mo(wowsdir, "en")
    assert exists(f"{wowsdir}/{LC}/global.mo")
