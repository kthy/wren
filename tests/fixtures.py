# -*- coding: utf-8 -*-
"""Test fixtures."""

from os import makedirs
from os.path import abspath, exists
from shutil import copyfile, rmtree
from tempfile import mkdtemp

from pytest import fixture

BIN = "7777777"
TEST_MO_PATH = "./tests/testdata/global.mo"


@fixture(name="wowsdir")
def fixture_wowsdir():
    """Yield WoWs directory."""
    tmpdir = f"{mkdtemp(prefix='wren-pytest-')}/{BIN}"
    _prepare_global_mo(tmpdir)
    yield tmpdir
    rmtree(tmpdir)


def _prepare_global_mo(wowsbin):
    binlcdir = abspath(f"{wowsbin}/res/texts/en/LC_MESSAGES")
    makedirs(binlcdir)
    copyfile(TEST_MO_PATH, f"{binlcdir}/global.mo")
    assert exists(f"{binlcdir}/global.mo")
