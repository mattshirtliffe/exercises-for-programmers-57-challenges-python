import os
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch, call
import app

import pickledb


from string import Template


class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '------------\n Todo List \n------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_get_task(self):
        expected = 'Enter task: '
        with patch('builtins.input', return_value='Pick up some milk') as mocked_input:
            with patch('builtins.print') as mocked_print:
                task = app.get_task()
                mocked_input.assert_called_with(expected)
                self.assertEqual(task, 'Pick up some milk')
    
    def test_store_task(self):
        task = 'Pick up some milk'
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            app.store_task(task)
            mocked_load.assert_called_with('tasks.db', True)
            mock.set.assert_called_with('Pick up some milk', False)

    def test_print_tasks(self):
        expected_calls = [call('Tasks: '), call('go for a walk'), call('Pick up some milk')]
        tasks = {"go for a walk": False, "Pick up some milk": False}
        with patch('builtins.print') as mocked_print:
            app.print_tasks(tasks.keys())
            mocked_print.assert_has_calls(expected_calls)

    def test_get_tasks(self):
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            tasks = app.get_tasks()
            mocked_load.assert_called_with('tasks.db', True)
            mock.getall.assert_called()

    def test_delete_task(self):
        task = 'Pick up some milk'
        with patch('pickledb.load') as mocked_load:
            mock = MagicMock()
            mocked_load.return_value = mock
            app.delete_task(task)
            mocked_load.assert_called_with('tasks.db', True)
            mock.exists.assert_called()
            mock.rem.assert_called_with(task)