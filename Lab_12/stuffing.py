import platedecorator

class Stuffing(platedecorator.PlateDecorator):
    def description(self):
        """
        Call superclass description and additional description.
        """
        if self.count() <= 1:  
            return super().description() + " Stuffing"
        else:
            return super().description() + " and Turkey"

    def area(self):
        """
        Call superclass area and subtract Stuffing area
        """
        return super().area() - 18

    def weight(self):
        """
        Call superclass weight and subtract Stuffing weight
        """
        return super().weight() - 7

    def count(self):
        """
        Call superclass method and add 1 to increment counter
        """
        return super().count() + 1
