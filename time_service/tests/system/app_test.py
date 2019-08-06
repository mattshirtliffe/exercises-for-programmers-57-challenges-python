import os
from unittest import TestCase
from unittest.mock import patch, call
from app import app
import client

import json
from datetime import datetime


class AppTest(TestCase):


    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        with self.app as client, patch('app.get_now', return_value=datetime(2015, 8, 4, 12, 22, 44, 123456)) as mocked_datetime:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()),  {'current_time': 'Tue, 04 Aug 2015 12:22:44 GMT'})

    def test_get_data(self):
        with patch('requests.get') as mocked_request_get:
            mocked_request_get.return_value.status_code = 200
            response = client.get_data()
            self.assertEqual(response.status_code, 200)
            mocked_request_get.assert_called_with(f'http://localhost:5000/')

    
    def test_print_current_time(self):
        with patch('builtins.print') as mocked_print:
            client.print_current_time('Tue, 06 Aug 2019 12:03:47 GMT')
            mocked_print.assert_called_with('The current time is Tue, 06 Aug 2019 12:03:47 GMT')