from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------------\n Word frequency finder \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_text_from_file(self):
        expected = 'badger badger badger badger mushroom mushroom\nsnake badger badger badger'
        text = app.get_text_from_file()
        self.assertEqual(text, expected)

    def test_count_frequency(self):
        text = 'badger badger badger badger mushroom mushroom\nsnake badger badger badger'
        expected = {'badger': 7, 'mushroom': 2, 'snake': 1}
        text = app.count_frequency(text)
        self.assertDictEqual(text, expected)

    def test_print_frequency_histogram(self):
        words_freq = {'badger': 7, 'mushroom': 2, 'snake': 1}
        expected_called = [call('badger: *******'), call('mushroom: **'), call('snake: *')]
        with patch('builtins.print') as mocked_print:
            app.print_frequency_histogram(words_freq)
            mocked_print.assert_has_calls(expected_called)