from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------------\n Comparing Numbers \n--------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_first_number(self):
        expected = 1
        expected_input = 'Enter the first number: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '1')
                number = app.get_first_number()
                mocked_input.assert_called_with(expected_input)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(number, expected)

    def test_get_second_number(self):
        expected = 51
        expected_input = 'Enter the second number: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '51')
                number = app.get_second_number()
                mocked_input.assert_called_with(expected_input)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(number, expected)

    def test_get_third_number(self):
        expected = 2
        expected_input = 'Enter the third number: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '2')
                number = app.get_third_number()
                mocked_input.assert_called_with(expected_input)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(number, expected)

    def test_print_name_of_month_message(self):
         
        largest_number = 51
        expected = f'The largest number is {largest_number}'
        with patch('builtins.print') as mocked_print:
            
            app.print_largest_number(largest_number)
            mocked_print.assert_called_with(expected)