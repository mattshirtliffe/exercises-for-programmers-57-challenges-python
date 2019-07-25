from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------------\n Legal driving age \n--------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)


    def test_get_age(self):

        expected = 'What is your age? '
        expected_age = 15
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad', '15')
                age = app.get_age()
                mocked_print.assert_called_once_with('a valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(age, expected_age)

    def test_print_driving_message(self):
        
        expected = f'You are not old enough to legally drive.'
        with patch('builtins.print') as mocked_print:
            app.print_driving_message(15)
            mocked_print.assert_called_with(expected)
            app.print_driving_message(17)
            expected = f'You are old enough to legally drive.'
            mocked_print.assert_called_with(expected)