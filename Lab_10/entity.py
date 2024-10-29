"""
Abstract class that describes a character in the game

Attributes
----------

:attribute name: str; name of monster
:attribute _hp: int; current hp of entity
:attribute max_hp: int; max hp of entity

Methods
-------

take_damage(self, dmg): subtracts the dmg from hp, but does not allow the hp to 
    drop below 0
heal(self): restore the entity's hp to max_hp
__str__(self): returns a string in the format 'Name\nHP: hp/max_hp'
attack(self, entity): abstract method that all subclasses will override to 
    attack and do damage to the opposing entity
"""

import abc

class Entity(abc.ABC):
    """Abstract class, represents an entity object."""
    def __init__(self, name, max_hp):
        """
        Assign the max_hp val to both _max_hp and _hp attributes
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, dmg):
        """
        The damage an entity takes. Subtract the dmg value from an entity's _hp.
        Do not let the hp go past 0, if negative, rest to 0
        """
        self._hp = self._hp - dmg

        # hp is negative, reset to 0
        if self.hp < 0:
            self._hp = 0

    def heal(self):
        """
        Restore the entity's hp to max_hp.
        """
        self._hp = self._max_hp

    def __str__(self):
        """
        Return the entity's name and hp in the format 'Name\nHP: hp/max_hp'.
        """
        return f"{self.name}\nHP: {self.hp}/{self._max_hp}"

    @abc.abstractmethod
    def attack(self, entity):
        pass

