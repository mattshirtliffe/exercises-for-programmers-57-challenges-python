import random
import string

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Filtering Values \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_numbers():
    number_string = input('Enter a list of numbers, separated by spaces: ')
    number_string_list = number_string.split()
    return list(map(int, number_string_list))


def get_evens(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def print_evens(even_numbers):
    n = ' '.join(str(e) for e in even_numbers)
    print(f'The even numbers are {n}.')


if __name__ == "__main__":
    print_header()
    numbers = get_numbers()
    even_numbers = get_evens(numbers)
    print_evens(even_numbers)
   
