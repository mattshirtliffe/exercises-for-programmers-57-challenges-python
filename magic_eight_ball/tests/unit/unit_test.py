from unittest import TestCase
import app

class KarvonenHeartRateTest(TestCase):

    def calculate_target_heart_rate(self):
        
        target_heart_rate = app.calculate_target_heart_rate(55, 22, 65)
        self.assertEqual(target_heart_rate, 138)