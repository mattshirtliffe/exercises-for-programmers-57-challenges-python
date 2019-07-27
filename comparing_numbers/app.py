

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Comparing Numbers \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_first_number():

    while True:
        try:
            number = input(f'Enter the first number: ')
            return int(number)
        except ValueError:
            print('A valid number is required')


def get_second_number():

    while True:
        try:
            number = input(f'Enter the second number: ')
            return int(number)
        except ValueError:
            print('A valid number is required')


def get_third_number():

    while True:
        try:
            number = input(f'Enter the third number: ')
            return int(number)
        except ValueError:
            print('A valid number is required')

def get_largest_number(numbers):

    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number
    
    # return max(numbers)
    
    # numbers.sort()
    # return numbers[-1]



def print_largest_number(largest_number):
    print(f'The largest number is {largest_number}')


if __name__ == "__main__":
    print_header()
    numbers = []

    first_number = get_first_number()
    numbers.append(first_number)
    
    second_number = get_second_number()
    numbers.append(second_number)

    third_number = get_third_number()
    numbers.append(third_number)

    largest_number = get_largest_number(numbers)
    print_largest_number(largest_number)