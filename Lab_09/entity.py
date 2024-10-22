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

    def __str__(self):
        """
        Return the entity's name and hp in the format "Name: hp/max_hp".
        """
        return f"Name: {self.hp}/{self._max_hp}"

    @abc.abstractmethod
    def basic_attack(self):
        pass

    @abc.abstractmethod
    def special_attack(self):
        pass
