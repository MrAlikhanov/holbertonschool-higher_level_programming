#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python.
It defines Fish and Bird parent classes and a FlyingFish subclass.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Subclass representing a flying fish, inheriting from Fish and Bird.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both parents' habitat method."""
        print("The flying fish lives both in water and the sky!")
