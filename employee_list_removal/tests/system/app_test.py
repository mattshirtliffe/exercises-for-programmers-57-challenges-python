from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def setUp(self):
        pass

    def test_print_header(self):
        
        expected = '------------------------\n Employee list removal \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_employee_name(self):
        expected_employee_name = 'Chris Jones'
        expected = 'Enter an employee name to remove: '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('', 'Chris Jones')
            employee_name = app.get_employee_name()
            mocked_print.assert_called_with('A valid input is required')
            mocked_input.assert_called_with(expected)
            self.assertEqual(employee_name, expected_employee_name)

    def test_print_employees(self):
        expected_calls = [
            call('There are 5 employees:'),
            call('John Smith'),
            call('Jakie Jackson'),
            call('Chris Jones'),
            call('Amanda Cullen'),
            call('Jeremy Goodwin')
        ]
        with patch('builtins.print') as mocked_print:
            app.print_employees()
            mocked_print.assert_has_calls(expected_calls)

    def test_remove_employee(self):

        expected_calls = [
            call('There are 4 employees:'),
            call('John Smith'),
            call('Jakie Jackson'),
            call('Amanda Cullen'),
            call('Jeremy Goodwin')
        ]
        with patch('builtins.print') as mocked_print:
            app.remove_employee('Chris Jones')
            app.print_employees()
            mocked_print.assert_has_calls(expected_calls)

    