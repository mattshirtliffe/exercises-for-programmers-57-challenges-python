

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Legal driving age \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_age():
    while True:
        try:
            age = input('What is your age? ')
            return int(age)
        except ValueError:
            print('a valid input required')


def print_driving_message(age, legal_driving_age=17):
    n = 'not ' if age < legal_driving_age else ''
    print(f'You are {n}old enough to legally drive.')

if __name__ == "__main__":
    print_header()
    age = get_age()
    print_driving_message(age)
