from unittest import TestCase
import app

class BacTest(TestCase):

    def test_calculate_blood_alcohol(self):
        expected_blood_alcohol = 0.08
        weight = 100
        gender = 'm'
        drinks = 4
        hours = 1
        blood_alcohol = app.calculate_blood_alcohol(weight, gender, drinks, hours)
        self.assertEqual(blood_alcohol, expected_blood_alcohol)