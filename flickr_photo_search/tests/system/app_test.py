import os
from unittest import TestCase
from unittest.mock import patch, call
import app

from string import Template


class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------\n Flickr photo search \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_template(self):
        
        template = app.get_template()
        self.assertIsInstance(template, Template)

    def test_get_search_string(self):
        expected = 'Search string: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'cat')
                search_string = app.get_search_string()
                mocked_print.assert_called_with('A valid input required.')
                mocked_input.assert_called_with(expected)
                self.assertEqual(search_string, 'cat')

    def test_get_weather_for_city(self):
        tag = 'Cat'
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            response = app.get_pictures_for_tag(tag)
            self.assertEqual(response.status_code, 200)
            mocked_request_get.assert_called_with(f'https://www.flickr.com/services/feeds/photos_public.gne?format=json&tags={tag}&nojsoncallback=true')

    def test_write_content(self):
        with patch('builtins.open') as mocked_open:
            app.write_content('cat', 'content')
            mocked_open.assert_called_with('cat.html', 'w')