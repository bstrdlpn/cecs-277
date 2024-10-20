import vehicle
import random

class Motorcycle(vehicle.Vehicle):
    def __init__(self):
        """calls the superclass's init with values for name (“Swift Bike”), 
        initial ('M'), min_speed (6), and max_speed (8)"""
        super().__init__('Swift Bike', 'M', 6, 8)

    def slow(self, dist):
        """
        overridden method - 75% speed

        :param dist: int type; distance to the next obstacle
        """
        move = round(random.randrange(self.min_speed, self.max_speed) * .75)

        # if there are no further obstacles
        if dist is None:
            self._position += move
            return f"{self._name} slowly moves {move} units"
        # there is an obstacle in the way and we pass it
        if move + self.position > dist + self.position:
            self._position += move
            return f"{self._name} slowly and safely moves around the obstacle {move} units!"
        # no matches to other conditions
        else:
            self._position += move
            return f"{self._name} slowly moves {move} units!"

    def description_string(self):
        """returns a string with the motorcycles's stats and abilities"""
        return f"{self._name} - a speedy motorcycle ({self.min_speed}-{self.max_speed}). Special: Wheelie (2x speed but there's a chance you'll crash)."

    def special_move(self, dist):
        """
        Wheelie special ability. 25 percent chance of failure. 

        :param dist: int type; dist from player to obstacle

        :returns: str type; str describing the action
        """

        chance = random.randint(1, 4)
       
        # insufficient energy
        if self.energy < 15:
            if self.energy >= 5:
                return self.fast(dist)
            else:
                return self.slow(dist)
        
        # if roll on chance is 4: fail state
        if chance == 4:
            self._energy -= 15
            self._position += 1
            return f"{self._name} pops a wheelie and falls over!"
        # if roll is less than 4, successful chance roll
        elif chance < 4:
            self._energy -= 15
            move = random.randrange(self.min_speed, self.max_speed) * 2
            # if there are no further obstacles
            if dist is None:
                self._position += move
                return f"{self._name} pops a wheelie and moves {move} units!"
            # if there is an obstacle in the way, and we move past that distance
            elif move + self.position > dist + self.position:
                self._position += dist - 1
                return f"{self._name} pops a wheelie and crashes into an obstacle!"
            # doesn't fit other constraints
            else:
                self._position += move
                return f"{self._name} pops a wheelie and moves {move} units!"

