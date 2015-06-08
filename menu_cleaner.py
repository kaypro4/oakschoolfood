# Converts a menu into a list of strings, for which each string should
# represent a menu item.
# Code is very specific to OUSD menus
from __future__ import absolute_import, division, print_function


def clean_menu(file):
    """Converts a menu with word wrapping into one line per food item"""
    with open(file) as f:
        lines = f.readlines()
        cleaned = _clean_menu_lines(lines)
    return cleaned


def _clean_menu_lines(lines):
    """Converts lines, which may wrap, into one line per real menu item"""

    # TODO, rather than combining line, would be better to make them separate
    # That will make it easier to get caloric content.
    # Also, should take distinct set at end, since OUSD often enters milk twice.

    # List of character strings that commonly appear before or after a menu item wraps
    connectors = (" w", "w ", "with", "+", "&")

    cleaned = []
    append_next = False
    for line in lines:
        line = _remove(line)
        if append_next:
            cleaned[-1] = cleaned[-1] + " " + line
            append_next = False
        elif line.endswith(connectors):
            append_next = True
            cleaned.append(line)
        elif line.startswith(connectors):
            cleaned[-1] = cleaned[-1] + " " + line
        else:
            cleaned.append(line)

    # whitespace begone
    cleaned = [item.strip() for item in cleaned]
    return cleaned


def _remove(item):
    """Removes characters we don't want to keep around"""

    # TODO: replace list with regex patterns per menu source
    removers = ('\n', '(V)', '(V,P)', '(P)', '(V,FP)', '(FP)')
    removed = item
    for remover in removers:
        removed = removed.replace(remover, '')
    return removed
