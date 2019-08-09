from unittest import TestCase
from unittest.mock import patch, call
import app
import os

class AppTest(TestCase):

    def setUp(self):
        file_name = 'products.json'
        if not os.path.exists(file_name):
            open(file_name, 'a').close()
    
    def tearDown(self):
        pass

    def test_print_header(self):
        
        expected = '---------------------\n Tracking inventory \n---------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)
    
    def test_get_product_name(self):
        
        expected_product_name = 'iPad'
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'iPad')
            product_name = app.get_product_name()
            mocked_input.assert_called_with('What is the product name? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(product_name, expected_product_name)

    def test_get_serial_number(self):

        expected_serial_number = 'AXB124AXY'
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'AXB124AXY')
            serial_number = app.get_serial_number()
            mocked_input.assert_called_with('What is the serial number? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(serial_number, expected_serial_number)

    def test_get_product_value(self):

        expected_product_value = 399.00
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', '399.00')
            product_value = app.get_product_value()
            mocked_input.assert_called_with('What is the product value? ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(product_value, expected_product_value)


    def test_get_json_from_file(self):
        with patch('builtins.open') as mocked_open:
            data = app.get_json_from_file()
            mocked_open.assert_called_with('products.json')
            self.assertIsInstance(data, dict)

    def test_save_product(self):
        with patch('builtins.open') as mocked_open:
            data = {}
            product = {'name': 'a', 'value': 1.0, 'serial_number': '1'}
            data = app.save_product(data, product)
            mocked_open.assert_called_with('products.json', 'w')

    def test_print_products(self):
        expected = '+------+-------+---------------+\n| name | value | serial_number |\n+------+-------+---------------+\n| a    | 1.0   | 1             |\n| b    | 2.0   | 2             |\n+------+-------+---------------+'
        with patch('builtins.print') as mocked_print:
            data = {'products': [{'name': 'a', 'value': 1.0, 'serial_number': '1'}, {'name': 'b', 'value': 2.0, 'serial_number': '2'}]}
            app.print_products(data)
            mocked_print.assert_called_with(expected)