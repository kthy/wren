# -*- coding: utf-8 -*-
"""Test fixtures."""

from os import makedirs
from os.path import abspath, exists
from shutil import copyfile, rmtree
from tempfile import mkdtemp

from pytest import fixture

from wren.pomo import LC

BIN = "7777777"
TEST_MO_PATH = "./tests/testdata/global.mo"


@fixture(name="workdir")
def fixture_workdir():
    """Yield working directory."""
    tmpdir = mkdtemp(prefix="wren-pytest-")
    yield tmpdir
    rmtree(tmpdir)


@fixture(name="wowsdir")
def fixture_wowsdir():
    """Yield WoWs directory."""
    tmpdir = f"{mkdtemp(prefix='wren-pytest-')}/{BIN}"
    _prepare_global_mo(tmpdir)
    yield tmpdir
    rmtree(tmpdir)


def _prepare_global_mo(wowsbin):
    binlcdir = abspath(f"{wowsbin}/{LC}")
    makedirs(binlcdir)
    copyfile(TEST_MO_PATH, f"{binlcdir}/global.mo")
    assert exists(f"{binlcdir}/global.mo")
