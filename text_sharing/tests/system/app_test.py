import os
from unittest import TestCase
from unittest.mock import patch, call
from app import app

import json
from datetime import datetime


class AppTest(TestCase):


    def setUp(self):
        
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['PICKLE_DB'] = 'test.db'
        app.testing = True
        app.debug = False
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        os.remove('test.db')

    def test_home(self):
        with self.app as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)         
            self.assertIn('<h1>Enter Text</h1>',  response.get_data().decode("utf-8") )

    def test_create_text(self):
        with self.app as client:
            response = client.post('/', data={'text': 'Some text'}, follow_redirects=False)
            self.assertEqual(response.status_code, 302)