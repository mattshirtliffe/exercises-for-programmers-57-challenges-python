

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