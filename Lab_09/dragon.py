import entity
import random

class Dragon(entity.Entity):
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp)
        self._special_attacks = num_sp

    def decrement_special_attacks(self):
        """
        Subtract 1 from _special_attacks. If value becomes negative, set to 0.
        """
        self._special_attacks -= 1

        # if the num of special attacks is negative set to 0
        if self._special_attacks < 0:
            self._special_attacks = 0

    def basic_attack(self, hero):
        """
        Tail attack, the hero takes a random amount of damage in the range 3-7. 
        Return a string with the desc of the attack and the damage dealt to the 
        hero.
        """
        damage = random.randrange(3,7)
        hero.take_damage(damage)

        return f"{self.name} smashes you with its tail for {damage} damage!"

    def __str__(self):
        """
        use super to get the __str__ from the entity class, then concatenate on 
        then number of special attacks remaining.
        """
        return super().__str__() + " Special attacks remaining: " + str(self._special_attacks)