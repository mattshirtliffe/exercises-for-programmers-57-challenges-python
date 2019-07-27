from unittest import TestCase
import app

class NumbersToNamesTest(TestCase):
    
    def test_get_month_from_number(self):
        month_number = 3
        expected_month = 'March'
        month = app.get_month_from_number(month_number)
        self.assertEqual(month, expected_month)