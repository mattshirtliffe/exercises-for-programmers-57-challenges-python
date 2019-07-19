from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '--------------\n Pizza Party \n--------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)


    # def test_get_length_of_the_room(self):
    #     expected_length_room = 15
    #     expected = 'What is the length of the room in feet? '
    #     with patch('builtins.input') as mocked_input:
    #         with patch('builtins.print') as mocked_print:
    #             mocked_input.side_effect = ('bad input', '15')
    #             length_of_the_room = app.get_length_of_the_room()
    #             mocked_input.assert_called_with(expected)
    #             mocked_print.assert_called_with('A valid number is required')
    #             self.assertEqual(length_of_the_room, expected_length_room)

    def test_get_number_of_people(self):
        expected_number_of_people = 8
        expected = 'How many people? '
        
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', '8')
                number_of_people = app.get_number_of_people()

                mocked_input.assert_called_with(expected)
                mocked_print.assert_called_with('A valid number is required')
                self.assertEqual(number_of_people, expected_number_of_people)