# -*- coding: utf-8 -*-
"""Classes representing a textual change."""

from enum import Enum, unique


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
        print(self)

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
