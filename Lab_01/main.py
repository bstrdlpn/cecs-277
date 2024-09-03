import check_input
import random

# Student
# 08/27/2024
# Guessing Game

def main():
    cpu_num = random.randint(1, 100)
    player_guess = 0
    # count starts at one to include the player's first guess
    count = 1

    # FOR TESTING ONLY
    #print(cpu_num)
    print(f"- Guessing Game -")
    print(f"I'm thinking of a number.")
    player_guess = check_input.get_int_range("Make a guess (1-100): ", 1, 100)
    
    '''
    Main gameplay loop
    Continuously requests player to take a guess, then increments the guess number
    'count' if the guess is incorrect. After player correctly guesses the number,
    loop is exited. Guesses outside the bounds are not incremented in count total.
    '''

    while player_guess != cpu_num:
        if player_guess < cpu_num:
            print(f"Too low! Guess again!")
            player_guess = check_input.get_int_range("Guess again (1-100): ", 1, 100)
            count += 1
        elif player_guess > cpu_num:
            print(f"Too high! Guess again!")
            player_guess = check_input.get_int_range("Guess again (1-100): ", 1, 100)
            count += 1
        
        print(f"Correct! You got it in {count} tries!")
main()
