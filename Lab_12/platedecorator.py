import abc
import plate

class PlateDecorator(plate.Plate, abc.ABC):
    def __init__(self, p):
        """
        Constructs the PlateDecorator instance.

        :param p: object; plate object 
        """
        self._plate = p
    
    def description(self):
        """
        Return a string description of the plate and what is on it.
        """
        return self._plate.description()

    def area(self):
        """
        Return the remaining square inches the plate can hold.
        """
        return self._plate.area()

    def weight(self):
        """
        Return the remaining number of ounces the plate can hold.
        """
        return self._plate.weight()

    def count(self):
        """
        Return the number of food items the plate is currently holding.
        """
        return self._plate.count()