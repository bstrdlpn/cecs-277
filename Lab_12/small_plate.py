import plate

class SmallPlate(plate.Plate):
    def description(self):
        """
        Return a string description of the plate and what is on it.
        """
        return "Sturdy 10 inch paper plate with"

    def area(self):
        """
        Return the remaining square inches the plate can hold.
        """
        return 78

    def weight(self):
        """
        Return the remaining number of ounces the plate can hold.
        """
        return 32

    def count(self):
        """
        Return the number of food items the plate is currently holding.
        """
        return 0