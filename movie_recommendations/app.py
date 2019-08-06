import os
import requests
from string import Template
import urllib

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Movie Recommendations \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)

    
def get_movie_name():
    
    while True:
        name = input('Enter the name of a movie: ')
        if len(name) > 0:
            return urllib.parse.quote(name)
        else:
            print('A valid input required.')


def get_movie_data(movie_name):
    api_key = os.environ['OMD_API_KEY']
    url = f'https://www.omdbapi.com/?apikey={api_key}&t={movie_name}'
    response = requests.get(url)
    response.raise_for_status
    if response.ok:
        return response

def print_movie_data(data):
    
    title = data['Title']
    year = data['Year']
    rated = data['Rated']
    runtime = data['Runtime']
    plot = data['Plot']
    
    print(f'Title: {title}')
    print(f'Year: {year}')
    print(f'Rated: {rated}')
    print(f'Runtime: {runtime}')
    print(f'Plot: {plot}')
    for rating in data.get('Ratings'):
        if rating['Source'] == "Rotten Tomatoes":
            rating = int(rating['Value'].replace('%', ''))
            if rating >= 80:
                print('You should watch this film right now!')


if __name__ == "__main__":
    print_header()
    movie_name = get_movie_name()
    response = get_movie_data(movie_name)
    if response:
        if response.status_code == 200:
            print_movie_data(response.json())

    
