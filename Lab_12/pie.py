import platedecorator

class Pie(platedecorator.PlateDecorator):
    def description(self):
        """
        Call superclass description and additional description.
        """
        if self.count() <= 1:  
            return super().description() + " Pie"
        else:
            return super().description() + " and Pie"

    def area(self):
        """
        Call superclass area and subtract Pie area
        """
        return super().area() - 19

    def weight(self):
        """
        Call superclass weight and subtract Pie weight
        """
        return super().weight() - 8

    def count(self):
        """
        Call superclass method and add 1 to increment counter
        """
        return super().count() + 1
