import die

class Player:
    def __init__(self):
        """
        Construct and sort the list of three 'die' objects. Initialize points
        to zero.
        """
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._points = 0


    def get_points(self):
        """Return player points"""
        return self._points


    def roll_dice(self):
        """
        Call roll on each of the dice objects in the internal list and sort it.
        """
        for dice in self._dice:
            dice.roll()

        self._dice.sort()


    def has_pair(self):
        """
        returns true if two dice in the list have the same value (uses ==)
        increments points by 1
        """
        count = 0
        for i in range(len(self._dice)):
            for j in range(i +1, len(self._dice)):
                if self._dice[i] == self._dice[j]:
                    count += 1
            

        if count != 1:
            return False
        else:
            self._points += 1
            return True


    def has_three_of_a_kind(self):
        """
        Return True if all dice in the list have the same value. Increment 
        points by 3 if True.
        """

        if self._dice[0] == self._dice[1] == self._dice[2]:
            self._points += 3
            return True

        return False
    

    def has_series(self):
        """
        Return true if values of dice are in a sequence. Ex: 1, 2, 3 or 2, 3, 4
        or 4, 5, 6. Increment points by 2 if True.
        """
        for i in range(len(self._dice)):
            for j in range(i + 1, len(self._dice) + 1):
                if i != len(self._dice) + 1:
                    if self._dice[j] - self._dice[i] != 1:
                        return False

        self._points += 2
        return True


    def __str__(self):
        """Return a string in the format: 'D1=2,D2=4,D3=6'."""
        return f"D1: {self._dice[0]}, D2: {self._dice[1]}, D3: {self._dice[2]}"