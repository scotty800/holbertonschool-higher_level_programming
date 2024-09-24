#!/usr/bin/env python3


class VerboseList(list):
    """
    A subclass of the built-in list that provides verbose output
    when performing common list operations.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a message.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extends the list by appending elements from
        an iterable and prints a message.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """
        Removes the first occurrence of an item
        from the list and prints a message.
        Raises a ValueError if the item is not found.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            raise ValueError("Item [{}] not found in the list.".format(item))

    def pop(self, index=-1):
        """
        Removes and returns the item at the given position in the list.
        Prints a message and raises a ValueError if the list is empty.
        """
        if self:
            item = self[index]
            print("Popped [{}] from the list.".format(item))
            return super().pop(index)
        else:
            raise ValueError("Cannot pop from an empty list.")
