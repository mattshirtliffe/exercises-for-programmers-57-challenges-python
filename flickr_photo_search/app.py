import os
import requests
from string import Template

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Flickr photo search \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)

def get_template():
    template_file_text = ''
    with open('template.html', 'r') as f:
        template_file_text = ''.join(f.readlines())
    return Template(template_file_text)
    
def get_search_string():
    
    while True:
        search_string = input('Search string: ')
        if len(search_string) > 0:
            return search_string
        else:
            print('A valid input required.')


def get_pictures_for_tag(tag):
    
    response = requests.get(f'https://www.flickr.com/services/feeds/photos_public.gne?format=json&tags={tag}&nojsoncallback=true')
    response.raise_for_status
    if response.ok:
        return response

def write_content(search_string, content):
    with open(f'{search_string}.html', 'w') as f:
        f.writelines(content)

if __name__ == "__main__":
    print_header()
    template = get_template()
    search_string = get_search_string()
    
    images = ''
    response = get_pictures_for_tag(search_string)
    if response:
        if response.status_code == 200:
            data = response.json()
            items = data['items']
            
            for item in items:
                image_url = item['media']['m']
                title = item['title']
                images += f' <img src="{image_url}" alt="{title}"> \n'


    content = template.substitute(tag=search_string, images=images)
    write_content(search_string, content)

    
