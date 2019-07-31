import random

employees = [
    'John Smith',
    'Jakie Jackson',
    'Chris Jones',
    'Amanda Cullen',
    'Jeremy Goodwin',
]

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Employee list removal \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_employees():
    number_of_employees = len(employees)
    print(f'There are {number_of_employees} employees:')
    for employee in employees:
        print(employee) 


def get_employee_name():
    while True:
        employee_name = input('Enter an employee name to remove: ')
        if len(employee_name) > 0:
            return employee_name
        else:
            print('A valid input is required')


def remove_employee(employee_name):
    if employee_name in employees:
        employees.remove(employee_name)


def print_response():
    responses = ['Yes', 'No', 'Maybe', 'Ask again later.']
    response = random.choice(responses)
    print(response)


if __name__ == "__main__":
    print_header()
    print_employees()
    employee_name = get_employee_name()
    remove_employee(employee_name)
    print_employees()