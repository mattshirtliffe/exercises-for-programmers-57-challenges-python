from unittest import TestCase
import app

class EmployeeListTest(TestCase):

    def test_remove_employee(self):
        expected = ['John Smith','Jakie Jackson','Amanda Cullen','Jeremy Goodwin']
        app.remove_employee('Chris Jones')
        self.assertListEqual(app.employees, expected)