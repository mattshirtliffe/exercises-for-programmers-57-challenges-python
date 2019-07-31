from unittest import TestCase
import app

class SortingRecordsTest(TestCase):
    
    def test_sort_users(self):

        expected = [
            {'first_name':'John', 'last_name':'Johnson', 'position':'Manager', 'separation_date':'2016-12-31'},
            {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'},
            {'first_name':'Michaela', 'last_name':'Michaelson', 'position':'District Manage', 'separation_date':'2015-12-19'},
            {'first_name':'Jake', 'last_name':'Jacobson', 'position':'Programmer', 'separation_date':''},
            {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''},
            {'first_name':'Sally', 'last_name':'Weber', 'position':'Web Developer', 'separation_date':'2015-12-18'}
        ]

        app.users = app.sort_users()
        self.assertDictEqual(app.users[-1], {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'})
        self.assertDictEqual(app.users[0], {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''})