

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Pizza Party \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_number_of_people():

    while True:
        try:
            number_of_people_str = input('How many people? ')
            number_of_people = int(number_of_people_str)
            return number_of_people
        except ValueError:
            print('A valid number is required')


def get_number_of_pizza():

    while True:
        try:
            number_of_pizza = input('How many pizzas fo you have? ')
            return int(number_of_pizza)
        except ValueError:
            print('A valid number is required')


def print_people_and_pizzas(people, pizza):
    print(f'{people} people with {pizza} pizzas')


def get_number_of_slices(number_of_pizza, average_slices=8):
    return number_of_pizza * average_slices


def get_slices_per_person(slices, people):
    return slices // people


def get_leftover_slices(slices, people):
    return slices % people


def print_person_gets(slices):
    s = 's' if slices != 1 else ''
    print(f'Each peron gets {slices} slice{s} of pizza')


def print_leftover(slices):
    s = 's' if slices != 1 else ''
    there_x = 'are' if slices != 1 else 'is'
    print(f'There {there_x} {slices} leftover slice{s}')