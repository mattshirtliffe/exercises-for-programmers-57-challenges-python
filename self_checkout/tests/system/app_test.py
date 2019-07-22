from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '----------------\n Self-Checkout \n----------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_item_price(self):

        item_number = 1
        expected_input_text = f'Enter the price of item {item_number}: '
        expected_item_price = 25

        with patch('builtins.input', return_value='25') as mocked_input:
            item_price = app.get_item_price(item_number)
            mocked_input.assert_called_with(expected_input_text)
            self.assertEqual(item_price, expected_item_price)

    def test_get_item_quantity(self):

        item_number = 1
        expected_input_text = f'Enter the quantity of item {item_number}: '
        expected_item_quantity = 2

        with patch('builtins.input', return_value='2') as mocked_input:
            item_quantity = app.get_item_quantity(item_number)
            mocked_input.assert_called_with(expected_input_text)
            self.assertEqual(item_quantity, expected_item_quantity)

    def test_print_subtotal(self):
        subtotal = 64.00
        expected = f'Subtotal: {subtotal}'
        with patch('builtins.print') as mocked_print:
            app.print_subtotal(subtotal)
            mocked_print.assert_called_with(expected)

    def test_print_tax(self):
        tax = 3.52
        expected = f'Tax: {tax}'
        with patch('builtins.print') as mocked_print:
            app.print_tax(tax)
            mocked_print.assert_called_with(expected)

    def test_print_total(self):
        total = 67.52
        expected = f'Total: {total}'
        with patch('builtins.print') as mocked_print:
            app.print_total(total)
            mocked_print.assert_called_with(expected)