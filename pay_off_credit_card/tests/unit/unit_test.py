from unittest import TestCase
import app

class PayOffCreditCardTest(TestCase):
    
    def test_calculate_months_until_paid_off(self):
        balance = 5000
        apr = 12
        monthly_payments = 100
        
        months_until_paid_off = app.calculate_months_until_paid_off(balance, apr, monthly_payments)
        self.assertEqual(months_until_paid_off, 70)