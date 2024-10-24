import dragon
import flying
import fire
import random

class FlyingFireDragon(dragon.Dragon, fire.FireMixin, flying.FlyingMixin):
    def __init__(self, name, max_hp):
        """
        call super to seat a default name, hp and number of special attacks
        """
        super().__init__('Deadly Nadder', 20, 2)

    def special_attack(self, opponent):
        """
        randomly choose one of the four flying and fire attack methods from mixins
        """
        attack = random.randomchoice([self.swoop, self.windblast, self.fireblast, self.fireball])

        attack(opponent)