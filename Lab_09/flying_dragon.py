import dragon
import flying
import random

class FlyingDragon(dragon.Dragon, flying.FlyingMixin):
    def __init__(self, name, max_hp, num_sp):
        """
        call super to seat a default name, hp and number of special attacks
        """
        super().__init__('Timberjack', 10, 3)

    def special_attack(self, opponent):
        """
        randomly choose one of the two flying attack methods from FlyingMixin
        """
        attack = random.randchoice([self.swoop, self.windblast])
        
        attack(opponent)