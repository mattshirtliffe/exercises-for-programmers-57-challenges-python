
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Calculate area of a rectangle room \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_length_of_the_room():

    while True:
        try:
            length_str = input('What is the length of the room in feet? ')
            length_of_room = int(length_str)
            return length_of_room
        except:
            print('A valid number is required')


def get_width_of_the_room():

    while True:
        try:
            width_str = input('What is the width of the room in feet? ')
            width_of_room = int(width_str)
            return width_of_room
        except:
            print('A valid number is required')


def print_entered_dimensions(length, width):
    print(f'You entered dimensions of {length} feet by {width} feet.')


def calculate_area_square_feet(length, width):
    return length * width

def calculate_area_square_meters(length, width):
    area_square_meters = (int(length) * int(width)) * 0.09290304
    area_square_meters = round(area_square_meters, 3)
    return area_square_meters

def print_area_message(square_feet, square_meters):
    print(f'The are is\n{square_feet} square feet\n{square_meters} square meters')