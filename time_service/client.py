import requests


def get_data():
    url = 'http://localhost:5000/'
    response = requests.get(url)
    response.raise_for_status
    if response.ok:
        return response


def print_current_time(time):
    print(f'The current time is {time}')


if __name__ == "__main__":
    data = get_data()
    data = data.json()
    print_current_time(data['current_time'])