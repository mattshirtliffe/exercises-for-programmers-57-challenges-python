from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '---------------\n Simple Maths \n---------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_first_number(self):
        value = '10'
        expected_first_number = 10
        with patch('builtins.input', return_value=value) as mocked_input:
            first_number = app.get_first_number()
            mocked_input.assert_called_with('What is the first number? ')
            self.assertEqual(first_number, expected_first_number)

    def test_get_first_number_invalid(self):
        expected_first_number = 10
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '10')
                first_number = app.get_first_number()
                mocked_input.assert_called_with('What is the first number? ')
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(first_number, expected_first_number)

    def test_get_second_number(self):
        value = '5'
        expected_second_number = 5
        with patch('builtins.input', return_value=value) as mocked_input:
            second_number = app.get_second_number()
            mocked_input.assert_called_with('What is the second number? ')
            self.assertEqual(second_number, expected_second_number)

    def test_print_add_numbers_result(self):
        first_number = 10
        second_number = 5
        result= 15
        expected = f'{first_number} + {second_number} = {result}'
        with patch('builtins.print') as mocked_print:
            app.print_add_numbers_result(first_number, second_number, result)
            mocked_print.assert_called_with(expected)

    def test_print_subtract_numbers_result(self):
        first_number = 10
        second_number = 5
        result= 15
        expected = f'{first_number} - {second_number} = {result}'
        with patch('builtins.print') as mocked_print:
            app.print_subtract_numbers_result(first_number, second_number, result)
            mocked_print.assert_called_with(expected)

    def test_print_multiply_numbers_result(self):
        first_number = 10
        second_number = 5
        result= 15
        expected = f'{first_number} * {second_number} = {result}'
        with patch('builtins.print') as mocked_print:
            app.print_multiply_numbers_result(first_number, second_number, result)
            mocked_print.assert_called_with(expected)

    def test_print_divide_numbers_result(self):
        first_number = 10
        second_number = 5
        result= 15
        expected = f'{first_number} / {second_number} = {result}'
        with patch('builtins.print') as mocked_print:
            app.print_divide_numbers_result(first_number, second_number, result)
            mocked_print.assert_called_with(expected)