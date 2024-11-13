import abc
"""
Abstract plate interface.
"""

class Plate(abc.ABC):
    def description(self):
        """
        Return a string description of the plate and what is on it.
        """
        pass

    def area(self):
        """
        Return the remaining square inches the plate can hold.
        """
        pass

    def weight(self):
        """
        Return the remaining number of ounces the plate can hold.
        """
        pass

    def count(self):
        """
        Return the number of food items the plate is currently holding.
        """
        pass
    