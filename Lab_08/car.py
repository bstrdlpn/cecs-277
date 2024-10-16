import vehicle
import random

class Car(vehicle.Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        """
        calls the superclass's init with values for name (“Lightning Car”),
        initial ('C'), min_speed (6), and max_speed (8)
        """
        super().__init__(name, initial, min_speed, max_speed)
        name = "Lightning Car"
        initial = 'C'
        self.min_speed = min_speed = 6
        max_speed = 8

    def description_string(self):
        """returns a string with the car's stats and abilities"""
        return "Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)"

    def special_move(self, dist):
        """passes in the distance to the next obstacle (if there is
        one). If there is sufficient energy (>= 15), deduct 15 energy and move 
        the car at 1.5x speed. If there is an obstacle, then it will crash and 
        stops in the space just before it, otherwise it moves the randomized 
        distance. Return a string that describes the event that occurred with 
        the name of the car and the distance traveled (if applicable)."""
        if self._energy >= 15:
            move = random.randrange(self.min_speed * 1.5, self.max_speed * 1.5)

        if move + self._position > dist + self._position:
            self._energy -= 15
            move = self._position + (dist - 1)
            self._position += move
            return f"{self._name} CRASHES into an obstacle"
        else:
            self._position += move
            return f"Lightning Car uses nitro boost and moves {move} units!"

