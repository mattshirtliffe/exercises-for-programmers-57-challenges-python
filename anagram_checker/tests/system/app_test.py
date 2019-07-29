from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------\n Anagram Checker \n------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_prompt_get_strings(self):

        expected = 'Enter two strings and I\'ll tell you if they\nare anagrams: '
        with patch('builtins.print') as mocked_print:
            app.prompt_get_strings()
            mocked_print.assert_called_with(expected)
    
    def test_get_first_string(self):

        expected = 'Enter the first string: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'note')
                first_string = app.get_first_string()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(first_string, 'note')

    def test_get_first_string(self):

        expected = 'Enter the second string: '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('' , 'tone')
                second_string = app.get_second_string()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected)
                self.assertEqual(second_string, 'tone')


    def test_print_is_anagram(self):

        first_string = 'note'
        second_string = 'tone'

        expected = f'{first_string} and {second_string} are anagrams.'
        with patch('builtins.print') as mocked_print:
            app.print_is_anagram(first_string, second_string)
            mocked_print.assert_called_with(expected)