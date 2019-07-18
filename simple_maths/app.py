def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Simple Maths \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_first_number():

    while True:
        try:
            first_number_str = input('What is the first number? ')
            first_number = int(first_number_str)
            return first_number
        except:
            print('A valid number is required')


def get_second_number():

    while True:
        try:
            second_number_str = input('What is the second number? ')
            second_number = int(second_number_str)
            return second_number
        except:
            print('A valid number is required')


def add_numbers(first_number, second_number):
    return first_number + second_number


def print_add_numbers_result(first_number, second_number, result):
    print(f'{first_number} + {second_number} = {result}')


def subtract_numbers(first_number, second_number):
    return first_number - second_number


def print_subtract_numbers_result(first_number, second_number, result):
    print(f'{first_number} - {second_number} = {result}')


def multiply_numbers(first_number, second_number):
    return first_number * second_number


def print_multiply_numbers_result(first_number, second_number, result):
    print(f'{first_number} * {second_number} = {result}')


def divide_numbers(first_number, second_number):
    return first_number / second_number


def print_divide_numbers_result(first_number, second_number, result):
    print(f'{first_number} / {second_number} = {result}')

if __name__ == "__main__":
    print_header()
    first_number = get_first_number()
    second_number = get_second_number()

    res = add_numbers(first_number, second_number)
    print_add_numbers_result(first_number, second_number, res)

    res = subtract_numbers(first_number, second_number)
    print_subtract_numbers_result(first_number, second_number, res)

    res = multiply_numbers(first_number, second_number)
    print_multiply_numbers_result(first_number, second_number, res)

    res = divide_numbers(first_number, second_number)
    print_divide_numbers_result(first_number, second_number, res)