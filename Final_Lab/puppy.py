import puppy_state
import state_asleep

class Puppy(puppy_state.PuppyState):
    def __init__(self):
        """
        initializes the state to the asleep state, and then initializes the number of feeds and plays
        """
        self._state = state_asleep.StateAsleep

    #properties?

    def change_state(self, new_state):
        """
        updates the puppy’s state to the new state
        """
        self._state = new_state

    def throw_ball(self):
        """
        calls the play method for whichever state the puppy is in
        """
        play = self.play()
        return play

    def give_food(self):
        """
        calls the feed method for whichever state the puppy is in
        """
        feed = self.feed()
        return feed

    def inc_feeds(self):
        """
        increments the number of times the puppy has been fed in a row
        """
        pass

    def inc_plays(self):
        """
        increments the number of times the puppy has played in a row.
        """
        pass

    def reset(self):
        """
        reinitializes the feeds and plays attributes
        """
        pass