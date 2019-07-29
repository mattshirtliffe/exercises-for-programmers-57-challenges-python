

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Anagram Checker \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def prompt_get_strings():
    print('Enter two strings and I\'ll tell you if they\nare anagrams: ')


def get_first_string():

    while True:
        first_string = input('Enter the first string: ')
        
        if len(first_string) >=3:
            return first_string
        else:
            print('A valid input is required')


def get_second_string():

    while True:
        second_string = input('Enter the second string: ')
        
        if len(second_string) >=3:
            return second_string
        else:
            print('A valid input is required')


def is_anagram(first_string, second_string):

    return sorted(first_string) == sorted(second_string) 


def print_is_anagram(first_string, second_string):
    if(is_anagram(first_string, second_string)):
        print(f'{first_string} and {second_string} are anagrams.')

if __name__ == "__main__":
    
    print_header()
    prompt_get_strings()
    first_string = get_first_string()
    second_string = get_second_string()
    print_is_anagram(first_string, second_string)