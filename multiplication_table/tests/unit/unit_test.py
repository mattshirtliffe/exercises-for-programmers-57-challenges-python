from unittest import TestCase
import app

class MultiplicationTableTest(TestCase):
    
    def test_multiply_numbers(self):
        
        answer = app.multiply(12, 12)
        self.assertEqual(answer, 144)