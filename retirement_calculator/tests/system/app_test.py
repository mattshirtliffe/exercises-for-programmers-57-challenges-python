from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '------------------------\n Retirement Calculator \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)
    
    def test_get_current_age(self):
        expected = 'What is your current age? '
        expected_age=30
        with patch('builtins.input', return_value='30') as mocked_print:
            age = app.get_current_age()
            mocked_print.assert_called_with(expected)
            self.assertEqual(age, expected_age)

    def test_get_retirement_age(self):
        expected = 'At what age would you like to retire? '
        expected_retirement_age=80
        with patch('builtins.input', return_value='80') as mocked_print:
            retirement_age = app.get_retirement_age()
            mocked_print.assert_called_with(expected)
            self.assertEqual(retirement_age, expected_retirement_age)

    def test_print_years_left_message(self):
        years = 25
        expected = f'You have {years} years left until you can retire'
        with patch('builtins.print') as mocked_print:
            app.print_years_left_messages(years)
            mocked_print.assert_called_with(expected)

    def test_print_retirement_year_message(self):
        this_year = 2015
        retirement_year = 2055
        expected = f'It\'s {this_year}, so you can retire in {retirement_year}'
        with patch('builtins.print') as mocked_print:
            app.print_retirement_year_message(2015, 2055)
            mocked_print.assert_called_with(expected)
