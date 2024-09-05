
import check_input
import random

"""
Long Nguyen, Christina Hipolito

==Rock, Paper Scissors:==
A program that allows a player to play "Rock, Paper, Scissors" against the 
computer. This will track the number of wins by the computer or player.
"""

def weapon_menu():
    """"
    Player selects one of 4 options:
        R = Rock
        P = Paper
        S = Scissors
        or
        B = Go Back
    
        If R, P, or S is selected, the choice is returned, otherwise, B will 
        return the user to the main menu
        """
    valid_flag = False

    while not valid_flag:
        player = input("Pick a weapon (R = rock, P = paper, S = scissors, B =  Go Back): ").upper()
        if player == "B":
            valid_flag = True
            return player
        elif player == "R" or player == "P" or player == "S":
            valid_flag = True
            return player
        else: 
            print("Invalid Input. PLease Select 'R', 'P', 'S', or 'B'.")


def comp_weapon():
    """"Randomly chooses the computer's throw and returns the choice."""

    # Constant containing weapons choices
    WEAPON_CHOICE = ('R', 'P', 'S')
    # R = Rock
    # P = Paper
    # S = Scissors

    comp_selection = ''
    
    # Randomly selects a weapon from the `_WEAPON_CHOICE` table
    comp_selection = random.choice(WEAPON_CHOICE)
    
    return comp_selection

def find_winner(player, comp):
    """
    Parameters:     player - player weapon
                    comp -   computer weapon

    Returns:        Point awarding a win to the player or comp

        find_winner(player, comp) - Passes in the two weapons (R, P, or S),
        displays the throws, compares the two weapons and displays the result 
        and returns who is the winner of that round (0=Tie, 1=Player, 2=Computer).
        a. Rock crushes Scissors
        b. Scissors cuts Paper
        c. Paper covers Rock
    """

    if player == comp:
        if player == 'R':
            print('You chose Rock')
            print('Computer chose Rock')
            print('Tie')
            return 0
        elif player == 'P':
            print('You chose Paper')
            print('Computer chose Paper')
            print('Tie')
            return 0
        else: 
            print('You chose Scissors')
            print('You chose Scissors') 
            print('Tie')
            return 0
    elif player == 'R' and comp == 'S':
        print('You chose Rock')
        print('Computer chose Scissors')
        print('Player Wins')
        return 1
    elif player == 'S' and comp == 'P':
        print('You chose Scissors')
        print('Computer chose Paper')
        print('Player Wins')
        return 1
    elif player == 'P' and comp == 'R':
        print('You chose Paper')
        print('Computer chose Rock')
        print('Player Wins')
        return 1
    elif player == 'R' and comp == 'P':
        print('You chose Rock')
        print('Computer chose Paper')
        print('Computer Wins')
        return 2
    elif player == 'S' and comp == 'R':
        print('You chose Scissors')
        print('Computer chose Rock')
        print('Computer Wins')
        return 2
    elif player == 'P' and comp == 'S':
        print('You chose Paper')
        print('Computer chose Scissors')
        print('Computer Wins')
        return 2
    else:
        print('Invalid input, must select "R", "P", "S", or "B"')
        return

def display_scores(player, comp):
    """"
    Displays the scores.

    Parameters:     player -    player score
                    computer -  computer score
    """
    print("Final Score: ")
    print(f"Player = {player}")
    print(f"Computer = {comp}")

def main():
    player_score = 0
    comp_score = 0

    while True:
        selection = check_input.get_int_range('RPS Menu:\n1. Play Game\n2. Show Score\n3. Quit\n', 1, 3)
        if selection == 1:
            # create variables that save player and comp choice
            player = weapon_menu()
            if player == 'B':
                pass
            else:
                comp = comp_weapon()
                win_state = find_winner(player, comp)
                if win_state == 1:
                    player_score += 1
                elif win_state == 2:
                    comp_score += 1
        elif selection == 2:
            display_scores(player_score, comp_score)
        elif selection == 3:
            display_scores(player_score, comp_score)
            break

main()

