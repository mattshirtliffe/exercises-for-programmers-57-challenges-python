from unittest import TestCase
from unittest.mock import patch
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
                