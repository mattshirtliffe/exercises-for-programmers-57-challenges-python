from unittest import TestCase
import app

class CalcFunTest(TestCase):

    def test_add_numbers(self):
        first_number = 10
        second_number = 5
        result = app.add_numbers(first_number, second_number)
        self.assertEqual(result, 15)

    def test_subtract_numbers(self):
        first_number = 10
        second_number = 5
        result = app.subtract_numbers(first_number, second_number)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        first_number = 10
        second_number = 5
        result = app.multiply_numbers(first_number, second_number)
        self.assertEqual(result, 50)

    def test_divide_numbers(self):
        first_number = 10
        second_number = 5
        result = app.divide_numbers(first_number, second_number)
        self.assertEqual(result, 2)
