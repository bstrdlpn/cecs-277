import entity
import random

class Hero(entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)

    def basic_attack(self, opponent):
        """
        The dragon takes a random amount of damage in the range 2D6. Return a 
        string with the description of the attack and the damage dealt to the 
        dragon.
        """
        damage = random.randrange(1,6) + random.randrange(1,6)
        opponent.take_damage(damage)

        return f"{self.name} slashes the {opponent.name} with their sword for {damage} damage!"

    def special_attack(self, opponent):
        """
        The dragon takes a random amount of damage in the range 1D12. Return a 
        string with the description of the attack and the damage dealt to the 
        dragon.
        """
        damage = random.randrange(1, 12)
        opponent.take_damage(damage)
        
        return f"{self.name} hits the {opponent.name} with an arrow for {damage} damage!"
