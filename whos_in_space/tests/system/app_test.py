from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------\n Who\'s in space? \n------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)


    def test_get_who_is_in_space(self):

        response_json = {'message': 'success', 'people': [{'name': 'Alexey Ovchinin', 'craft': 'ISS'}, {'name': 'Nick Hague', 'craft': 'ISS'}, {'name': 'Christina Koch', 'craft': 'ISS'}, {'name': 'Alexander Skvortsov', 'craft': 'ISS'}, {'name': 'Luca Parmitano', 'craft': 'ISS'}, {'name': 'Andrew Morgan', 'craft': 'ISS'}], 'number': 6}
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            mocked_request_get.return_value.json.return_value = response_json
            response = app.get_who_is_in_space()
            self.assertEqual(response.status_code, 200)
            mocked_request_get.assert_called_with('http://api.open-notify.org/astros.json')
            self.assertEqual(response.json(), response_json)


    def test_print_people_in_space(self):
        
        expected = [
            call('The are 6 people in space right now:\n'),
            call('Name | Craft'),
            call('Alexey Ovchinin | ISS'),
            call('Nick Hague | ISS'),
            call('Christina Koch | ISS'),
            call('Alexander Skvortsov | ISS'),
            call('Luca Parmitano | ISS'),
            call('Andrew Morgan | ISS')
        ]
        with patch('builtins.print') as mocked_print:
            response_json = {'message': 'success', 'people': [{'name': 'Alexey Ovchinin', 'craft': 'ISS'}, {'name': 'Nick Hague', 'craft': 'ISS'}, {'name': 'Christina Koch', 'craft': 'ISS'}, {'name': 'Alexander Skvortsov', 'craft': 'ISS'}, {'name': 'Luca Parmitano', 'craft': 'ISS'}, {'name': 'Andrew Morgan', 'craft': 'ISS'}], 'number': 6}
            app.print_people_in_space(response_json)
            mocked_print.assert_has_calls(expected)