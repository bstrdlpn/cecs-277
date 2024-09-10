import check_input
import random
from dictionary import words

def display_gallows(num_incorrect):
    """
    Given the number of incorrect guesses the user has made, display the state 
    of the hangman on the gallows (ex. zero incorrect guesses should show an empty 
    gallows, 6 incorrect guesses should show the complete hanged man).
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
        print('||    \o')
        print('||     |')
        print('||    / \\')
        print('||')
    elif num_incorrect == 6:
        print('========')
        print('||/    |')
        print('||    \o/')
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
    incorrect_guesses = []
    correct_guesses = []
    secret_word = words.random.choice()

    num_correct_guesses = 0
    num_incorrect_guesses = 0

    while True:
    
main()