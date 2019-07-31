import random
import string

password_characters = list()

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Password Generator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_minimum_length():
    while True:
        try:
            minimum_length = input('What\'s the minimum length? ')
            minimum_length = int(minimum_length)
            return minimum_length
        except ValueError:
            print('A valid input is required')

def get_number_of_special_chars():
    while True:
        try:
            number = input('How many special characters? ')
            number = int(number)
            return number
        except ValueError:
            print('A valid input is required')

def get_number_of_numbers():
    while True:
        try:
            number = input('How many numbers? ')
            number = int(number)
            return number
        except ValueError:
            print('A valid input is required')


def build_password(length, special, numbers):
    
    for i in range(special):
        password_characters.append(random.choice(string.punctuation))

    for i in range(numbers):
        password_characters.append(random.choice(string.digits))

    for i in range(length-len(password_characters)):
        password_characters.append(random.choice(string.ascii_letters))

    random.shuffle(password_characters)

if __name__ == "__main__":
    print_header()
    minimum_length = get_minimum_length()
    number_of_numbers = get_number_of_numbers()
    special_chars = get_number_of_special_chars()
    build_password(minimum_length, special_chars, number_of_numbers)
    print( 'Your password is\n'+''.join(password_characters))
