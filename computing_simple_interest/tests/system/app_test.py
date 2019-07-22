from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '----------------------------\n Computing simple interest \n----------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header('Computing simple interest')
            mocked_print.assert_called_with(expected)

    def test_get_principal(self):
        expected_principal = 1500
        expected = 'Enter the principal: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '1500')
                principal = app.get_principal()
                mocked_print.assert_called_with('A valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(principal, expected_principal)


    def test_get_rate_of_interest(self):
        expected_rate_of_interest = 4.3
        expected = 'Enter the rate of interest: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '4.3')
                rate_of_interest = app.get_rate_of_interest()
                mocked_print.assert_called_with('A valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(rate_of_interest, expected_rate_of_interest)

    def test_get_number_of_years(self):
        expected_number_of_years = 4
        expected = 'Enter the number of years: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '4')
                number_of_years = app.get_number_of_years()
                mocked_print.assert_called_with('A valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(number_of_years, expected_number_of_years)

    def test_print_investment(self):
        years = 4
        interest = 4.3
        investment_value = 1758
        expected = f'After {years} at {interest}, the investment will\n be worth {investment_value}.'
        with patch('builtins.print') as mocked_print:
            app.print_investment(years, interest, investment_value)
            mocked_print.assert_called_with(expected)