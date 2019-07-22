from unittest import TestCase
import app

class ComputeInterestTest(TestCase):
    
    def test_calc_investment(self):
        expected = 1758
        principal = 1500
        rate = 4.3
        years =  4
        v = app.calc_investment(principal, rate, years)
        self.assertEqual(v, expected)