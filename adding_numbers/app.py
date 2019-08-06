

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Adding Numbers \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_numbers():

    numbers = list()
    while len(numbers) != 5:
        try:
            number = input('Enter a number: ')
            number = int(number)
            numbers.append(number)
        except ValueError:
            print('A valid input is required')
    return numbers


def get_total(numbers):
    return sum(numbers)


def print_total(total):
    print(f'The total is {total}.')


if __name__ == "__main__":
    
    print_header()
    numbers = get_numbers()
    total = get_total(numbers)
    print_total(total)
