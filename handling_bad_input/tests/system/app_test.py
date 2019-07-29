from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------\n Handling bad inputs \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_rate_of_return(self):

        expected = 'What is the rate of return? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '0', 'ABC', '4')
                rate_of_return = app.get_rate_of_return()
                mocked_print.assert_called_with('Sorry. That\'s not a valid input.')
                mocked_input.assert_called_with(expected)
                self.assertEqual(rate_of_return, 4)

    def test_print_years(self):
        
        years = 18
        expected = f'It will take {years} to double your initial investment.'
        with patch('builtins.print') as mocked_print:
            app.print_years(years)
            mocked_print.assert_called_with(expected)