import check_input
import random
from dictionary import words

def display_gallows(num_incorrect):
    """
    Displays the state of the hangman on the gallows.

    Parameter:
        num_incorrect : number of incorrect guesses

    Returns:
        Image of hangman on gallows as related to num-incorrect
    """
    print(f'Incorrect Selections: {num_incorrect}')
    if num_incorrect == 0:
        print('========')
        print('||/    |')
        print('||')
        print('||')
        print('||')
        print('||')
    elif num_incorrect == 1:
        print('========')
        print('||/    |')
        print('||     o')
        print('||')
        print('||')
        print('||')
    elif num_incorrect == 2:
        print('========')
        print('||/    |')
        print('||     o')
        print('||     |')
        print('||')
        print('||')
    elif num_incorrect == 3:
        print('========')
        print('||/    |')
        print('||     o')
        print('||     |')
        print('||    /')
        print('||')
    elif num_incorrect == 4: #choices 4-5 need a double slash to terminate string literal
        print('========')
        print('||/    |')
        print('||     o')
        print('||     |')
        print('||    / \\') # for example, here: it will print 1 \
        print('||')
    elif num_incorrect == 5:
        print('========')
        print('||/    |')
        print('||    \\o')
        print('||     |')
        print('||    / \\')
        print('||')
    elif num_incorrect == 6:
        print('========')
        print('||/    |')
        print('||    \\o/')
        print('||     |')
        print('||    / \\')
        print('||')


def display_letters(letters):
    """
    given a list of letters, display each of the letters separated by spaces. Use 
    this function when displaying the correct letters list, the incorrect letters 
    list, and the letters that are remaining list.
    """
    pass


def get_letters_remaining(incorrect, correct):
    """
    given the list of incorrect guesses and the list of correct guesses, return 
    the list of remaining letters in the alphabet to choose from (do not display 
    the list from within the function).

    Parameters:
        incorrect : list of incorrect guesses
        correct :   list of correct guesses

    Returns:
        the list of remaining letters in the alphabet to choose from
    """
    
    pass


def main():
    """
    Create a loop that repeats until the user quits. Choose a random word from the
    words list. Create additional lists, one for incorrect guesses (starts empty),
    other for correct guesses, starts with 5 letters.

    Create a loop that will repeat until the user guesses all 5 letters in the 
    word, or until the user has made 6 incorrect guesses.
    """
    # guess lists 
    incorrect_guesses = []
    correct_guesses = ['_', '_', '_', '_', '_']

    #counters
    num_correct_guesses = 0
    num_incorrect_guesses = 0

    while True:
        # Randomly selects a word from the dictionary
        secret_word = random.choice(words)
        while True:
            choice = input('Enter a letter: ').upper()
            if choice.isalpha():
                break
            else:
                print('Please enter a letter A through Z only.')
        # if the player's choice exists in the secret word
        if choice in secret_word:
            print('Correct!')
            # iterate through string, and update correct guesses list with the
            # correct indexed character
            for index, char in enumerate(secret_word):
                if choice == char:
                    correct_guesses[index] = choice
            num_correct_guesses += 1
            get_letters_remaining(incorrect_guesses, 
                                  correct_guesses)
            if '-' not in correct_guesses:
                print('You win!')
                choice = check_input.get_yes_no('Play again (Y/N)? ')
                if not choice:
                    break
        else:
            print('Incorrect!')
            incorrect_guesses.append(choice)
            num_incorrect_guesses += 1




    """
    is choice IN secret_word
        if YES:
            GET index of choice IN secret_word
            correct[index] = choice
            correct += 1
            display_gallows(incorrect)
            get_letters_remaining(incorrect, correct)
            display_letters(letters)
        if NO:
            incorrect_guesses.append(choice)
            incorrect += 1
            display_gallows(incorrect)
            get_letters_remaining(incorrect, correct)
            display_letters(letters
    """
    
    #TODO 
    # loop that repeats until user quits - breaks on y or n
    
main()