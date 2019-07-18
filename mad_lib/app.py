

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Mad Libs \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)