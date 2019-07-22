from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected = '----------------------\n currency conversion \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header('currency conversion')
            mocked_print.assert_called_with(expected)

    def test_get_euros_exchanging(self):

        expected_input_text = f'How may euros are you exchanging?: '
        expected_euros = 81

        with patch('builtins.input', return_value='81') as mocked_input:
            euros = app.get_euros_exchanging()
            mocked_input.assert_called_with(expected_input_text)
            self.assertEqual(euros, expected_euros)

    def test_get_exchange_rate(self):

        expected_input_text = f'What is the exchange rate?: '
        expected_exchange_rate = 137.51

        with patch('builtins.input', return_value=str(expected_exchange_rate)) as mocked_input:
            exchange_rate = app.get_exchange_rate()
            mocked_input.assert_called_with(expected_input_text)
            self.assertEqual(exchange_rate, expected_exchange_rate)

    def test_print_rate(self):
        euros = 81
        rate = 137.51
        expected = f'{euros} euros at exchange rage of {rate}'
        with patch('builtins.print') as mocked_print:
            app.print_rate(euros, rate)
            mocked_print.assert_called_with(expected)


    def test_print_rate(self):
        dollars = 111.83
        expected = f'{dollars} US dollars'
        with patch('builtins.print') as mocked_print:
            app.print_dollars(dollars)
            mocked_print.assert_called_with(expected)