import random

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Guess the Number Game \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_play():
    print('Let\'s play Guess the number.')


def get_difficulty():

    while True:
        try:
            difficulty = input('Pick a difficulty level (1, 2 or 3): ')
            difficulty = int(difficulty)
            if difficulty > 0 or difficulty <=3:
                return difficulty
            else:
                print('A valid input is required')    
        except ValueError:
            print('A valid input is required')


def get_max_number_from_difficulty(difficulty):
    max_number = (10 ** difficulty)
    return max_number


def create_number(difficulty):
    max_number = get_max_number_from_difficulty(difficulty)
    return random.randint(1,max_number)


def get_guessed_number(difficulty):
    
    max_number = get_max_number_from_difficulty(difficulty)
    while True:
        try:
            guessed_number = input('I have my number. What\'s your guess? ')
            guessed_number = int(guessed_number)
            if guessed_number >= 1 and guessed_number <= max_number:
                return guessed_number
            else:
                print('A valid input is required')    
        except ValueError:
            print('A valid input is required')


def get_guessed_again(difficulty, previous_guessed_number, number):
    
    max_number = (10 ** difficulty)
    while True:
        try:
            if previous_guessed_number > number:
                guessed_number = input('Too high. Guess again: ')
            else:
                guessed_number = input('Too low. Guess again: ')
            
            guessed_number = int(guessed_number)
            if guessed_number >= 1 and guessed_number <= max_number:
                return guessed_number
            else:
                print('A valid input is required')    
        except ValueError:
            print('A valid input is required')


def play_again():

    while True:
        answer = input('play again? ')
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            play()
        elif answer == 'n' or answer == 'no':
            print('Goodbye!')
            exit()
        else:
            print('A valid input is required')
        

def print_number_of_guesses(number_of_guesses):
    print(f'You got it in {number_of_guesses} guesses!') 


def play():
    difficulty = get_difficulty()
    number_of_guesses = 0
    number = create_number(difficulty)
    guessed = get_guessed_number(difficulty)
    number_of_guesses +=1
    while guessed != number:
        guessed = get_guessed_again(difficulty, guessed, number)
        number_of_guesses +=1
    
    print_number_of_guesses(number_of_guesses)  
    play_again()

if __name__ == "__main__":
    play()