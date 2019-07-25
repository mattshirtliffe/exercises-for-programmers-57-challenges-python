from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------------\n Temperature Converter \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)


    def test_print_prompt(self):
        
        expected = 'Press C to convert from Fahernheit to Celsius.\nPress F to convert from Celsius to Fahernheit.\n'
        with patch('builtins.print') as mocked_print:
            app.print_prompt()
            mocked_print.assert_called_with(expected)

    def test_get_temp_format(self):

        expected = 'What choice: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', 'C', 'F')
                temp_format = app.get_temp_format()
                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid input is required')
                self.assertEqual(temp_format, 'C')
                temp_format = app.get_temp_format()
                self.assertEqual(temp_format, 'F')

    def test_get_temperature(self):

        expected = 'Please enter the temperature in Fahernheit: '
        expected_temperature = 32
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad', '32', '32')
                temperature = app.get_temperature('F')
                mocked_print.assert_called_once_with('a valid input required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(temperature, expected_temperature)
                expected = 'Please enter the temperature in Celsius: '
                temperature = app.get_temperature('C')
                mocked_input.assert_called_with(expected)
                self.assertEqual(temperature, expected_temperature)
    

    def test_print_temperature(self):
        
        with patch('builtins.print') as mocked_print:
            temperature_format = 'C'
            temperature = 0
            app.print_temperature(temperature_format, temperature)
            mocked_print.assert_called_with('The temperature in Celsius is 0')
            temperature_format = 'F'
            temperature = 32
            app.print_temperature(temperature_format, temperature)
            mocked_print.assert_called_with('The temperature in Fahernheit is 32')

