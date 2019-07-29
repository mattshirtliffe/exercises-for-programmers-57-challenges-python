from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------------\n Validating Inputs \n--------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_first_name(self):

        expected = 'Enter your first name: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'Matthew')
                first_name = app.get_first_name()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(first_name, 'Matthew')

    def test_get_last_name(self):

        expected = 'Enter your last name: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'Shirtliffe')
                last_name = app.get_last_name()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(last_name, 'Shirtliffe')

    def test_get_employee_id(self):

        expected = 'Enter your employee id: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'AA-1234')
                employee_id = app.get_employee_id()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(employee_id, 'AA-1234')

    def test_get_zip_code(self):

        expected = 'Enter your zip code: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'ABCDE')
                zip_code = app.get_zip_code()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(zip_code, 'ABCDE')