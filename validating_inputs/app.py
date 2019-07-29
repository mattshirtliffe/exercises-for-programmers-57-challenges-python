import re

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Validating Inputs \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_first_name():

    while True:
        first_name = input('Enter your first name: ')
        if len(first_name) >=2:
            return first_name
        else:
            print('A valid input is required')


def get_last_name():

    while True:
        last_name = input('Enter your last name: ')
        if len(last_name) >=2:
            return last_name
        else:
            print('A valid input is required')

def get_employee_id():
    regex = '^[A-Z]{2}-[0-9]{3,4}'
    while True:
        employee_id = input('Enter your employee id: ')
        if re.match(regex, employee_id):
            return employee_id
        else:
            print('A valid input is required')

def get_zip_code():
    regex = '^[A-Z]{5}'
    while True:
        zip_code = input('Enter your zip code: ')
        if re.match(regex, zip_code):
            return zip_code
        else:
            print('A valid input is required')


if __name__ == "__main__":
    
    print_header()
    first_name = get_first_name()
    last_name = get_last_name()
    zip_code = get_zip_code()
    employee_id = get_employee_id()
    if all([first_name, last_name, zip_code, employee_id]):
        print('There were no errors found')
