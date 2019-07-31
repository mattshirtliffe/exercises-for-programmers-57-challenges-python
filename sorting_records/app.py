import random
import string

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Sorting records \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


users = [
    {'first_name':'John', 'last_name':'Johnson', 'position':'Manager', 'separation_date':'2016-12-31'},
    {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'},
    {'first_name':'Michaela', 'last_name':'Michaelson', 'position':'District Manage', 'separation_date':'2015-12-19'},
    {'first_name':'Jake', 'last_name':'Jacobson', 'position':'Programmer', 'separation_date':''},
    {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''},
    {'first_name':'Sally', 'last_name':'Weber', 'position':'Web Developer', 'separation_date':'2015-12-18'}
]


def print_headings():
    """ Print header 
    """
    # header_text = ''
    
    headings = ['First Name', 'Last Name', 'Position', 'Separation date']
    for index, heading in enumerate(headings):
        if index == len(headings)-1:
            print(heading)
        else:    
            print(heading, end='|')
    print()


def print_users():
    for user in users:
        for key, value in user.items():
            end_spaces = len(key) * ' '
            value += end_spaces[len(value):]
            print(value, end='|')
        print('\n')


def sort_users():
    return sorted(users, key=lambda k: k['last_name'])

if __name__ == "__main__":
    print_header()
    print_headings()
    users = sort_users()
    print_users()