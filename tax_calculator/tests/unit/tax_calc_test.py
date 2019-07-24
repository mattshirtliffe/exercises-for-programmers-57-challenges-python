from unittest import TestCase
import app

class AppTest(TestCase):
    
    def test_calculate_tax(self):
        subtotal = 10.00
        expected = 0.55
        tax = app.calculate_tax(subtotal)
        self.assertEqual(tax, expected)

    def test_calculate_total(self):
        expected_total = 10.55
        subtotal = 10.00
        tax = 0.55
        total = app.calculate_total(subtotal, tax)
        self.assertEqual(total, expected_total)
