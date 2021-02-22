# -*- coding: utf-8 -*-
"""Test the wren CLI."""

from os import makedirs
from os.path import abspath

from click import ClickException
from config import Config
from fixtures import fixture_config, fixture_wowsdir  # pylint: disable=unused-import
from pytest import raises

from wren.cli import (
    _bindir,
    default_changesets,
    get_warship_directory,
    load_config,
    raise_if_not_path_exists,
)


def test_default_changesets():
    """Test the default_changesets method."""
    assert default_changesets() == ["radar"]


def test_get_warship_directory(config, wowsdir):
    """Test the get_warship_directory method."""
    assert get_warship_directory(config) == wowsdir


def test_load_config():
    """Test the load_config method."""
    cfg = load_config("./tests/testdata/test.cfg")
    assert isinstance(cfg, Config)


def test_raise_if_not_path_exists_no_raise(wowsdir):
    """Test the raise_if_not_path_exists method (no error raised)."""
    assert raise_if_not_path_exists("dummy", wowsdir) is None


def test_raise_if_not_path_exists_raises(wowsdir):
    """Test the raise_if_not_path_exists method (error raised)."""
    with raises(ClickException):
        raise_if_not_path_exists("dummy", f"{wowsdir}\\foobar")


def test__bindir(wowsdir):
    """Test the _bindir method."""
    bin_path = abspath(wowsdir + "/..")
    assert _bindir(bin_path) == "7777777"
    makedirs(f"{bin_path}/8888888")
    assert _bindir(bin_path) == "8888888"


def test__bindir_raises():
    """Test when _bindir method raises ValueError."""
    with raises(ValueError):
        _bindir("C:\\")
