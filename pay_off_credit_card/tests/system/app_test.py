from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------------------\n Months to Pay Off a Credit Card \n----------------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_balance(self):

        expected = 'What is your balance? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '5000')
                balance = app.get_balance()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(balance, 5000)

    def test_get_apr(self):
        expected = 'What is the APR on the card (as a percent)? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '12')
                apr = app.get_apr()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(apr, 12)

    def test_get_monthly_payments(self):
        expected = 'What are the monthly payment you can make? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '100')
                monthly_payments = app.get_monthly_payments()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(monthly_payments, 100)

    def test_print_months_take_to_pay(self):
        
        months = 70
        expected = f'It will take you {months} months to pay off this card'
        with patch('builtins.print') as mocked_print:
            app.print_months_take_to_pay(months)
            mocked_print.assert_called_with(expected)