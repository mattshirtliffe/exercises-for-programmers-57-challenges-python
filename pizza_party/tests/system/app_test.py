from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '--------------\n Pizza Party \n--------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

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
    
    def test_get_number_of_pizza(self):
        
        expected_number_of_pizza = 2
        expected_input_text = 'How many pizzas fo you have? '
        with patch('builtins.input', return_value='2') as mocked_input:
            number_of_pizza = app.get_number_of_pizza()
            mocked_input.assert_called_with(expected_input_text)
            self.assertEqual(number_of_pizza, expected_number_of_pizza)
    
    def test_print_people_and_pizzas(self):
        people = 8
        pizza = 2
        expected = f'{people} people with {pizza} pizzas'
        with patch('builtins.print') as mocked_print:
            app.print_people_and_pizzas(people, pizza)
            mocked_print.assert_called_with(expected)

    def test_print_person_gets(self):
        
        with patch('builtins.print') as mocked_print:
            slices = 2
            expected = f'Each peron gets {slices} slices of pizza'
            app.print_person_gets(slices)
            mocked_print.assert_called_with(expected)
            slices = 1
            expected = f'Each peron gets {slices} slice of pizza'
            app.print_person_gets(slices)
            mocked_print.assert_called_with(expected)

    def test_print_leftover_slices(self):
        with patch('builtins.print') as mocked_print:
            slices = 2
            expected = f'There are {slices} leftover slices'
            app.print_leftover(slices)
            mocked_print.assert_called_with(expected)

            slices = 1
            expected = f'There is {slices} leftover slice'
            app.print_leftover(slices)
            mocked_print.assert_called_with(expected)