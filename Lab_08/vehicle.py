import abc
import random

class Vehicle(abc.ABC):
    """
    Abstract superclass representing vehicles.

    Attributes:
    -----------
    _name: vehicle name
    _initial: vehicle initial speed
    min_speed: min val of speed range
    max_speed: max val of speed range
    _position: vehicle position on track
    _energy: vehicle power level

    """

    def __init__(self, name, initial, min_speed, max_speed):
        """
        Abstract constructor

        :param name: str type; vehicle name
        :param initial: vehicle initial speed
        :param min_speed: min val of speed range
        :param max_speed: max val of speed range
        """
        self._name = name
        self._initial = initial
        self.min_speed = min_speed
        self.max_speed = max_speed
        self._position = 0
        self._energy = 100
    
    @property
    def initial(self)
        return self._initial

    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy

    def fast(self, dist):
        """
        Pass in the distance to the next obstacle (if there is one). If there is
        sufficient energy (>=5), randomize a value between min and max speed for
        the number of spacees they will move and deduct 5 energy. If that movement
        is less than the distance to the next obstacle, then they move that amount,
        otherwise, it crashes into the obstacle and stops in the space just before
        the obstacle. Return a string that describes the event that occurred 
        with the name of the vehicle and the distance traveled (if applicable).
        """
        if self.energy() >= 5:
            move = random.randrange(self.min_speed, self.max_speed)
            self._position += move
            self._energy -= 5
        else:
            # what does the vehicle do if energy < 5?
            pass

        # crash into the obstacle and stop before it
        if move < dist:
            move = dist - 1
            self._position += move
            # return a string that describes the event that occurred with name of vehicle and distance travelled
            return f"{self._name} CRASHES into an obstacle"


    def slow(self, dist):
        """
        Pass in the distance to the next obstacle (if there is one). The vehicle 
        will move at half speed. If there is an obstacle, then it will go around 
        it. No energy cost. Return string that describes the event that occurred
        with the name of he vehicle and distance traveled (if applicable).
        """
        pass

    def __str__(self):
        return {self._name}, self.position(), self.energy()

    @abc.abstractmethod
    def description_string(self):
        pass

    @abc.abstractmethod
    def special_move(self, dist):
        pass