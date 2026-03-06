#!/usr/bin/python3
"""Module for appending a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
