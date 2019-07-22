from unittest import TestCase
import app

class CurrencyConversionTest(TestCase):

    def test_calculate_amount(self):
        expected = 111.38
        euro = 81
        exchange_rate = 137.51
        rate = app.calculate_amount(euro, exchange_rate)
        self.assertEqual(rate, expected)