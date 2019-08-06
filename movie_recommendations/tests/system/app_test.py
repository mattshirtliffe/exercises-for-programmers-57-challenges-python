import os
from unittest import TestCase
from unittest.mock import patch, call
import app

from string import Template


class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------------\n Movie Recommendations \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_movie_name(self):
        expected = 'Enter the name of a movie: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'Guardians of the Galaxy')
                search_string = app.get_movie_name()
                mocked_print.assert_called_with('A valid input required.')
                mocked_input.assert_called_with(expected)
                self.assertEqual(search_string, 'Guardians%20of%20the%20Galaxy')


    def test_get_movie_data(self):
        movie_name = 'Guardians%20of%20the%20Galaxy'
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            response = app.get_movie_data(movie_name)
            self.assertEqual(response.status_code, 200)
            api_key = os.environ['OMD_API_KEY']
            mocked_request_get.assert_called_with(f'https://www.omdbapi.com/?apikey={api_key}&t=Guardians%20of%20the%20Galaxy')


    def test_print_movie_data(self):
        
        expected = [
            call('Title: Guardians of the Galaxy'),
            call('Year: 2014'),
            call('Rated: PG-13'),
            call('Runtime: 121 min'),
            call('Plot: A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.'),
            call('You should watch this film right now!')
        ]

        with patch('builtins.print') as mocked_print:
            data = {
                'Title': 'Guardians of the Galaxy', 
                'Year': '2014',
                'Rated': 'PG-13',
                'Released': '01 Aug 2014',
                'Runtime': '121 min',
                'Plot': 'A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.',
                'Ratings':[{'Source':'Rotten Tomatoes','Value':'91%'}]
            }

            app.print_movie_data(data)
            mocked_print.assert_has_calls(expected)