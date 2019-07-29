from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-----------------\n Adding Numbers \n-----------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_numbers(self):

        expected = 'Enter a number: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '1', '2', '3', '4', '5')
                numbers = app.get_numbers()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertListEqual([i+1 for i in range(5)], numbers)

    def test_print_total(self):
        
        total = 15
        expected = f'The total is {total}.'
        with patch('builtins.print') as mocked_print:
            app.print_total(total)
            mocked_print.assert_called_with(expected)