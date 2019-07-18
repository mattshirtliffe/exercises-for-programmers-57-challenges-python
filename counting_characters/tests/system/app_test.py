from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '----------------------\n Counting Characters \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_input(self):
        with patch('builtins.input', return_value='Homer') as mocked_input:
            app.get_input()
            mocked_input.assert_called_with('What is the input string? ')

    def test_get_input_invalid(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('', 'Homer')
            with patch('builtins.print') as mocked_print:
                app.get_input()
                mocked_input.assert_called_with('What is the input string? ')
                mocked_print.assert_called_with('A valid input required')

    def test_print_header(self):
        input_str = 'Homer'
        expected = f'{input_str} has 5 characters.'
        with patch('builtins.print') as mocked_print:
            app.print_message(input_str)
            mocked_print.assert_called_with(expected)

    @patch('app.print_header')
    @patch('app.get_input')
    @patch('app.print_message')
    def test_run(self, print_header, get_input, print_message):
        with patch('builtins.input', return_value='Homer'):
            app.run()
            print_header.assert_called()
            get_input.assert_called()
            print_message.assert_called()