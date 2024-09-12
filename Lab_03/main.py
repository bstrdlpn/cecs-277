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
    if '_' in letters or len(letters) == 5:
        return print(' '.join(map(str, letters)))
    elif len(letters) >= 15:
        letters_remaining = ' '.join(map(str, letters))
        return print(f"Letters Remaining: {letters_remaining}")
    else:
        incorrect_letters = ' '.join(map(str, letters))
        return print(f"Incorrect Letters: {incorrect_letters}")

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
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # loops which remove the elements contained in incorrect and correct from 
    # alphabet list, which contains the remaining letters
    for ele in incorrect:
        if ele in alphabet:
            alphabet.remove(ele)

    for ele in correct:
        if ele in alphabet:
            alphabet.remove(ele)

    return alphabet


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

    # Randomly selects a word from the dictionary
    secret_word = random.choice(words)
    while True:   
        while True:
            print(secret_word)
            choice = input('Enter a letter: ').upper()
            remaining_letters = get_letters_remaining(correct_guesses, incorrect_guesses)
            if (choice.isalpha()and len(choice) == 1) and choice in remaining_letters:
                break
            elif (choice.isalpha() == False) and (len(choice) > 1):
                print('Please select a different letter that has not been guessed.')
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
            remaining_letters = get_letters_remaining(correct_guesses, 
                                                      incorrect_guesses)
            display_letters(incorrect_guesses)
            display_gallows(num_incorrect_guesses)
            display_letters(correct_guesses)
            display_letters(remaining_letters)
            if '_' not in correct_guesses:
                print('You win!')
                choice = check_input.get_yes_no('Play again (Y/N)? ')
                if not choice:
                    break
                else:
                    num_correct_guesses = 0
                    num_incorrect_guesses = 0
                    incorrect_guesses = []
                    correct_guesses = ['_', '_', '_', '_', '_']
                    secret_word = random.choice(words)

        else:
            print('Incorrect!')
            """
            Append choice to incorrect_guess
            Increment num_incorrect_guesses
            Get remaining_letters
            Display incorrect selections
            Display Gallows
            Display Correct Letters Array
            Display Letters Rmaining
            """
            incorrect_guesses.append(choice)
            num_incorrect_guesses += 1
            remaining_letters = get_letters_remaining(correct_guesses, 
                                                      incorrect_guesses)
            display_letters(incorrect_guesses)
            display_gallows(num_incorrect_guesses)
            display_letters(correct_guesses)
            display_letters(remaining_letters)
            if num_incorrect_guesses >=6:
                print('You Lose!')
                choice = check_input.get_yes_no('Play again? (Y/N)? ')
                if not choice:
                    break
                else:
                    # reset the game counters and lists
                    num_correct_guesses = 0
                    num_incorrect_guesses = 0
                    incorrect_guesses = []
                    correct_guesses = ['_', '_', '_', '_', '_']
                    secret_word = random.choice(words)

main()