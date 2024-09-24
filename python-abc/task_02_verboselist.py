#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items".format(len(iterable)))

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            raise ValueError("Item [{}] not found in the list".format(item))

    def pop(self, index=-1):
        if self:
            item = self[index]
            print("Popped [{}] from the list.".format(item))
            super().pop(index)
        else:
            raise ValueError("Cannot pop from an empty list.")