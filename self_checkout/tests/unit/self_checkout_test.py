from unittest import TestCase
import app

class SelfCheckoutTest(TestCase):

    def test_get_price_of_items(self):
        # unit test
        expected_total = 50
        price = 25
        quantity = 2
        total = app.get_price_of_items(price, quantity)
        self.assertEqual(total, expected_total)

    def test_get_items_subtotal(self):
        # unit test
        expected_items_subtotal = 39
        item_prices = [25, 10, 4]
        items_subtotal = app.get_items_subtotal(item_prices)
        self.assertEqual(items_subtotal, expected_items_subtotal)
    
    def test_get_tax(self):
        # unit test
        subtotal = 64.00
        expected_tax = 3.52
        tax = app.get_tax(subtotal)
        self.assertEqual(tax, expected_tax)
    
    def test_get_total(self):
        # unit test
        subtotal = 64.00
        tax = 3.52
        expected_total = 67.52
        total = app.get_total(subtotal, tax)
        self.assertEqual(total, expected_total)