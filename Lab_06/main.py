import player
from check_input import get_yes_no


"""
Christina Hipolito, Long Nguyen
10/03/2024

Yahtzee:
Dice game that awards the user for a pair, three-of-a-kind
"""

def take_turn(player):
    """
    Roll the player's dice, display the dice, check for and display any win 
    types (pair, three-of-a-kind, series), and display the updated score.

    :param player: (object) player
    """
    # roll the player's dice
    player.roll_dice()

    # display the dice
    print(player)

    # win conditions
    win = [player.has_pair(), player.has_three_of_a_kind(), player.has_series()]
    
    # display win types
    if win[0]:
        print('You got a pair!')
    if win[1]:
        print('You got 3 of a kind!')
    if win[2]:
        print('You got a series of 3!')
    if True not in win:
        print('Aww. Too Bad.')
    # display the updated score:
    print(f"Score {player.get_points()}")


def main():
    user = player.Player()

    while True:
        print("-Yahtzee-")
        print()
        take_turn(user)
        choice = get_yes_no("Play again? ")
        print()
        if not choice:
            break

    print("Game Over.") 
    print(f"Final Score = {user.get_points()}")

main()