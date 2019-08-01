import random
import string


def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Name sorter \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_names_in_file():
    with open("names.txt") as file:
        for l in file.readlines():
            print(l)


def get_names_from_file():
    with open("names.txt") as file:
        for name in file.readlines():
            yield name


def print_users():
    for user in users:
        for key, value in user.items():
            end_spaces = len(key) * ' '
            value += end_spaces[len(value):]
            print(value, end='|')
        print('\n')


def sort_users():
    return sorted(users, key=lambda k: k['last_name'])


def sort_user_names(names):
    sorted_names = sorted(names, key= lambda n : (n[0], n.split(' ')[1][0]))
    return sorted_names


def print_number_of_names(number_of_names):
    message = f'Total of {number_of_names} names'
    print(message)
    print('-'*len(message))


def print_names(names):
    for name in names:
        print(name.rstrip())
    print()


if __name__ == "__main__":
    print_header()
    names = [name for name in get_names_from_file()]
    sorted_names = sort_user_names(names)
    print_number_of_names(len(sorted_names))
    print_names(sorted_names)

    