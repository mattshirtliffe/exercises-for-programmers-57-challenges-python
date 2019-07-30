

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Karvonen heart rate \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_headings():
    """ Print header 
    """
    header_text = ''
    a = 'Intensity   '
    b = ' Rate '
    top = f'{a}|{b}\n'
    bottom = len(a)*'-'+'|'+len(b)*'-'

    TEXT = ' Karvonen heart rate \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += top
    header_text += bottom
    print(header_text)


def get_resting_heart_rate():
    while True:
        try:
            resting_heart_rate = input('Resting pulse: ')
            resting_heart_rate = int(resting_heart_rate)
            return resting_heart_rate
        except ValueError:
            print('A valid input is required')


def get_age():
    while True:
        try:
            age = input('Age: ')
            age = int(age)
            return age
        except ValueError:
            print('A valid input is required')

def calculate_target_heart_rate(intensity, age, resting_heart_rate):
    intensity = intensity /100
    target_heart_rate = (((220 - age) - resting_heart_rate) * intensity) + resting_heart_rate
    return round(target_heart_rate)

def print_output(age, resting_heart_rate):

    for intensity in range(55, 96):
        print(f'{intensity}%         | {calculate_target_heart_rate(intensity, age, resting_heart_rate)} bpm')


if __name__ == "__main__":
    print_header()
    resting_heart_rate = get_resting_heart_rate()
    age = get_age()
    print_headings()
    print_output(age, resting_heart_rate)