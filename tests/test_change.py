# -*- coding: utf-8 -*-
"""Test the Action and Change."""

from wren.change import Action, Change


def test_action___repr__():
    """Test the __repr__ method of the Action enum."""
    action = Action.REPLACE
    lazarus = eval(repr(action))  # pylint: disable=eval-used
    assert lazarus is Action.REPLACE


def test_change_is_prefix():
    """Test the is_prefix method of the Change class."""
    change_prefix = Change(Action.PREFIX.value, "", "")
    change_replace = Change(Action.REPLACE.value, "", "")
    assert change_prefix.is_prefix()
    assert not change_replace.is_prefix()


def test_change_is_replace():
    """Test the is_prefix method of the Change class."""
    change_prefix = Change(Action.PREFIX.value, "", "")
    change_replace = Change(Action.REPLACE.value, "", "")
    assert not change_prefix.is_replace()
    assert change_replace.is_replace()


def test_change___repr__():
    """Test the __repr__ method of the Change class."""
    change = Change("prefix_value", "IDS_PRSC108", "φ12 ")
    lazarus = eval(repr(change))  # pylint: disable=eval-used
    assert lazarus == change
