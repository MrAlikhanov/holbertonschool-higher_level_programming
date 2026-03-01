#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator to keep track of how many items have been processed.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated over.
    """

    def __init__(self, some_iterable):
        """
        Initializes the CountedIterator.

        Args:
            some_iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.count

    def __next__(self):
        """
        Increments the counter and returns the next item from the iterator.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
