#!/usr/bin/python3
"""
This module defines the VerboseList class.
It extends the built-in list class to provide notifications
when items are added or removed.
"""


class VerboseList(list):
    """
    A custom list class that prints messages upon modification.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints a notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
