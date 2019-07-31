from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '---------------\n Magic 8 Ball \n---------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_question(self):

        expected = 'What\'s your question? '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('', 'Will I be rich and famous?')
            question = app.get_question()
            mocked_print.assert_called_with('A valid input is required')
            mocked_input.assert_called_with(expected)
            self.assertEqual(question, 'Will I be rich and famous?')

    def test_print_response(self):
        expected = 'Ask again later.'
        with patch('builtins.print') as mocked_print, patch('random.choice', return_value='Ask again later.'):
            app.print_response()
            mocked_print.assert_called_with(expected)