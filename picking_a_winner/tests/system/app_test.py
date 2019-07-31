from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def setUp(self):
        pass

    def test_print_header(self):
        
        expected = '-------------------\n Picking a Winner \n-------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_name(self):
        expected_name = 'Homer'
        expected = 'Enter a name: '
        with patch('builtins.input') as mocked_input, patch('builtins.print') as mocked_print:
            mocked_input.side_effect = ('', 'Homer')
            name = app.get_name()
            mocked_print.assert_called_with('A valid input is required')
            mocked_input.assert_called_with(expected)
            self.assertEqual(name, expected_name)

    def test_get_name(self):
        expected_calls = [
            call('Enter a name: '),
            call('Enter a name: '),
            call('Enter a name: '),
            call('Enter a name: '),
            call('Enter a name: '),
            call('Enter a name: ')
        ]

        with patch('builtins.print') as mocked_print, patch('builtins.input', return_value='name') as mocked_input:
            app.get_names()

            mocked_input.assert_has_calls(expected_calls)

    def test_pick_winner(self):

        expected_name = 'Maggie'
        app.names = [
            'Homer',
            'Bart',
            'Maggie',
            'Lisa',
            'Moe'
        ]
        with patch('random.choice', return_value='Maggie'):
            name = app.pick_name()
            self.assertEqual(name, expected_name)

    def test_print_winner(self):
        
        winner_name = 'Maggie'
        expected = f'The winner is... {winner_name}'
        with patch('builtins.print') as mocked_print:
            app.print_winner(winner_name)
            mocked_print.assert_called_with(expected) 