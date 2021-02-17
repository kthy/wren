# -*- coding: utf-8 -*-
"""Test the gettext manipulation methods."""

from os import makedirs, remove
from os.path import abspath, exists
from shutil import copyfile, rmtree
from tempfile import mkdtemp

from pytest import fixture, raises

from wren.pomo import (
    LC,
    backup_original_mo,
    compile_mo,
    install_modified_mo,
    prepare_po,
    restore_original_mo,
)

BIN = "1234567"


@fixture(name="workdir")
def fixture_workdir():
    """Yield working directory."""
    tmpdir = mkdtemp(prefix="wren-pytest-")
    print(f"Fixture workdir: {tmpdir}")
    yield tmpdir
    print("Teardown workdir")
    rmtree(tmpdir)


@fixture(name="wowsdir")
def fixture_wowsdir():
    """Yield WoWs directory."""
    tmpdir = mkdtemp(prefix="wren-pytest-") + BIN
    print(f"Fixture wowsdir: {tmpdir}")
    _prepare_global_mo(tmpdir)
    yield tmpdir
    print("Teardown wowsdir")
    rmtree(tmpdir)


def _prepare_global_mo(wowsbin):
    binlcdir = abspath(f"{wowsbin}/{LC}")
    makedirs(binlcdir)
    copyfile("./tests/testdata/global.mo", f"{binlcdir}/global.mo")
    assert exists(f"{binlcdir}/global.mo")


def test_backup_original_mo(wowsdir):
    """Test the backup_original_mo method."""
    assert exists(wowsdir)
    assert exists(f"{wowsdir}/{LC}/global.mo")
    assert not exists(f"{wowsdir}/{LC}/global.mo.original")
    backup_original_mo(wowsdir)
    assert exists(f"{wowsdir}/{LC}/global.mo")
    assert exists(f"{wowsdir}/{LC}/global.mo.original")


def test_compile_mo(workdir):
    """Test the compile_mo method"""
    raise NotImplementedError


def test_install_modified_mo(workdir, wowsdir):
    """Test the install_modified_mo method"""
    raise NotImplementedError


def test_prepare_po(workdir):
    """Test the prepare_po method"""
    raise NotImplementedError


def test_restore_original_mo(wowsdir):
    """Test the restore_original_mo method"""
    assert not exists(f"{wowsdir}/{LC}/global.mo.original")
    backup_original_mo(wowsdir)
    remove(f"{wowsdir}/{LC}/global.mo")
    assert not exists(f"{wowsdir}/{LC}/global.mo")
    restore_original_mo(wowsdir)
    assert exists(f"{wowsdir}/{LC}/global.mo")
