from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------------------\n Password Strength Indicator \n------------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_first_string(self):

        expected = 'Enter password: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , '12345')
                password = app.get_password()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(password, '12345')

    def test_password_validator(self):

        with patch('builtins.print') as mocked_print:
            password = '12345'
            expected = f'The password \'{password}\' is a very weak password'
            app.password_validator(password)
            mocked_print.assert_called_with(expected)

            password = 'abcdef'
            expected = f'The password \'{password}\' is a weak password'
            app.password_validator(password)
            mocked_print.assert_called_with(expected)
    
            password = 'abcd123xyz'
            expected = f'The password \'{password}\' is a strong password'
            app.password_validator(password)
            mocked_print.assert_called_with(expected)

            password = '1337h@xor!'
            expected = f'The password \'{password}\' is a very strong password'
            app.password_validator(password)
            mocked_print.assert_called_with(expected)