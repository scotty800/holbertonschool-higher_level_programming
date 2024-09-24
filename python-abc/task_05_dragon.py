#!/usr/bin/env python3


class SwimMixin:
    """
    Mixin class that adds the ability to swim.
    """

    def swim(self):
        """
        Prints a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds the ability to fly.
    """

    def fly(self):
        """
        Prints a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, which can swim, fly, and roar.
    Inherits behaviors from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")
