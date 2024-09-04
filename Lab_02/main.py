import check_input
import random

"""

    Use the random module to randomly choose the computer's weapon.
    Please stick to the functions and parameters mentioned in the assignment 
    description; don't add anything extra.
    Submit by 5th September 11:59 p.m.
    Only one person from each group needs to submit the assignment.

    weapon_menu() - Asks the user to input their choice: (R)ock, (P)aper, (S)cissors,
    or (B)ack. Checks user input for validity and then returns the inputted value.
    2. comp_weapon() - Randomly chooses the computer's throw and returns an “R”,
    “P”, or “S”.


    
    display_scores(player, comp) - Displays the scores.

"""

def weapon_menu():
    """"
    Player selects one of 4 options
        R = Rock
        P = Paper
        S = Scissors
        or
        B = Go Back
    
        If R, P, or S is selected, the choice is returned, otherwise, B will return
        to the main menu
        """
    
    while True:
        player = input("Pick a weapon (R = rock, P = paper, S = scissors, B =  Go Back): ")
        if player == "B":
            break
        elif player == "R" or player == "P" or player == "S":
            return player

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
        displays the throws, compares the two weapons and displays the result and returns
        who is the winner of that round (0=Tie, 1=Player, 2=Computer).
        a. Rock crushes Scissors
        b. Scissors cuts Paper
        c. Paper covers Rock
    """
    if player == comp:
        if player == 'R':
            print('You chose Rock')
            print('Computer chose Rock')
            print('Tie')
        elif player == 'P':
            print('You chose Paper')
            print('Computer chose Paper')
            print('Tie')
        else: 
            print('You chose Scissors')
            print('You chose Scissors') 
            print('Tie')       
    elif player == 'R' and comp == 'S':
        print('You chose Rock')
        print('Computer chose Scissors')
        print('Player Wins')
        _PLAYER_SCORE += 1
    elif player == 'S' and comp == 'P':
        print('You chose Scissors')
        print('Computer chose Paper')
        print('Player Wins')
        _PLAYER_SCORE += 1
    elif player == 'P' and comp == 'R':
        print('You chose Paper')
        print('Computer chose Rock')
        print('Player Wins')
        _PLAYER_SCORE += 1
    elif player == 'R' and comp == 'P':
        print('You chose Rock')
        print('Computer chose Paper')
        print('Computer Wins')
        _COMP_SCORE += 1
    elif player == 'S' and comp == 'R':
        print('You chose Scissors')
        print('Computer chose Rock')
        print('Computer Wins')
        _COMP_SCORE += 1
    else:
        print('You chose Paper')
        print('Computer chose Scissors')
        print('Computer Wins')
        _COMP_SCORE += 1

    return

def display_scores(player, comp):
    """"Displays the player scores."""
    # What is player, comp parameter?
    return f"Final Score:\nPlayer = {player}\nComputer -= {comp}"

def main_menu():
    selection = int(input("RPS Menu:\n1. Play Game\n2. Show Score\n3. Quit\n"))
    if selection == 1:
        weapon_menu()
    elif selection == 2:
        display_scores()
    elif selection == 3:
        exit()
    

def main():
    #TODO - while loop that continuously asks to play the game, unless quit
    # we can use the check_input module to check input for main menu
    
    while True:
        selection = check_input.get_int('RPS Menu:\n1. Play Game\n2. Show Score\n3. Quit\n')
        if selection == 1:
            # create variables that save player and comp choice
            player = weapon_menu()
            comp = comp_weapon()


            
    print(comp)
main()