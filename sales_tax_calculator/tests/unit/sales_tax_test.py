from unittest import TestCase
import app

class SalesTaxTest(TestCase):
    
    def test_calculate_state_tax(self):
        amount = 10
        state = 'Wisconsin'
        expected = 0.5
        tax = app.calculate_state_tax(amount, state)
        self.assertEqual(tax, expected)

        state = 'Illinois'
        expected = 0.8
        tax = app.calculate_state_tax(amount, state)
        self.assertEqual(tax, expected)

        state = 'New York'
        expected = 0.0
        tax = app.calculate_state_tax(amount, state)
        self.assertEqual(tax, expected)


    def test_calculate_county_tax(self):
        amount = 100
        county = 'Eau Claire'
        expected = 0.005
        tax = app.calculate_county_tax(amount, county)
        self.assertEqual(tax, expected)


        county = 'Dunn'
        expected = 0.004
        tax = app.calculate_county_tax(amount, county)
        self.assertEqual(tax, expected)

        county = 'Other'
        expected = 0.00
        tax = app.calculate_county_tax(amount, county)
        self.assertEqual(tax, expected)

    def test_calculate_total(self):
        amount = 10
        tax = 0.51
        total = app.calculate_total(amount, tax)
        self.assertEqual(10.51, total)