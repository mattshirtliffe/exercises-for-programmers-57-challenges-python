from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '--------------\n Word finder \n--------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_text_from_file(self):
        expected = 'One should never utilize the word \"utilize\" in\nwriting. Use "use" instead.'
        text = app.get_text_from_file()
        self.assertEqual(text, expected)

    def test_replace_utilize(self):
        text = 'One should never utilize the word \"utilize\" in\nwriting. Use "use" instead.'
        expected = 'One should never use the word \"use\" in\nwriting. Use "use" instead.'
        text = app.replace_utilize(text)
        self.assertEqual(text, expected)

    def test_get_new_file_name(self):
        
        expected_file_name = 'test.txt'
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'test.txt')
            file_name = app.get_new_file_name()
            mocked_input.assert_called_with('What is the output file name? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(file_name, expected_file_name)

    def test_create_file(self):
        content = 'One should never use the word \"use\" in\nwriting. Use "use" instead.'
        with patch('builtins.open') as mocked_open:

            app.create_output_file('test.text', content)
            mocked_open.assert_called_with('test.text', 'w')