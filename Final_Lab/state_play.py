import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
    def feed(self, puppy):
        """
        Attempt to feed the puppy.

        :return: str; description of feed attempt failure.
        """
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """
        Play with the puppy, if puppy has been played with consecutively 3 times, 
        change state to 'StateAsleep' and return string of what puppy does, else 
        return string desc of what puppy does.

        :return: str; description of what puppy does
        """
        puppy.inc_plays()
        if puppy.plays % 3 == 0:
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy played so much it fell asleep!"
        else:
            return "You throw the ball again and the puppy excitedly chases it."