import re

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Password Strength Indicator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_password():

    while True:
        password = input('Enter password: ')
        if len(password) >=1:
            return password
        else:
            print('A valid input is required')

def password_validator(password):
    
    special_characters_regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if len(password) < 8 and password.isdigit():
        print(f'The password \'{password}\' is a very weak password')
    elif len(password) < 8 and password.isalpha():
        print(f'The password \'{password}\' is a weak password')
    elif len(password) >= 8 and (any(char.isdigit() for char in password) and special_characters_regex.search(password) is None):
        print(f'The password \'{password}\' is a strong password')
    elif len(password) >= 8 and special_characters_regex.search(password):
        print(f'The password \'{password}\' is a very strong password')

def prompt_get_strings():
    print('Enter two strings and I\'ll tell you if they\nare anagrams: ')


def get_first_string():

    while True:
        first_string = input('Enter the first string: ')
        
        if len(first_string) >=3:
            return first_string
        else:
            print('A valid input is required')


def get_second_string():

    while True:
        second_string = input('Enter the second string: ')
        
        if len(second_string) >=3:
            return second_string
        else:
            print('A valid input is required')


def is_anagram(first_string, second_string):

    return sorted(first_string) == sorted(second_string) 


def print_is_anagram(first_string, second_string):
    if(is_anagram(first_string, second_string)):
        print(f'{first_string} and {second_string} are anagrams.')

if __name__ == "__main__":
    
    print_header()
    prompt_get_strings()
    first_string = get_first_string()
    second_string = get_second_string()
    print_is_anagram(first_string, second_string)