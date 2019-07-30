from unittest import TestCase
from unittest.mock import patch, call
import app

class AppTest(TestCase):

    def test_print_header(self):
        
        expected = '----------------------\n Karvonen heart rate \n----------------------\n'
        with patch('builtins.print') as mocked_print:
            app.print_header()
            mocked_print.assert_called_with(expected)

    def test_print_headings(self):
        
        expected = 'Intensity   | Rate \n------------|------'
        with patch('builtins.print') as mocked_print:
            app.print_headings()
            mocked_print.assert_called_with(expected)

    def test_resting_heart_rate(self):

        expected = 'Resting pulse: '
        with patch('builtins.input', return_value='65') as mocked_input:
            resting_heart_rate = app.get_resting_heart_rate()
            mocked_input.assert_called_with(expected)
            self.assertEqual(resting_heart_rate, 65)

    def test_get_age(self):
        expected = 'Age: '
        with patch('builtins.input', return_value='22') as mocked_input:
            age = app.get_age()
            mocked_input.assert_called_with(expected)
            self.assertEqual(age, 22)

    def test_print_header(self):
        expected_calls = [
            call('55%         | 138 bpm'),
            call('56%         | 139 bpm'),
            call('57%         | 141 bpm'),
            call('58%         | 142 bpm'),
            call('59%         | 143 bpm'),
            call('60%         | 145 bpm'),
            call('61%         | 146 bpm'),
            call('62%         | 147 bpm'),
            call('63%         | 149 bpm'),
            call('64%         | 150 bpm'),
            call('65%         | 151 bpm'),
            call('66%         | 153 bpm'),
            call('67%         | 154 bpm'),
            call('68%         | 155 bpm'),
            call('69%         | 157 bpm'),
            call('70%         | 158 bpm'),
            call('71%         | 159 bpm'),
            call('72%         | 161 bpm'),
            call('73%         | 162 bpm'),
            call('74%         | 163 bpm'),
            call('75%         | 165 bpm'),
            call('76%         | 166 bpm'),
            call('77%         | 167 bpm'),
            call('78%         | 169 bpm'),
            call('79%         | 170 bpm'),
            call('80%         | 171 bpm'),
            call('81%         | 173 bpm'),
            call('82%         | 174 bpm'),
            call('83%         | 175 bpm'),
            call('84%         | 177 bpm'),
            call('85%         | 178 bpm'),
            call('86%         | 179 bpm'),
            call('87%         | 181 bpm'),
            call('88%         | 182 bpm'),
            call('89%         | 183 bpm'),
            call('90%         | 185 bpm'),
            call('91%         | 186 bpm'),
            call('92%         | 187 bpm'),
            call('93%         | 189 bpm'),
            call('94%         | 190 bpm'),
            call('95%         | 191 bpm')
        ]
        age = 22
        resting_heart_rate = 65
        with patch('builtins.print') as mocked_print:
            app.print_output(age, resting_heart_rate)
            mocked_print.assert_has_calls(expected_calls)
            mocked_print.assert_called_with('95%         | 191 bpm')
