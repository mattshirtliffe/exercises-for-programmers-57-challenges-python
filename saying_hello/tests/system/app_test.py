from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):
    
    def test_print_header(self):
        expected = '---------------\n Saying Hello \n---------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_name(self):      
        with patch('builtins.input', return_value='Matthew') as mocked_input:
            name = app.get_name()
            mocked_input.assert_called_with('What is your name? ')
            self.assertEqual('Matthew', name)
    
    def test_get_name_invalid(self):      
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('', 'Matthew')
            name = app.get_name()
            mocked_input.assert_called_with('What is your name? ')
            self.assertEqual('Matthew', name)
    
    def test_print_greeting(self):
        name = 'Matthew'
        expected = f'Hello {name}, nice to meet you'
        with patch('builtins.print') as mocked_print:
            app.print_greeting(name)
            mocked_print.assert_called_with(expected)
    
    @patch('app.print_header')
    @patch('app.get_name')
    @patch('app.print_greeting')
    def test_run(self, print_header, get_name, print_greeting):
        with patch('builtins.input', return_value='Matthew'):
            app.run()
            print_header.assert_called()
            get_name.assert_called()
            print_greeting.assert_called()

