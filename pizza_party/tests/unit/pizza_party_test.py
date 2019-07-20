from unittest import TestCase
import app

class PizzaPartyTest(TestCase):

    def test_get_number_of_slices(self):
        expected = 16
        number_of_pizza = 2
        slices = app.get_number_of_slices(number_of_pizza)
        self.assertEqual(expected, slices)

    def test_get_slices_per_person(self):
        expected = 2
        total_number_of_slices = 16
        number_of_people = 8
        slices_per_person = app.get_slices_per_person(total_number_of_slices, number_of_people)
        self.assertEqual(expected, slices_per_person)

    def test_get_leftover_slices(self):
        expected = 0
        total_number_of_slices = 16
        number_of_people = 8
        leftover_slices = app.get_leftover_slices(total_number_of_slices, number_of_people)
        self.assertEqual(expected, leftover_slices)