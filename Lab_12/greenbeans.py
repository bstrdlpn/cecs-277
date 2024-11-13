import platedecorator

class GreenBeans(platedecorator.PlateDecorator):
    def description(self):
        """
        Call superclass description and additional description.
        """
        if self.count() <= 1:  
            return super().description() + " Green Beans"
        else:
            return super().description() + " and Green Beans"

    def area(self):
        """
        Call superclass area and subtract GreenBeans area
        """
        return super().area() - 20

    def weight(self):
        """
        Call superclass weight and subtract GreenBeans weight
        """
        return super().weight() - 3

    def count(self):
        """
        Call superclass method and add 1 to increment counter
        """
        return super().count() + 1
