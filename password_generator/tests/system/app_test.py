from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '---------------------\n Password Generator \n---------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_minimum_length(self):
        expected_minimum_length = 8
        expected = 'What\'s the minimum length? '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('', '8')
            minimum_length = app.get_minimum_length()
            mocked_input.assert_called_with(expected)
            mocked_print.assert_called_with('A valid input is required')
            self.assertEqual(minimum_length, expected_minimum_length)

    def test_get_number_of_special_chars(self):
        expected_number = 2
        expected = 'How many special characters? '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('', '2')
            number = app.get_number_of_special_chars()
            mocked_input.assert_called_with(expected)
            mocked_print.assert_called_with('A valid input is required')
            self.assertEqual(number, expected_number)

    def test_build_password(self):
        length = 8 
        special = 2
        numbers = 2
        password = app.build_password(length, special, numbers)