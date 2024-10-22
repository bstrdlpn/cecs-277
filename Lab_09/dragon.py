import entity

class Dragon(entity.Entity):
    def __init__(self, name, max_hp, num_sp):
        super().__init__()
        _special_attacks = num_sp

    def decrement_special_attacks(self):
        """
        Subtract 1 from _special_attacks. If value becomes negative, set to 0.
        """
        pass

    def basic_attack(self, opponent):
        """
        Tail attack, the hero takes a random amount of damage in the range 3-7. 
        Return a string with the desc of the attack and the damage dealt to the 
        hero.
        """
        pass

    def __str__(self):
        """
        use super to get the __str__ from the entity class, then concatenate on 
        then number of special attacks remaining.
        """
        pass