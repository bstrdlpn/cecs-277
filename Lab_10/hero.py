import entity
import random

class Hero(entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)
        pos = [0,0] # starting position

    def attack(self, entity):
        """
        Hero attacks enemy, randomize damage in range 2-5.

        :returns: str; string representing action taken by hero
        """
        damage = random.randrange(2,5)
        entity.take_damage(damage)

        return f"{self.name} attacks a {entity.name} for {damage} damage!"
    
    def go_north(self):
        if pos[1] == 0:
            print("You can't move that way.")
        else:
            pos[1] += 1

    def go_south(self):
        if pos[1] == 4:
            print("You can't move that way.")
        else:
            pos[1] -= 1
    
    def go_east(self):
        if pos[0] == 0:
            print("You can't move that way.")
        else:
            pos[0] += 1
    
    def go_west(self):
        if pos[0] == 0:
            print("You can't move that way.")
        else:
            pos[0] -= 1