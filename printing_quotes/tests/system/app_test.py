from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '------------------\n Printing Quotes \n------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_quote(self):
        value = 'These arn\'t the droids you\'re looking for'
        with patch('builtins.input', return_value=value) as mocked_input:
            quote = app.get_quote()
            mocked_input.assert_called_with('What is the quote? ')
            self.assertEqual(quote, value)

    def test_get_author_name(self):
        expect_author_name = 'Obi-Wan Kenobi'
        with patch('builtins.input', ) as mocked_input:
            author_name = app.get_author_name()
            mocked_input.assert_called_with('Who said it? ')
            self.assertEqual(author_name, expect_author_name)
    
    def test_print_quotes(self):
        expected_quote = 'These arn\'t the droids you\'re looking for'
        expected_author_name = 'Obi-Wan Kenobi'
        expected_quote_output = f'{expected_author_name} says, \"{expected_quote}\"'
        with patch('builtins.print') as mocked_print:
            app.print_quotes(expected_author_name, expected_quote)
            mocked_print.assert_called_with(expected_quote_output)