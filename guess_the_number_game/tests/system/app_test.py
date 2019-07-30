from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------------------\n Guess the Number Game \n------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_print_play(self):
        
        expected = 'Let\'s play Guess the number.'
        with patch('builtins.print') as mocked_print:
            app.print_play()
            mocked_print.assert_called_with(expected)

    def test_get_difficulty(self):
        expected_input_text= 'Pick a difficulty level (1, 2 or 3): '
        expected = 1
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('','4','1')
            difficulty = app.get_difficulty()
            mocked_print.assert_called_with('A valid input is required')
            mocked_input.assert_called_with(expected_input_text)
            difficulty = app.get_difficulty()
            self.assertEqual(difficulty, expected)

    def test_create_number(self):
        expected = 1
        with patch('random.randint', return_value=1):
            number = app.create_number(1)
            self.assertEqual(number, expected)
