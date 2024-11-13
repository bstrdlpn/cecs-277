import platedecorator

class Potatoes(platedecorator.PlateDecorator):
    def description(self):
        """
        Call superclass description and additional description.
        """
        if self.count() <= 1:  
            return super().description() + " Potatoes"
        else:
            return super().description() + " and Potatoes"

    def area(self):
        """
        Call superclass area and subtract Potatoes area
        """
        return super().area() - 18

    def weight(self):
        """
        Call superclass weight and subtract Potatoes weigght
        """
        return super().weight() - 6

    def count(self):
        """
        Call superclass method and add 1 to increment counter
        """
        return super().count() + 1
