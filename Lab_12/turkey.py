import platedecorator

class Turkey(platedecorator.PlateDecorator):
    def description(self):
        """
        Call superclass description and additional description.
        """
        if self.count() <= 1:  
            return super().description() + " Turkey"
        else:
            return super().description() + " and Turkey"

    def area(self):
        """
        Call superclass area minus Turkey area
        """
        return super().area() - 15

    def weight(self):
        """
        Call superclass weight minus Turkey weight
        """
        return super().weight() - 4

    def count(self):
        """
        Call superclass method and add 1 to increment counter
        """
        return super().count() + 1
