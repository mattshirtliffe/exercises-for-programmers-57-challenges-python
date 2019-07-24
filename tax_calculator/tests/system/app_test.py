from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '-----------------\n Tax calculator \n-----------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_order_amount(self):
        expected_order_amount = 10
        expected = 'What is the order amount? '
        with patch('builtins.input', return_value='10') as mocked_input:
            order_amount = app.get_order_amount()
            mocked_input.assert_called_with(expected)
            self.assertEqual(order_amount, expected_order_amount)

    def test_get_state(self):
        expected = 'What is the state? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', 'WI', 'MN')
                state = app.get_state()
                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid input is required')
                self.assertEqual(state, 'WI')
                state = app.get_state()
                self.assertEqual(state, 'MN')
    
    def test_print_subtotal(self):
        subtotal = 10.00
        expected = f'The subtotal is {subtotal:.2f}.'
        with patch('builtins.print') as mocked_print:
            app.print_subtotal(subtotal)
            mocked_print.assert_called_with(expected)

    def test_print_tax(self):
        tax = 10.00
        expected = f'The tax is {tax:.2f}.'
        with patch('builtins.print') as mocked_print:
            app.print_tax(tax)
            mocked_print.assert_called_with(expected)
    
    def test_print_total(self):
        total = 10.00
        expected = f'The total is {total:.2f}.'
        with patch('builtins.print') as mocked_print:
            app.print_total(total)
            mocked_print.assert_called_with(expected)

    
    def test_print_message(self):
        order_amount = 10.00
        expected = f'The total is {order_amount:.2f}.'
        with patch('builtins.print') as mocked_print:
            app.print_message('WI', order_amount)
            mocked_print.assert_has_calls([
                call('The subtotal is 10.00.'),
                call('The tax is 0.55.'),
                call('The total is 10.55.')
                ])

            app.print_message('MN', order_amount)
            mocked_print.assert_called_with(expected)
