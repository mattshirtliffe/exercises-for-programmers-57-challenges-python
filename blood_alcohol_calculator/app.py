

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Blood alcohol calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_weight():
    while True:
        try:
            weight = input('What is your weight? ')
            return int(weight)
        except ValueError:
            print('a valid input required')


def get_gender():
    genders = ['m', 'f']
    while True:
        gender = input('What is you gender? ')
        if gender in genders:
            return gender
        
        print('A valid input is required')


def get_number_of_drinks():
    while True:
        try:
            weight = input('How many drinks? ')
            return int(weight)
        except ValueError:
            print('a valid input required')


def get_hours_since_drink():
    while True:
        try:
            weight = input('Number of hours since last drink? ')
            return int(weight)
        except ValueError:
            print('a valid input required')

def calculate_blood_alcohol(weight, gender, drinks, hours):
    genders = {'m': 0.73, 'f': 0.66}
    oz = 12
    abv = 5/100
    alcohol = oz*drinks*abv
    
    blood_alcohol = (alcohol * (5.14 / weight) * genders[gender]) - (0.015 * hours)
    return round(blood_alcohol, 2)

def print_bac(blood_alcohol):
    print(f'Your BAC is {blood_alcohol}')

def print_legal_bac(blood_alcohol):
    n = 'not ' if blood_alcohol >= 0.08 else ''
    print(f'It is {n}legal for you to drive')

if __name__ == "__main__":
    print_header()
    drinks = get_number_of_drinks()
    gender = get_gender()
    weight = get_weight()
    hours = get_hours_since_drink()
    bac = calculate_blood_alcohol(weight, gender, drinks, hours)
    print_bac(bac)
    print_legal_bac(bac)
