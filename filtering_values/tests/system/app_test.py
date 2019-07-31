from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-------------------\n Filtering Values \n-------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_numbers(self):
        expected_number = 2
        expected = 'Enter a list of numbers, separated by spaces: '
        with patch('builtins.input', return_value='1 2 3 4 5 6 7 8') as mocked_input:
            numbers = app.get_numbers()
            mocked_input.assert_called_with(expected)
            self.assertListEqual(numbers, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_print_evens(self):
        expected = 'The even numbers are 2 4 6 8.'
        with patch('builtins.print') as mocked_print:
            app.print_evens([2, 4, 6, 8])
            mocked_print.assert_called_with(expected)