import statistics

numbers = list()

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Computing Statistics \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_number():
    while True:
        try:
            number = input('Enter a number: ')
            number = int(number)
            return number
        except ValueError:
            return number

def get_numbers():
    while True:
        number = get_number()
        if number == 'done':
            break
        else:
            numbers.append(number)

def print_numbers():
    base_text = 'Numbers: '
    for index, number in enumerate(numbers):
        if index != len(numbers)-1:
            base_text += f'{number}, '
        else:
            base_text += f'{number}'
            
    print(base_text)

def print_average():
    average = statistics.mean(numbers)
    print(f'The average is {average}')

def print_minimum():
    minimum = min(numbers)
    print(f'The minimum is {minimum}')

def print_maximum():
    maximum = max(numbers)
    print(f'The maximum is {maximum}')

def print_standard_deviation():
    standard_deviation = statistics.stdev(numbers)
    standard_deviation = round(standard_deviation, 2)
    print(f'The standard deviation is {standard_deviation}.')

if __name__ == "__main__":
    print_header()
    get_numbers()
    print_numbers()
    print_average()
    print_minimum()
    print_maximum()
    print_standard_deviation()
