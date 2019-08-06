import os
from unittest import TestCase
from unittest.mock import patch, call
import app


class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-----------------------\n Grabbing the weather \n-----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)


    def test_get_weather_for_city(self):
        city_name = 'Sheffield'
        response_json = {'coord': {'lon': -1.47, 'lat': 53.38}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 19.99, 'pressure': 1007, 'humidity': 49, 'temp_min': 17.78, 'temp_max': 22.22}, 'visibility': 10000, 'wind': {'speed': 7.2, 'deg': 230}, 'clouds': {'all': 20}, 'dt': 1565007677, 'sys': {'type': 1, 'id': 1382, 'message': 0.0072, 'country': 'GB', 'sunrise': 1564979280, 'sunset': 1565034948}, 'timezone': 3600, 'id': 2638077, 'name': 'Sheffield', 'cod': 200}
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            mocked_request_get.return_value.json.return_value = response_json
            response = app.get_weather_for_city(city_name)
            self.assertEqual(response.status_code, 200)
            api_key = os.environ['OPEN_WEATHER_MAP_API_KEY']
            mocked_request_get.assert_called_with(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q=Sheffield&appid={api_key}')
            self.assertEqual(response.json(), response_json)


    def test_print_weather_data(self):
        
        expected = [call('Sheffield weather:'), call('20 degrees celsius')]
        temp = 20
        location = 'Sheffield'

        with patch('builtins.print') as mocked_print:
            app.print_weather_data(temp, location)
            mocked_print.assert_has_calls(expected)