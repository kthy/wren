# -*- coding: utf-8 -*-
"""Classes representing a textual change."""

from enum import Enum, unique

from polib import MOFile


@unique
class Action(Enum):
    """A value representing a type of action."""

    PREFIX = "prefix_value"
    REPLACE = "replace_value"

    def __repr__(self):
        return f'Action("{self.value}")'


class Change:
    """A class representing a textual change."""

    def __init__(self, action, msgid, value):
        self.action = Action(action)
        self.msgid = msgid
        self.value = value

    def __eq__(self, other):
        return all(
            [
                self.action == other.action,
                self.msgid == other.msgid,
                self.value == other.value,
            ]
        )

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return f'Change("{self.action.value}", "{self.msgid}", "{self.value}")'

    def apply(self, mo_file: MOFile):
        """Apply this change to the given MOFile."""
        entry = next(filter(lambda m: m.msgid == self.msgid, mo_file))
        if self.is_prefix():
            entry.msgstr = self.value + entry.msgstr
        else:
            entry.msgstr = self.value

    def is_prefix(self) -> bool:
        """Return True if this is a PREFIX change."""
        return self.action is Action.PREFIX

    def is_replace(self) -> bool:
        """Return True if this is a REPLACE change."""
        return self.action is Action.REPLACE
