from unittest import TestCase
from unittest.mock import patch
from datetime import datetime
import app

class CalcRetirementTest(TestCase):

    def test_get_current_year(self):
        with patch('app.get_now', return_value=datetime(2015, 8, 4, 12, 22, 44, 123456)) as mocked_datetime:
            year = app.get_current_year()
            self.assertEqual(year, 2015)
    
    def test_calc_years_till_retirement(self):
        years_till_retirement = app.calc_years_till_retirement(30, 80)
        self.assertEqual(years_till_retirement, 50)

    def test_calc_retirement_year(self):
        retirement_year = app.calc_retirement_year(2019, 50)
        self.assertEqual(retirement_year, 2069)