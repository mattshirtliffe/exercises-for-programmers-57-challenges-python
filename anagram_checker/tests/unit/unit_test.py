from unittest import TestCase
import app

class AnagramTest(TestCase):
    
    def test_is_anagram(self):
        is_anagram = app.is_anagram('tone', 'note')
        self.assertTrue(is_anagram)