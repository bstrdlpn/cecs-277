import puppy_state
import state_asleep
import state_play

class StateEat(puppy_state.PuppyState):
    def play(self, puppy):
        """
        Return the puppy to play state.

        :return: str; string describing action puppy takes during play
        """
        puppy.change_state(state_play.StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."
    
    def feed(self, puppy):
        """
        Feed the puppy. If puppy has been fed consecutively three times, change 
        the _state attribute to 'StateAsleep' and return string desc, else return 
        string desc.

        :return: str; string describing action of what puppy does.
        """
        puppy.inc_feeds()
        if puppy.feeds % 3 == 0:
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy ate so much it fell asleep!"
        else:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
