import random

class Die():
    """
    A die with n number of sides.
    
    Attributes:
        sides (int): The number of sides of the die
        value (int): The value of the rolled die.
    """

    def __init__(self, sides=6):
        """Set the number of sides of the die. Default = 6."""
        self._sides = sides
        self._value = self.roll()


    def roll(self):
        """Roll the die to set the value of the die."""
        self._value = random.randint(1, self._sides)
        return self._value
    

    def __str__(self):
        """Return the string representation of the die."""
        return str(self._value)

    def __lt__(self, other):
        """
        Compare the two dice to see if self's value is less than the other's 
        value.
        """
        return self._value < other._value

    def __eq__(self, other):
        """
        Compare the two dice to see if self's value is equal to other's value.
        """
        return self._value == other._value

    def __sub__(self, other):
        """Return the difference between self's value and other's value."""
        return self._value - other._value
