
def print_header(text):
    """ Print header 
    """
    header_text = ''
    TEXT = f' {text} \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_principal():
    while True:
        try:
            principal = input('Enter the principal: ')
            return float(principal)
        except ValueError:
            print('A valid input required')


def get_rate_of_interest():
    while True:
        try:
            rate_of_interest = input('Enter the rate of interest: ')
            return float(rate_of_interest)
        except ValueError:
            print('A valid input required')

def get_number_of_years():
    while True:
        try:
            number_of_years = input('Enter the number of years: ')
            return float(number_of_years)
        except ValueError:
            print('A valid input required')

def get_compound():
    while True:
        try:
            rate_of_interest = input('What is the number of time the interest is compounded each year? ')
            return float(rate_of_interest)
        except ValueError:
            print('A valid input required')


def calc_investment(principal, rate, years, compound):
    return round(principal * (1+((rate/100)/compound))**(compound*float(years)), 2)


def print_investment(years, interest, investment_value):
    print(f'After {years} at {interest}, the investment will\n be worth {investment_value}.')
