from unittest import TestCase
import app

class AddingNumbersTest(TestCase):
    
    def test_get_total(self):
        expected = 15
        numbers = [1, 2, 3, 4, 5]
        total = app.get_total(numbers)
        self.assertEqual(total, expected)