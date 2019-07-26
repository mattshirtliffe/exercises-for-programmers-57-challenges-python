from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-----------------\n BMI Calculator \n-----------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_height(self):

        expected = 'Enter your height in feet and inches: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '6.3')
                height = app.get_height()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
            
                self.assertEqual(height, '6.3')

    def test_get_weight(self):

        expected = 'Enter your weight in pounds: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '280')
                weight = app.get_weight()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
            
                self.assertEqual(weight, 280)
    
    def test_print_bmi(self):
        bmi = 34.99
        expected = f'Your BMI is {bmi}'
        with patch('builtins.print') as mocked_print:
            app.print_bmi(bmi)
            mocked_print.assert_called_with(expected)

    def test_print_bmi_status(self):
        
        ideal_bmi = 18.5
        under_bmi = 17
        over_bmi = 32.5
        
        expected_ideal = 'You are within the ideal weight range.'
        expected_bad = 'You are overweight. You should see your doctor.'
        with patch('builtins.print') as mocked_print:
            
            app.print_bmi_status(ideal_bmi)
            mocked_print.assert_called_with(expected_ideal)

            
            app.print_bmi_status(under_bmi)
            mocked_print.assert_called_with(expected_bad)

            app.print_bmi_status(over_bmi)
            mocked_print.assert_called_with(expected_bad)