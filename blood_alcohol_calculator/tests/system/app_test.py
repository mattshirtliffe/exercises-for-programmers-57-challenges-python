from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '---------------------------\n Blood alcohol calculator \n---------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_weight(self):

        expected = 'What is your weight? '
        expected_age = 15
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad', '15')
                age = app.get_weight()
                mocked_print.assert_called_once_with('a valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(age, expected_age)

    def test_get_gender(self):

        expected = 'What is you gender? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', 'm', 'f')
                gender = app.get_gender()
                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid input is required')
                self.assertEqual(gender, 'm')
                gender = app.get_gender()
                self.assertEqual(gender, 'f')

    def test_get_number_of_drinks(self):

        expected = 'How many drinks? '
        expected_drinks = 3
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '3')
                drinks = app.get_number_of_drinks()
                mocked_print.assert_called_once_with('a valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(drinks, expected_drinks)

    def test_get_hours_since_drink(self):

        expected = 'Number of hours since last drink? '
        expected_hours = 2
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '2')
                drinks = app.get_hours_since_drink()
                mocked_print.assert_called_once_with('a valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(drinks, expected_hours)
    
    def test_print_bac(self):
        blood_alcohol = 0.08
        with patch('builtins.print') as mocked_print:
            app.print_bac(blood_alcohol)
            mocked_print.assert_called_with(f'Your BAC is {blood_alcohol}')

    def test_print_legal_bac(self):
        blood_alcohol = 0.08
        with patch('builtins.print') as mocked_print:
            app.print_legal_bac(blood_alcohol)
            mocked_print.assert_called_with('It is not legal for you to drive')
            app.print_legal_bac(0.05)
            mocked_print.assert_called_with('It is legal for you to drive')

