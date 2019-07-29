from unittest import TestCase
import app

class HandlingBadInputTest(TestCase):
    
    def test_calculate_years(self):
        
        expected = 18
        rate_of_return = 4
        years = app.calculate_years(rate_of_return)
        self.assertEqual(years, expected)