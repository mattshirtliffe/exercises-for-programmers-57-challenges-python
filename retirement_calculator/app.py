from datetime import datetime

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Retirement Calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_current_age():
    while True:
        try:
            age_str = input('What is your current age? ')
            age = int(age_str)
            return age
        except ValueError:
            print('A valid number is required')


def get_retirement_age():

    while True:
        try:
            retirement_age_str = input('At what age would you like to retire? ')
            retirement_age = int(retirement_age_str)
            return retirement_age
        except ValueError:
            print('A valid number is required')


def get_now():
    return datetime.now()

def get_current_year():
    year = get_now().year
    return year

def calc_years_till_retirement(current_age, retirement_age):
    return retirement_age - current_age

def calc_retirement_year(year, years_till_retirement):
    return year + years_till_retirement