

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Counting Characters \n'
    LINE = '-' * len(TEXT)
    LINE += '\n'

    header_text += LINE
    header_text += TEXT
    header_text += LINE
    print(header_text)


def get_input():
    while True:
        input_str = input('What is the input string? ')
        input_str_length = len(input_str)
        if input_str_length > 0:
            return input_str
        print('A valid input required')


def print_message(input_str):
    print(f'{input_str} has {len(input_str)} characters.')


def run():
    print_header()
    input_str = get_input()
    print_message(input_str)


if __name__ == "__main__":
    run()