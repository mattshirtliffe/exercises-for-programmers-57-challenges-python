import os
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch, call
import app

import pickledb


from string import Template


class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------\n Todo List \n------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_task(self):
        expected = 'Enter task: '
        with patch('builtins.input', return_value='Pick up some milk') as mocked_input:
            with patch('builtins.print') as mocked_print:
                task = app.get_task()
                mocked_input.assert_called_with(expected)
                self.assertEqual(task, 'Pick up some milk')
    
    def test_store_task(self):
        task = 'Pick up some milk'
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            app.store_task(task)
            mocked_load.assert_called_with('tasks.db', True)
            mock.set.assert_called_with('Pick up some milk', False)

    def test_print_tasks(self):
        expected_calls = [call('Tasks: '), call('go for a walk'), call('Pick up some milk')]
        tasks = {"go for a walk": False, "Pick up some milk": False}
        with patch('builtins.print') as mocked_print:
            app.print_tasks(tasks.keys())
            mocked_print.assert_has_calls(expected_calls)

    def test_get_tasks(self):
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            tasks = app.get_tasks()
            mocked_load.assert_called_with('tasks.db', True)
            mock.getall.assert_called()

    def test_delete_task(self):
        task = 'Pick up some milk'
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            app.delete_task(task)
            mocked_load.assert_called_with('tasks.db', True)
            mock.exists.assert_called()
            mock.rem.assert_called_with(task)


    def get_movie_data(self):
        movie_name = 'Guardians%20of%20the%20Galaxy'
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            response = app.get_movie_data(movie_name)
            self.assertEqual(response.status_code, 200)
            api_key = os.environ['OMD_API_KEY']
            mocked_request_get.assert_called_with(f'https://www.omdbapi.com/?apikey={api_key}&t=Guardians%20of%20the%20Galaxy')


    def print_movie_data(self):
        
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