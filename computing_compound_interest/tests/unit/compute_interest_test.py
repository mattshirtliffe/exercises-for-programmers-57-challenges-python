from unittest import TestCase
import app

class ComputeInterestTest(TestCase):
    
    def test_calc_investment(self):
        expected = 1938.84
        principal = 1500
        rate = 4.3
        years =  6
        compound = 4
        v = app.calc_investment(principal, rate, years, compound)
        self.assertEqual(v, expected)