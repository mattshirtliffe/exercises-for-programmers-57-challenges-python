from unittest import TestCase
from unittest.mock import patch
import app

class AppTest(TestCase):

    def test_print_header(self):
        expected_header_text = '-----------\n Mad Libs \n-----------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_once_with(expected_header_text)