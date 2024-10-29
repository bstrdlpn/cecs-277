"""
Extends entity - monster character that the hero encounters in the maze.
"""
import entity
import random

class Enemy(entity.Entity):
    def __init__(self, name, max_hp):
        super().__init__(random.choice(['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie'],
        random.randrange(4, 8)))
    
    def attack(self, entity):
        dmg = random.randrange(1,4)
        entity.take_damage(dmg)

        return f"{self.name} attacks {entity.name} for {dmg} damge."

