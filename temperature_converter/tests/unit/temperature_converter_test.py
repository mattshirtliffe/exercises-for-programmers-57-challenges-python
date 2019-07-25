from unittest import TestCase
import app

class TemperatureConverterTest(TestCase):

    def calculate_blood_alcohol(self):
        pass
        expected_blood_alcohol = 0.08
        weight = 100
        gender = 'm'
        drinks = 4
        hours = 1
        blood_alcohol = app.calculate_blood_alcohol(weight, gender, drinks, hours)
        self.assertEqual(blood_alcohol, expected_blood_alcohol)

    def test_celsius_to_fahernheit(self):
        expected = 32
        temperature = app.celsius_to_fahernheit(0)
        self.assertEqual(temperature, expected)

    def test_fahernheit_to_celsius(self):
        expected = 0
        temperature = app.fahernheit_to_celsius(32)
        self.assertEqual(temperature, expected)