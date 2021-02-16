#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main entrypoint for the wren CLI."""

from wren.cli import rename_ships

if __name__ == "__main__":
    # Click magically transforms the call, but pylint doesn't grok it…
    # pylint: disable=no-value-for-parameter,unexpected-keyword-arg
    rename_ships(prog_name="wren")
