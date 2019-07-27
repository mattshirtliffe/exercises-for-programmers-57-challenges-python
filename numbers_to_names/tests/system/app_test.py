from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-------------------\n Numbers to Names \n-------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_month_number(self):

        expected = 3
        expected_input = 'Please enter the number of the month?: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '13', '3')
                month_number = app.get_month_number()
                mocked_input.assert_called_with(expected_input)
                mocked_print.assert_called_with('A valid month number is required')
                self.assertEqual(month_number, expected)
    
    def test_print_name_of_month_message(self):
         
        month = 'March'
        expected = f'The name of the month is {month}'
        with patch('builtins.print') as mocked_print:
            
            app.print_name_of_month_message(month)
            mocked_print.assert_called_with(expected)