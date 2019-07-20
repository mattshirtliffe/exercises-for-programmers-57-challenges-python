
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
    length = input('What is the length of your ceiling? ')


def get_ceiling_width():
    width = input('What is the width of your ceiling? ')