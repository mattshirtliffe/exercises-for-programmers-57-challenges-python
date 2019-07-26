from unittest import TestCase
import app

class BMITest(TestCase):

    def test_calculate_bmi(self):
        
        expected = 34.99
        height = 75
        weight = 280
        bmi = app.calculate_bmi(weight, height)
        self.assertEqual(bmi, expected)


    def test_convert_height_to_inches(self):
        
        expected = 75
        inches = app.convert_height_to_inches('6.3')
        self.assertEqual(inches, expected)