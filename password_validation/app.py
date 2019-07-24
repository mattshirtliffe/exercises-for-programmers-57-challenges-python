

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Password Validation \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_password():
    while True:
        password = input('What is the password? ')
        if len(password) >= 5:
            return password


def get_is_password_valid(password, valid_password = 'abc$123'):
    return password == valid_password


def print_message(password):

    # if get_is_password_valid(password):
    #     print('Welcome!')
    # else:
    #     print('I dont\'t know you')
    
    m = 'Welcome!' if get_is_password_valid(password) else 'I dont\'t know you'
    print(m)

    
if __name__ == "__main__":
    print_header()
    password = get_password()
    print_message(password)