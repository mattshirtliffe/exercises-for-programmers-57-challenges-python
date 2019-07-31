import random

names = list()

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Picking a Winner \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_name():
    while True:
        employee_name = input('Enter a name: ')
        if len(employee_name) > 0:
            return employee_name
        else:
            print('A valid input is required')

def get_names():
    for i in range(6):
        name = get_name()
        names.append(name)

def pick_name():
    name = random.choice(names)
    return name


def print_winner(winner_name):
    print(f'The winner is... {winner_name}')


if __name__ == "__main__":
    print_header()
    get_names()
    winner_name = pick_name()
    print_winner(winner_name)