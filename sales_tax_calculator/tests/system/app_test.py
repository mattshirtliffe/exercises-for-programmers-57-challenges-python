from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------------------\n Multistate sales_tax_calculator \n----------------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_order_amount(self):

        expected = 10
        expected_input = 'What is the order amount?: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '10')
                order_amount = app.get_order_amount()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
                self.assertEqual(order_amount, expected)

    def test_get_state(self):

        expected_state = 'Wisconsin'
        expected_input = 'What state do you live in? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', 'Wisconsin')
                state = app.get_state()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
            
                self.assertEqual(state, expected_state)
    
    def test_get_county(self):

        expected_county = 'Eau Claire'
        expected_input = 'What county do you live in? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', 'Eau Claire')
                county = app.get_county()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
            
                self.assertEqual(county, expected_county)
    
    def test_print_tax(self):
         
        tax = 0.50
        expected = f'The tax is {tax:.2f}'
        with patch('builtins.print') as mocked_print:
            
            app.print_tax(tax)
            mocked_print.assert_called_with(expected)

    def test_print_total(self):
         
        total = 10.50
        expected = f'The total is {total:.2f}'
        with patch('builtins.print') as mocked_print:
            app.print_total(total)
            mocked_print.assert_called_with(expected)