from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def setUp(self):
        app.numbers = [100, 200, 1000, 300]

    def test_print_header(self):
        
        expected = '-----------------------\n Computing Statistics \n-----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_number(self):
        expected_number = 100
        expected = 'Enter a number: '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('done', '100')
            number = app.get_number()
            mocked_input.assert_called_with(expected)
            self.assertEqual(number, 'done')

            number = app.get_number()
            self.assertEqual(number, expected_number)

    def test_get_numbers(self):
        expected_calls = [
            call('Enter a number: '),
            call('Enter a number: '),
            call('Enter a number: '),
            call('Enter a number: '),
            call('Enter a number: ')
        ]

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('100', '200', '1000', '300', 'done')
            app.get_numbers()

            mocked_input.assert_has_calls(expected_calls)

    def test_print_numbers(self):

        with patch('builtins.print') as mocked_print:
            app.print_numbers()
            mocked_print.assert_called_with('Numbers: 100, 200, 1000, 300')

    def test_print_average(self):

        with patch('builtins.print') as mocked_print:
            app.print_average()
            mocked_print.assert_called_with('The average is 400')

    def test_print_minimum(self):
        
        with patch('builtins.print') as mocked_print:
            app.print_minimum()
            mocked_print.assert_called_with('The minimum is 100')

    def test_print_maximum(self):
        
        with patch('builtins.print') as mocked_print:
            app.print_maximum()
            mocked_print.assert_called_with('The maximum is 1000')

    def test_print_standard_deviation(self):
        
        with patch('builtins.print') as mocked_print:
            app.print_standard_deviation()
            mocked_print.assert_called_with('The standard deviation is 408.25.')