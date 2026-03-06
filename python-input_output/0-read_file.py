#!/usr/bin/python3
"""Module for reading a file and printing its content to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
