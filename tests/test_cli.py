# -*- coding: utf-8 -*-
"""Test the wren CLI."""

from os import makedirs
from os.path import abspath

from fixtures import fixture_wowsdir  # pylint: disable=unused-import

from wren.cli import _bindir


def test__bindir(wowsdir):
    """Test the _bindir method."""
    bin_path = abspath(wowsdir + "/..")
    assert _bindir(bin_path) == "7777777"
    for subdir in ("1111111", "2222222", "3333333", "4444444", "5555555", "6666666"):
        makedirs(f"{bin_path}/{subdir}")
    assert _bindir(bin_path) == "7777777"
    makedirs(f"{bin_path}/8888888")
    assert _bindir(bin_path) == "8888888"
