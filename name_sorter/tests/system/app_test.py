from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------\n Name sorter \n--------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_print_names_in_file(self):
        calls = [
            call('Ling, Mai\n'),
            call('Johnson, Jim\n'),
            call('Zarnecki, Sabrina\n'),
            call('Jones, Chris\n'),
            call('Jones, Aaron\n'),
            call('Swift, Geoffrey\n'),
            call('Xiong, Fong')
        ]
        with patch('builtins.print') as mocked_print:
            app.print_names_in_file()
            mocked_print.assert_has_calls(calls)

    def test_get_names_from_file(self):
        names = [
            'Ling, Mai',
            'Johnson, Jim',
            'Zarnecki, Sabrina',
            'Jones, Chris',
            'Jones, Aaron',
            'Swift, Geoffrey',
            'Xiong, Fong'
        ]
        for name in app.get_names_from_file():
            self.assertIn(name.rstrip(), names)

    def test_sort_user_names(self):

        names = [name.rstrip() for name in app.get_names_from_file()]
        expected_names = ['Jones, Aaron', 'Jones, Chris', 'Johnson, Jim', 'Ling, Mai', 'Swift, Geoffrey', 'Xiong, Fong', 'Zarnecki, Sabrina']
        sorted_names = app.sort_user_names(names)
        self.assertListEqual(sorted_names, expected_names)

    def test_print_number_of_names(self):
        number_of_names = 7
        calls = [
            call(f'Total of {number_of_names} names'),
            call('----------------')
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_number_of_names(number_of_names)
            mocked_print.assert_has_calls(calls)

    def test_print_print_names(self):

        sorted_names = ['Jones, Aaron', 'Jones, Chris', 'Johnson, Jim', 'Ling, Mai', 'Swift, Geoffrey', 'Xiong, Fong', 'Zarnecki, Sabrina']
        calls = [
            call('Jones, Aaron'),
            call('Jones, Chris'),
            call('Johnson, Jim'),
            call('Ling, Mai'),
            call('Swift, Geoffrey'),
            call('Xiong, Fong'),
            call('Zarnecki, Sabrina')
        ]
        
        with patch('builtins.print') as mocked_print:
            app.print_names(sorted_names)
            mocked_print.assert_has_calls(calls)