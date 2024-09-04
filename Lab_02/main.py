import check_input
import random

"""
    Student 1, Student 2

    Submit by 5th September 11:59 p.m.
    Only one person from each group needs to submit the assignment.

    weapon_menu() - Asks the user to input their choice: (R)ock, (P)aper, 
    (S)cissors, or (B)ack. Checks user input for validity and then returns the 
    inputted value.
"""

def weapon_menu():
    """"
    Player selects one of 4 options
        R = Rock
        P = Paper
        S = Scissors
        or
        B = Go Back
    
        If R, P, or S is selected, the choice is returned, otherwise, B will 
        return to the main menu
        """
    
    while True:
        player = input("Pick a weapon (R = rock, P = paper, S = scissors, B =  Go Back): ")
        if player.upper() == "B":
            return 'B'
        elif player.upper() == "R" or "P" or "S":
            return player
        else:
            print('Invalid input, must select "R", "P", "S", or "B"')

def comp_weapon():
    """"Randomly chooses the computer's throw and returns an "R", "P" or "S". """

    # Constant containing weapons choices
    WEAPON_CHOICE = ['R', 'P', 'S']
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
    else:
        print('You chose Paper')
        print('Computer chose Scissors')
        print('Computer Wins')
        return 2


def display_scores(player, comp):
    """"Displays the scores."""
    print("Final Score: ")
    print(f"Player = {player}")
    print(f"Computer = {comp}")


def main():
    player_score = 0
    comp_score = 0
    
    while True:
        selection = check_input.get_int('RPS Menu:\n1. Play Game\n2. Show Score\n3. Quit\n')
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
            break


main()