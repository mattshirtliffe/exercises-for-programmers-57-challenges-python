

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Handling bad inputs \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_rate_of_return():
    while True:
        try:
            rate_of_return = input('What is the rate of return? ')
            rate_of_return = int(rate_of_return)
            if rate_of_return > 0:
                return rate_of_return
        except ValueError:
            print('Sorry. That\'s not a valid input.')


def calculate_years(rate_of_return):
    return 72 / rate_of_return


def print_years(years):
    print(f'It will take {years} to double your initial investment.')


if __name__ == "__main__":
    
    print_header()
    rate_of_return = get_rate_of_return()
    years = calculate_years(rate_of_return)
    print_years(years)
