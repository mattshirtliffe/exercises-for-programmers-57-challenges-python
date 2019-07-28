from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-----------------------------\n Troubleshooting car issues \n-----------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_get_yes_or_no(self):
        expected = False
        expected_input = 'Is the car silent when you turn the key? '
        question = expected_input
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', 'y', 'n')
                answer = app.get_yes_or_no(question)
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
                self.assertEqual(answer, not expected)
                answer = app.get_yes_or_no(question)
                self.assertEqual(answer, expected)