from unittest import TestCase
from unittest.mock import patch, call
import app
import os

class AppTest(TestCase):

    # def setUp(self):
    #     file_name = 'products.json'
    #     if not os.path.exists(file_name):
    #         open(file_name, 'a').close()
    
    # def tearDown(self):
    #     pass

    def test_print_header(self):
        
        expected = '-------------\n Trivia App \n-------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_read_questions_from_file(self):
        with patch('builtins.open') as mocked_open:
            data = app.read_questions_from_file()
            mocked_open.assert_called_with('questions.json')
            self.assertIsInstance(data, dict)

    def test_select_random_question(self):

        return_value = {
          "question":"What is PEP 8?",
          "answers":[
             {
                "answer":"PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.",
                "is_correct":True
             },
             {
                "answer":"PEP 8 is the name of the guy who developed python.",
                "is_correct":False
             }
          ]
       }

        with patch('random.choice', return_value=return_value):
            data = app.read_questions_from_file()
            question = app.select_random_question(data)
            self.assertEqual(question, return_value)


    def test_print_question(self):
        question = {'question': 'What is pickling and unpickling?', 'answers': [{'answer': 'Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling. ', 'is_correct': True}, {'answer': 'Pickle module is a tool for creating pickles', 'is_correct': False}]}
        expected = 'What is pickling and unpickling?'
        with patch('builtins.print') as mocked_print:
            app.print_question(question)
            mocked_print.assert_called_with(expected)

    def test_print_answers(self):
        question = {'question': 'What is pickling and unpickling?', 'answers': [{'answer': 'Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling. ', 'is_correct': True}, {'answer': 'Pickle module is a tool for creating pickles', 'is_correct': False}]}
        expected = [
            call('1: Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling. '),
            call('2: Pickle module is a tool for creating pickles')
            ]
        with patch('builtins.print') as mocked_print:
            app.print_answers(question)
            mocked_print.assert_has_calls(expected)

    def test_get_answer(self):
        
        expected_answer = 1
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', '3', '1')
            answer = app.get_answer(2)
            mocked_input.assert_called_with('Answer number: ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(answer, expected_answer)

    def test_check_answer(self):
        question = {'question': 'What is pickling and unpickling?', 'answers': [{'answer': 'Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling. ', 'is_correct': True}, {'answer': 'Pickle module is a tool for creating pickles', 'is_correct': False}]}
        is_correct =  app.check_answer(1 ,question['answers'])
        self.assertTrue(is_correct)

    
    def get_product_name(self):
        
        expected_product_name = 'iPad'
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'iPad')
            product_name = app.get_product_name()
            mocked_input.assert_called_with('What is the product name? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(product_name, expected_product_name)

    def get_serial_number(self):

        expected_serial_number = 'AXB124AXY'
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'AXB124AXY')
            serial_number = app.get_serial_number()
            mocked_input.assert_called_with('What is the serial number? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(serial_number, expected_serial_number)

    def get_product_value(self):

        expected_product_value = 399.00
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', '399.00')
            product_value = app.get_product_value()
            mocked_input.assert_called_with('What is the product value? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(product_value, expected_product_value)


    def get_json_from_file(self):
        with patch('builtins.open') as mocked_open:
            data = app.get_json_from_file()
            mocked_open.assert_called_with('products.json')
            self.assertIsInstance(data, dict)

    def save_product(self):
        with patch('builtins.open') as mocked_open:
            data = {}
            product = {'name': 'a', 'value': 1.0, 'serial_number': '1'}
            data = app.save_product(data, product)
            mocked_open.assert_called_with('products.json', 'w')

    def print_products(self):
        expected = '+------+-------+---------------+\n| name | value | serial_number |\n+------+-------+---------------+\n| a    | 1.0   | 1             |\n| b    | 2.0   | 2             |\n+------+-------+---------------+'
        with patch('builtins.print') as mocked_print:
            data = {'products': [{'name': 'a', 'value': 1.0, 'serial_number': '1'}, {'name': 'b', 'value': 2.0, 'serial_number': '2'}]}
            app.print_products(data)
            mocked_print.assert_called_with(expected)