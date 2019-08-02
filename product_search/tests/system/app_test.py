from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '-----------------\n Product search \n-----------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_products_from_file(self):
        expected = {
            'products':[
                {
                    'name':'Widget',
                    'price':25.00,
                    'quantity':5
                },
                {
                    'name':'Thing',
                    'price':15.00,
                    'quantity':5
                },
                {
                    'name':'Doodad',
                    'price':5.00,
                    'quantity':10
                }
            ]
        }
        product_json = app.get_products_from_file()
        self.assertDictEqual(product_json, expected)

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


    def test_get_product_from_products(self):
        
        expected_product =  {
                    'name':'Widget',
                    'price':25.00,
                    'quantity':5
                }
        products = {
            'products':[
                {
                    'name':'Widget',
                    'price':25.00,
                    'quantity':5
                },
                {
                    'name':'Thing',
                    'price':15.00,
                    'quantity':5
                },
                {
                    'name':'Doodad',
                    'price':5.00,
                    'quantity':10
                }
            ]
        }
        product = app.get_product_from_products('Widget', products['products'])
        self.assertDictEqual(product, expected_product)

        product = app.get_product_from_products('iPad', products['products'])
        self.assertIsNone(product)

    def test_print_product(self):
        product = {
                    'name':'Widget',
                    'price':25.00,
                    'quantity':5
                }
        expected_calls = [call('Name: Widget'), call('Name: 25.0'), call('Name: 5')]
        with patch('builtins.print') as mocked_print:
            app.print_product(product)
            mocked_print.assert_has_calls(expected_calls)