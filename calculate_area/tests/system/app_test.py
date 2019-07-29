from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '-------------------------------------\n Calculate area of a rectangle room \n-------------------------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_length_of_the_room(self):
        expected_length_room = 15
        expected = 'What is the length of the room in feet? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '15')
                length_of_the_room = app.get_length_of_the_room()
                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(length_of_the_room, expected_length_room)

    def test_get_width_of_the_room(self):
        expected_width_room = 20
        expected = 'What is the width of the room in feet? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('bad input', '20')
                width_of_the_room = app.get_width_of_the_room()
                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(width_of_the_room, expected_width_room)

    def test_print_entered_dimensions(self):
        length = 15
        width = 20
        expected = f'You entered dimensions of {length} feet by {width} feet.'
        with patch('builtins.print') as mocked_print:
            app.print_entered_dimensions(length, width)
            mocked_print.assert_called_with(expected)

    def test_print_area_message(self):
        square_feet= 300
        square_meters = 27.871
        expected = f'The are is\n{square_feet} square feet\n{square_meters} square meters'
        with patch('builtins.print') as mocked_print:
            app.print_area_message(square_feet, square_meters)
            mocked_print.assert_called_with(expected)