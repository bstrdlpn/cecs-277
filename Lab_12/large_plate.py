import plate

class LargePlate(plate.Plate):
    def description(self):
        """
        Return a string description of the plate and what is on it.
        """
        return "Flimsy 12 inch paper plate with"

    def area(self):
        """
        Return the remaining square inches the plate can hold.
        """
        return 113

    def weight(self):
        """
        Return the remaining number of ounces the plate can hold.
        """
        return 24

    def count(self):
        """
        Return the number of food items the plate is currently holding.
        """
        return 0