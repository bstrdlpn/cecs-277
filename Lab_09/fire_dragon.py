import dragon
import fire
import random


class FireDragon(dragon.Dragon, fire.FireMixin):
    def __init__(self, name, max_hp, num_sp):
        """
        call super() top set a default name, hp, and number of special attacks
        """
        super().__init__('Gronkle', 15, 3)

    def special_attack(self, opponent):
        """
        randomly choose one of the two fire attack methods from the fire mixin
        """
        attack = random.choice([self.fireball, self.fireblast])

        attack(opponent)