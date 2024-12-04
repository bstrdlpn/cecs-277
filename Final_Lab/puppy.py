import state_asleep

class Puppy:
    """
    Represents the user's puppy. The user can play or feed the puppo.
    """
    def __init__(self):
        """
        Initialize the state to the asleep state, and then initialize the number 
        of feeds and plays
        """
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0

    #properties? 
    # i think they are just to access the '_feeds' and '_plays' attributes
    @property 
    def feeds(self):
        return self._feeds
        
    @property
    def plays(self):
        return self._plays

    def change_state(self, new_state):
        """
        Update the puppy's state to the new state.
        """
        self._state = new_state

    def throw_ball(self):
        """
        Call the play method for whichever state the puppy is in.
        """
        return self._state.play(self)

    def give_food(self):
        """
        Call the feed method for whichever state the puppy is in.
        """
        return self._state.feed(self)

    def inc_feeds(self):
        """
        Increment the number of times the puppy has been fed in a row.
        """
        self._feeds += 1

    def inc_plays(self):
        """
        Increments the number of times the puppy has played in a row.
        """
        self._plays += 1

    def reset(self):
        """
        Reinitialize the feeds and plays attributes.
        """
        self._feeds = 0
        self._plays = 0