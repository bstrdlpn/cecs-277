import abc

class PuppyState(abc.ABC):
    @abc.abstractmethod
    def play(self, puppy):
        pass

    @abc.abstractmethod
    def feed(self, puppy):
        pass