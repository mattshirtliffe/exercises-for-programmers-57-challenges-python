from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected_header_text = '-----------\n Mad Libs \n-----------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_once_with(expected_header_text)


    def test_get_noun(self):
        value = 'Dog'
        with patch('builtins.input', return_value=value) as mocked_input:
            noun = app.get_noun()
            mocked_input.assert_called_with('Enter a noun: ')
            self.assertEqual(noun, value)

    def test_get_verb(self):
        value = 'walk'
        with patch('builtins.input', return_value=value) as mocked_input:
            verb = app.get_verb()
            mocked_input.assert_called_with('Enter a verb: ')
            self.assertEqual(verb, value)

    def test_get_adjective(self):
        value = 'blue'
        with patch('builtins.input', return_value=value) as mocked_input:
            adjective = app.get_adjective()
            mocked_input.assert_called_with('Enter a adjective: ')
            self.assertEqual(adjective, value)

    def test_get_adverb(self):
        value = 'quickly'
        with patch('builtins.input', return_value=value) as mocked_input:
            adverb = app.get_adverb()
            mocked_input.assert_called_with('Enter a adverb: ')
            self.assertEqual(adverb, value)
    
    def test_print_mad_lib(self):
        noun = 'Dog'
        verb = 'walk'
        adjective = 'blue'
        adverb = 'quickly'
        expected_mad_lib = f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!' 
        with patch('builtins.print') as mocked_print:
            app.print_mad_lib(noun, verb, adjective, adverb)
            mocked_print.assert_called_once_with(expected_mad_lib)