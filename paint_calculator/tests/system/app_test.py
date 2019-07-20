from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '-------------------\n Paint Calculator \n-------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_ceiling_length(self):
        expected_input = 'What is the length of your ceiling? '
        expected_length = 10
        with patch('builtins.input', return_value='10') as mocked_input:
            length = app.get_ceiling_length()
            mocked_input.assert_called_with(expected_input)
            self.assertEqual(length, expected_length)

    def test_get_ceiling_width(self):
        expected_input = 'What is the width of your ceiling? '
        expected_width = 10
        with patch('builtins.input', return_value='10') as mocked_input:
            width = app.get_ceiling_width()
            mocked_input.assert_called_with(expected_input)
            self.assertEqual(width, expected_width)

    def test_print_gallons_needed(self):
        area = 360
        gallons = 2
        expected = f'You will need to purchase {gallons} gallons of\n paint to cover {area} square feet.'
        with patch('builtins.print') as mocked_print:
            app.print_gallons_needed(gallons, area)
            mocked_print.assert_called_with(expected)