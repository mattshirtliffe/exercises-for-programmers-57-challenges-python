import os
from string import Template

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Website generator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_site_name():
    while True:
        site_name = input('Site name: ')
        if len(site_name) > 0:
            return site_name
        else:
            print('A valid input required')


def get_author_name():
    while True:
        name = input('Author: ')
        if len(name) > 0:
            return name
        else:
            print('A valid input required')


def ask_if_javacript():

    while True:
        answer = input('Do you want a folder for JavaScript? ')
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print('A valid input is required')

def ask_if_css():

    while True:
        answer = input('Do you want a folder for CSS? ')
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print('A valid input is required')

def create_folder(name):
    try:
        os.mkdir(name)
    except OSError:
        print (f'Failed to create ./{name}')
    else:
        print (f'Created ./{name}')


def create_file(path, content):
    path = os.path.join(path,'index.html')
    with open(path, 'w') as f:
        f.writelines(content)

if __name__ == '__main__':
    print_header()
    site_name = get_site_name()
    author_name = get_author_name()
    create_folder(site_name)
    javacript = ask_if_javacript()
    css = ask_if_css()
    if css:
        create_folder(os.path.join(site_name, 'css'))

    if javacript:
        create_folder(os.path.join(site_name, 'js'))

    template_file_text = ''
    with open('template.html', 'r') as f:
        template_file_text = ''.join(f.readlines())
    s = Template(template_file_text)
    
    create_file(site_name, s.substitute(name=site_name, author=author_name))

    