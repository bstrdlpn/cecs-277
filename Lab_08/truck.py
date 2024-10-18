import vehicle
import random


class Truck(vehicle.Vehicle):
    """Represents a truck"""
    def __init__(self):
        """Calls the superclass constructor."""
        super().__init__('Behemoth Truck', 'T', 4, 8)

    def description_string(self):
        """Return a string with the truck's stats and abilities."""
        return f"{self._name} - a heavy truck ({self.min_speed}-{self.max_speed} units). Special: Ram (2x speed and it smashes through obstacles)."

    def special_move(self, dist):
        """
        Use Truck special move 'Ram'.
        
        :param dist: int type; distance to obstacle

        :returns: str type; string of action that occurs when 'Ram' encoounters 
        an obstacle (or not)
        """
         # insufficient energy
        if self.energy < 15:
            if self.energy >= 5:
                return self.fast(dist)
            else:
                return self.slow(dist)

        # calculate move
        move = random.randrange(self.min_speed, self.max_speed) * 2
        self._energy -= 15

        # if there are no further obstacles
        if dist is None:
            return f"{self._name} rams forward {move} units!"
        # there is an obstacle in the way, and we pass it
        elif self.position + move > self.position + dist:
            self._position += move
            return f"{self._name} rams forward bashing through the obstacle to go {move} units!"
        # other constraints don't apply
        else:
            self._position += move
            return f"{self._name} rams forward {move} units!"

