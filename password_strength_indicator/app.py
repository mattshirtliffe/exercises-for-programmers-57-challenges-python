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


if __name__ == "__main__":
    
    print_header()
    password = get_password()
    password_validator(password)