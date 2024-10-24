import random

class FireMixin:
    def fireblast(self, opponent):
        """
        if the dragon has any special attacks left, then it blasts the hero with
        fire and they take a random amount of damage in range 5-9. Decrement sp
        attacks. Return a string with a desc of the attack and damage dealt to
        hero, otherwise, no damage done, and a string desc failure returned.
        """
        if self._special_attacks > 0:
            self.decrement_special_attacks()
            damage = random.randrange(5, 9)
            opponent.take_damage(damage)
            return f"{self.name} engulfs {opponent.name} in flames for {damage} damage!"
        else:
            return f"{self.name} tries to engulf {opponent.name} in flames, but it is all out of fuel."

    def fireball(self, opponent):
        """
        if the dragon has any special attacks left, then it spits a fireball at 
        the hero and they take a random amount of damage in range 408, decrement 
        sp attacks. Return str with a desc of the attack and damage dealt to hero.
        Otherwise, no damage, and string describing failure is returned.
        """
        if self._special_attacks > 0:
            self.decrement_special_attacks()
            damage = random.randrange(4, 8)
            opponent.take_damage(damage)
            return f"{self.name} spits a fireball at {opponent.name} for {damage} damage!"
        else:
            return f"{self.name} tries to engulf {opponent.name} in flames, but it is all out of fuel." 