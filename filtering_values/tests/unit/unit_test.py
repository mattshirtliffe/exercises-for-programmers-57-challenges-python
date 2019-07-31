from unittest import TestCase
import app

class FilteringValuesTest(TestCase):

    def test_get_evens(self):
        evens = app.get_evens([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertListEqual(evens, [2, 4, 6, 8])