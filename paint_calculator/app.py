
import math

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Paint Calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_ceiling_length():
    while True:
        try:
            length = input('What is the length of your ceiling? ')
            return int(length)
        except ValueError:
            print('A valid number is required')


def get_ceiling_width():
    while True:
        try:
            width = input('What is the width of your ceiling? ')
            return int(width)
        except ValueError:
            print('A valid number is required')


def calculate_area(width, length):
    return width * length


def calculate_gallons_needed(area):
    return math.ceil(area / 350)


def print_gallons_needed(gallons, area):
    print(f'You will need to purchase {gallons} gallons of\n paint to cover {area} square feet.')
