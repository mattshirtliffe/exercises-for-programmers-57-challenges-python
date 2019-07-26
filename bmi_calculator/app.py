

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' BMI Calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_height():

    while True:
        height = input(f'Enter your height in feet and inches: ')
        if len(height) >= 1:
            return height
        else:
            print('A valid input is required')


def get_weight():

    while True:
        try:
            weight = input(f'Enter your weight in pounds: ')
            return float(weight)
        except ValueError:
            print('A valid input is required')


def convert_height_to_inches(height):
    feet, inches = height.split('.')
    return ((float(feet) * 12) + float(inches))


def calculate_bmi(weight, height):

    bmi = (weight/(height**2)*703)
    return round(bmi, 2)


def print_bmi(bmi):
    print(f'Your BMI is {bmi}')


def print_bmi_status(bmi):
    min_bmi = 18.5
    max_max = 25
    if bmi >= min_bmi and bmi <= max_max:
        print('You are within the ideal weight range.')
    else:
        print('You are overweight. You should see your doctor.')


if __name__ == "__main__":
    print_header()
    height = get_height()
    weight = get_weight()
    inches = convert_height_to_inches(height)
    bmi = calculate_bmi(weight, inches)
    print_bmi(bmi)
    print_bmi_status(bmi)