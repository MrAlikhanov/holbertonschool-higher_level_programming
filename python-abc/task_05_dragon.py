#!/usr/bin/python3
"""
This module demonstrates the Mixin pattern in Python.
It defines SwimMixin and FlyMixin to provide modular behaviors
to a Dragon class.
"""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    It composes behaviors from multiple sources.
    """

    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
