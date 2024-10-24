import random

class FlyingMixin:
    def swoop(self, opponent):
        """
        if dragon has any sp attacks left, then it does a swoop attack at the 
        hero and they take a random amount f damage in the range 4-8 and the 
        number of sp attacks is decremented. Return a str with desc attack and 
        damage dealt ot hero, otherwise, no damage done, str desc failure return.
        """
        if self._special_attacks > 0:
            self.decrement_special_attacks()
            damage = random.randrange(4, 8)
            opponent.take_damage(damage)
            return f"{self.name} takes to the skies and swoops down dealing {damage} damage to {opponent.name}!"
        else:
            return f"{self.name} attempts to take flight, but is all out of energy."

    def windblast(self, opponent):
        """
        if the dragon has any sp attacks left, blasts wind at hero and they take 
        a random amount of damage in range 3-7 and num sp attacks is decremented.
        Return a string with a desc of the attack and damage dealt. Otherwise,
        no damage done, and string describing failure is returned.
        """
        if self._special_attacks > 0:
            self.decrement_special_attacks()
            damage = random.randrange(3, 7)
            opponent.take_damage(damage)
            return f"{self.name} flaps its wings and blasts {opponent.name} for {damage} damage!"
        else:
            return f"{self.name} attempts to move its wings, but is all out of energy."