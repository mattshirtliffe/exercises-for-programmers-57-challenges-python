from unittest import TestCase
import app

class PaintCalculatorTest(TestCase):

    def test_calculate_area(self):
        expected = 300
        width = 15
        length = 20
        area =  app.calculate_area(width, length)
        self.assertEqual(expected, area)
    
    def test_calculate_gallons_needed(self):
        area = 360
        expected_gallons = 2
        gallons_needed = app.calculate_gallons_needed(area)
        self.assertEqual(expected_gallons, gallons_needed)