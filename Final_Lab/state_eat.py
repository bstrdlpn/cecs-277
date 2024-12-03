import puppy_state
import state_asleep
import state_play

class StateEat(puppy_state.PuppyState):
    def play(self, puppy):
        """
        Return the puppy to play state.

        :return: str; string describing action puppy takes during play
        """
        puppy.play(state_play.StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."
    
    def feed(self, puppy):
        """
        Feed the puppy.
        """
        if puppy._state == puppy.StateEat:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.feed(state_asleep.StateFeed())