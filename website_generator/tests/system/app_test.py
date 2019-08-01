from unittest import TestCase
from unittest.mock import patch, call
import app


class AppTest(TestCase):
    def test_print_header(self):

        expected = '--------------------\n Website generator \n--------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_site_name(self):
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'awesomeco')
            site_name = app.get_site_name()
            mocked_input.assert_called_with('Site name: ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(site_name, 'awesomeco')

    def test_get_author_name(self):
        with patch('builtins.input') as mocked_input, patch(
            'builtins.print'
        ) as mocked_print:
            mocked_input.side_effect = ('', 'Max Power')
            author_name = app.get_author_name()
            mocked_input.assert_called_with('Author: ')
            mocked_print.assert_called_with('A valid input required')
            self.assertEqual(author_name, 'Max Power')

    def test_ask_if_javacript(self):
        expected = False
        expected_input = 'Do you want a folder for JavaScript? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', 'y', 'n')
                answer = app.ask_if_javacript()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
                self.assertTrue(answer)
                answer = app.ask_if_javacript()
                self.assertFalse(answer)

    def test_ask_if_css(self):
        expected = False
        expected_input = 'Do you want a folder for CSS? '
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('', 'y', 'n')
                answer = app.ask_if_css()
                mocked_print.assert_called_with('A valid input is required')
                mocked_input.assert_called_with(expected_input)
                self.assertTrue(answer)
                answer = app.ask_if_css()
                self.assertFalse(answer)

    def test_create_folder(self):
        with patch('os.mkdir') as mocked_os_mkdir:
            app.create_folder('awesomeco')
            mocked_os_mkdir.assert_called_with('awesomeco')

    def test_create_file(self):
        with patch('builtins.open') as mocked_open:
            app.create_file('awesomeco', 'test')
            mocked_open.assert_called_with('awesomeco/index.html', 'w')