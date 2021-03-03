# -*- coding: utf-8 -*-
"""Test fixtures."""

from os import environ, makedirs
from os.path import abspath, exists
from shutil import copyfile, rmtree
from tempfile import mkdtemp

from config import Config
from pytest import fixture

WRENTMPDIR = f"{mkdtemp(prefix='wren-pytest-')}"

for b in ("1111111", "2222222", "3333333", "4444444", "5555555", "6666666", "7777777"):
    makedirs(abspath(f"{WRENTMPDIR}/bin/{b}"))


@fixture(name="config")
def fixture_config():
    """Yield config object."""
    environ["WRENTMPDIR"] = WRENTMPDIR + "\\bin"
    cfg = Config("./tests/testdata/test.cfg")
    yield cfg


@fixture(name="wowsdir")
def fixture_wowsdir():
    """Yield WoWs directory."""
    _prepare_global_mo(f"{WRENTMPDIR}\\bin\\7777777")
    yield f"{WRENTMPDIR}\\bin\\7777777"
    rmtree(WRENTMPDIR)


def _prepare_global_mo(wowsbin):
    binlcdir = abspath(f"{wowsbin}/res/texts/en/LC_MESSAGES")
    makedirs(binlcdir)
    copyfile("./tests/testdata/global.mo", f"{binlcdir}/global.mo")
    assert exists(f"{binlcdir}/global.mo")
