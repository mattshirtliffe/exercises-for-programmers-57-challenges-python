from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------\n Parsing a data file \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_record_from_file(self):

        records = [
            {'last': 'Ling', 'first': 'Mai', 'salary': '55900'},
            {'last': 'Johnson', 'first': 'Jim', 'salary': '56500'},
            {'last': 'Jones', 'first': 'Aaron', 'salary': '46000'},
            {'last': 'Jones', 'first': 'Chris', 'salary': '34500'},
            {'last': 'Swift', 'first': 'Geoffrey', 'salary': '14200'},
            {'last': 'Xiong', 'first': 'Fong', 'salary': '65000'},
            {'last': 'Zarnecki', 'first': 'Sabrina', 'salary': '51500'}
        ]
        for record in app.get_record_from_file():
            self.assertIn(record, records)

    def test_print_headings(self):
        calls = [
            call('Last     First     Salary'),
            call('-------------------------')
        ]
        expected = '----------------------\n Parsing a data file \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_headings()
            mocked_print.assert_has_calls(calls)

    def test_print_records(self):
        calls = [
            call('Ling     ', end=''),
            call('Mai       ', end=''),
            call('55900      ', end=''),
            call(),
            call('Johnson  ', end=''),
            call('Jim       ', end=''),
            call('56500      ', end=''),
            call(),
            call('Jones    ', end=''),
            call('Aaron     ', end=''),
            call('46000      ', end=''),
            call(),
            call('Jones    ', end=''),
            call('Chris     ', end=''),
            call('34500      ', end=''),
            call(),
            call('Swift    ', end=''),
            call('Geoffrey  ', end=''),
            call('14200      ', end=''),
            call(),
            call('Xiong    ', end=''),
            call('Fong      ', end=''),
            call('65000      ', end=''),
            call(),
            call('Zarnecki ', end=''),
            call('Sabrina   ', end=''),
            call('51500      ', end=''),
            call()
        ]
        expected = '----------------------\n Parsing a data file \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_records()
            mocked_print.assert_has_calls(calls)