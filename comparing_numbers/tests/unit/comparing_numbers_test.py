from unittest import TestCase
import app

class ComparingNumbersTest(TestCase):
    
    def test_get_largest_number(self):
        expected_largest_number = 51
        numbers = [1, 51, 2]
        largest_number = app.get_largest_number(numbers)
        self.assertEqual(largest_number, expected_largest_number)