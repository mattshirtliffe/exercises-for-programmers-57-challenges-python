import os
import requests


def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Grabbing the weather \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)
    
def get_location():
    
    while True:
        location = input('Where are you? ')
        if len(location) > 0:
            return location
        else:
            print('A valid input required.')


def get_weather_for_city(city_name):
    
    api_key = os.environ.get('OPEN_WEATHER_MAP_API_KEY', None)
    if not api_key:
        print('API KEY NOT FOUND')
        print('export OPEN_WEATHER_MAP_API_KEY={YOUR KEY}')
        return
    
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={city_name}&appid={api_key}')
    response.raise_for_status
    if response.ok:
        return response

def print_weather_data(temp, location):

    print(f'{location} weather:')
    print(f'{temp} degrees celsius')

if __name__ == "__main__":
    print_header()
    location = get_location()
    response = get_weather_for_city(location)
    if response:
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temp =  main['temp']
            print_weather_data(temp, location)