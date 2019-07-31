from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------------\n Filtering records \n--------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_search_string(self):
        with patch('builtins.print') as mocked_print, patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('', 'Jac')
            search_string = app.get_search_string()
            mocked_input.assert_called_with('Enter a search string: ')
            mocked_print.assert_called_with('A valid input is required')

    def test_print_headings(self):
        calls = [
            call('First Name', end='|'),
            call('Last Name', end='|'),
            call('Position', end='|'),
            call('Separation date'),
            call()
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_headings()
            mocked_print.assert_has_calls(calls)

    def test_print_users(self):
        calls = [
            call('John      ', end='|'),
            call('Johnson  ', end='|'),
            call('Manager ', end='|'),
            call('2016-12-31     ', end='|'),
            call('\n'),
            call('Tou       ', end='|'),
            call('Xiong    ', end='|'),
            call('Software Engineer', end='|'),
            call('2016-10-05     ', end='|'),
            call('\n'),
            call('Michaela  ', end='|'),
            call('Michaelson', end='|'),
            call('District Manage', end='|'),
            call('2015-12-19     ', end='|'),
            call('\n'),
            call('Jake      ', end='|'),
            call('Jacobson ', end='|'),
            call('Programmer', end='|'),
            call('               ', end='|'),
            call('\n'),
            call('Jacquelyn ', end='|'),
            call('Jackson  ', end='|'),
            call('DBA     ', end='|'),
            call('               ', end='|'),
            call('\n'),
            call('Sally     ', end='|'),
            call('Weber    ', end='|'),
            call('Web Developer', end='|'),
            call('2015-12-18     ', end='|'),
            call('\n')
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_users()
            mocked_print.assert_has_calls(calls)

    def test_sort_users(self):


        expected = [
            {'first_name':'John', 'last_name':'Johnson', 'position':'Manager', 'separation_date':'2016-12-31'},
            {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'},
            {'first_name':'Michaela', 'last_name':'Michaelson', 'position':'District Manage', 'separation_date':'2015-12-19'},
            {'first_name':'Jake', 'last_name':'Jacobson', 'position':'Programmer', 'separation_date':''},
            {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''},
            {'first_name':'Sally', 'last_name':'Weber', 'position':'Web Developer', 'separation_date':'2015-12-18'}
        ]

        app.users = app.sort_users()
        self.assertDictEqual(app.users[-1], {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'})
        self.assertDictEqual(app.users[0], {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''})