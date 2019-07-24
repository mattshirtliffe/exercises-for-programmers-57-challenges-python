from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '----------------------\n Password Validation \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_password(self):
        expected_input = 'What is the password? '
        expected_password = '12345'
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('','12345')
            password = app.get_password()
            mocked_input.assert_called_with(expected_input)
            self.assertEqual(password, expected_password)
    
    def test_check_password(self):
        # unit test
        invalid_password = '12345'
        valid_password = 'abc$123'
        is_valid = app.get_is_password_valid(invalid_password)
        self.assertEqual(False, is_valid)
        is_valid = app.get_is_password_valid(valid_password)
        self.assertEqual(True, is_valid)

    def test_print_message(self):
        expected_invalid = 'I dont\'t know you'
        expected_valid = 'Welcome!'
        with patch('builtins.print') as mocked_print:
            app.print_message('12345')
            mocked_print.assert_called_with(expected_invalid)
            app.print_message('abc$123')
            mocked_print.assert_called_with(expected_valid)