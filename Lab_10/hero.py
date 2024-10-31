import entity
import map
import random

class Hero(entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)
        
        # starting position at [0,0]
        self._loc = [0,0]

    @property
    def loc(self):
        return self._loc

    def attack(self, entity):
        """
        Hero attacks enemy, randomize damage in range 2-5.

        :returns: str; string representing action taken by hero
        """
        damage = random.randrange(2,5)
        entity.take_damage(damage)

        return f"{self.name} attacks a {entity.name} for {damage} damage!"
    
    def go_north(self):
        """Move hero North."""
        current_row = self.loc[0]

        if current_row > 0:
            self._loc = [current_row - 1, self.loc[1]]
            return self._map[self.loc]
        else:
            return 'o'

    def go_south(self):
        """Move hero South."""
        current_row = self.loc[0]

        if current_row < 4:
            self._loc = [current_row + 1, self.loc[1]]
            return self._map[self.loc]
        else:
            return 'o'

    def go_east(self):
        """Move hero East."""
        current_col = self.loc[1]

        if current_col < 4:
            self._loc = [self.loc[0], current_col + 1]
            return self._map[self.loc]
        else:
            return 'o'

    def go_west(self):
        """Move hero West."""
        current_col = self.loc[1]

        if current_col > 0:
            self._loc = [self.loc[0], current_col - 1]
            return self._map[self.loc]
        else:
            return 'o'