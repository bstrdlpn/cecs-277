import vehicle
import random

class Motorcycle(vehicle.Vehicle):
    def __init__(self, name, initial, min_speed, max_speed):
        """calls the superclass's init with values for name (“Swift Bike”), 
        initial ('M'), min_speed (6), and max_speed (8)"""
        super().__init__(name, initial, min_speed, max_speed)
        self._name = "Swift Bike"
        self._initial = 'M'
        self.min_speed = 6
        self.max_speed = 8


    def slow(self, dist):
        """overridden method - passes in distance to the next obstacle (if there 
        is one). The motorcycle will move at 75% speed, rather than half. If 
        there's an obstacle, then it will go around it. There is no energy cost. 
        Return a string that describes the event that occurred with the name of 
        the motorcycle and the distance traveled (if applicable)"""
        move = round(random.randrange(self.min_speed, self.max_speed) * .75)

        if move + self._position > dist + self._position:
            self._position += move
            return f"{self._name} slowly and safely moves around the obstacle {move} units!"
        else:
            self._position += move
            return f"{self._name} slowly moves {move} units!"


    def description_string(self):
        """returns a string with the motorcycles's stats and abilities"""
        return f"{self._name} - a speedy motorcycle ({self.min_speed}-{self.max_speed}). Special: Wheelie (2x speed but there's a chance you'll crash)."

    def special_move(self, dist):
        """passes in distance to the next obstacle (if there is one). If there 
        is sufficient energy (>= 15), deduct 15 energy, then there is a 75% 
        chance that the motorcycle will move at 2x speed, otherwise it will 
        crash and only move one space forward. If it was successful but there is 
        an obstacle, then it will crash and stops in the space just before it, 
        otherwise it moves the randomized distance. Return a string that 
        describes the event that occurred with the name of the motorcycle and 
        the distance traveled (if applicable)"""

        chance = random.randint(1, 4)
        
        # if roll on chance is 4 - fail state
        if self._energy >= 15 and chance == 4:
            self._position += 1
            return f"{self._name} pops a wheelie and falls over!"
        # if roll is less than 4
        if self._energy >= 15 and chance < 4:
            move = random.randrange({self.min_speed}, {self.max_speed}) * 2
            # if there is an obstacle in the way
            if move + self._position > dist + self._position:
                self._position += dist - 1
                return f"{self._name} pops a wheelie and crashes into an obstacle!"
            # if there is no obstacle
            else:
                self._position += move
                return f"{self._name} pops a wheelie and moves {move} units!"

