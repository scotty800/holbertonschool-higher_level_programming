#!/usr/bin/env python3


class CountedIterator:
    """
    A custom iterator that keeps track of
    the number of items it has iterated over.
    """
    def __init__(self, some_iterable):
        """
        Initializes the iterator with an iterable and
        sets the initial count to 0.
        Args:
        some_iterable: An iterable object to be iterated over.
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current count of items iterated over.
        """
        return self.count

    def __next__(self):
        """
        Returns the next item from the iterable,
        incrementing the count.
        Raises:
        StopIteration: When the iterable is exhausted.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator itself.
        """
        return self
