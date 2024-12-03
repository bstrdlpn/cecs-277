import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):
    def feed(self, puppy):
        puppy.change_state(state_eat.StateEat())
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        return "The puppy is alseep. It doesn't want to play right now."