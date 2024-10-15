import vehicle

class Car(vehicle.Vehicle):
    def __init__(self):
        """calls the superclass’s init with values for name (“Lightning Car”),
        initial (‘C’), min_speed (6), and max_speed (8)"""
        pass

    def description_string(self):
        """returns a string with the car’s stats and abilities"""
        pass

    def special_move(self, dist):
        """passes in the distance to the next obstacle (if there is
        one). If there is sufficient energy (>= 15), deduct 15 energy and move the car at 1.5x
        speed. If there is an obstacle, then it will crash and stops in the space just before it,
        otherwise it moves the randomized distance. Return a string that describes the event that
        occurred with the name of the car and the distance traveled (if applicable)."""
        pass

