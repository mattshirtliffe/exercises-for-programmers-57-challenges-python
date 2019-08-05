import requests


def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Who\'s in space? \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_who_is_in_space():
    response = requests.get('http://api.open-notify.org/astros.json')
    # response.raise_for_status
    if response.ok:
        return response

def print_people_in_space(json):
    people = json['people']
    print(f'The are {len(people)} people in space right now:\n')
    print('Name | Craft')
    for value in people:
        name = value['name']
        craft = value['craft']
        print(f'{name} | {craft}')

if __name__ == "__main__":
    print_header()
    response = get_who_is_in_space()
    json = response.json()
    print_people_in_space(json)
