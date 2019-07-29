from unittest import TestCase
import app

class AppTest(TestCase):

    def setUp(self):
        self.length = 15
        self.width = 20
        self.expected = 300

    def test_calculate_area_square_feet(self):

        area_square_feet = app.calculate_area_square_feet(self.length, self.width)
        self.assertEqual(area_square_feet, self.expected)

    def test_calculate_area_square_meters(self):
        expected = 27.871
        area_square_meters = app.calculate_area_square_meters(self.length, self.width)
        self.assertEqual(area_square_meters, expected)