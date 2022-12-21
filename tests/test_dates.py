import sys
sys.path.append('..')
import pydates.dates as dates

import unittest
import datetime




class Test(unittest.TestCase):

    def test_parse_date(self):
        #Check return type
        self.assertIsInstance(dates.parse_date('04/05/22'), datetime.datetime)
        #Check returns for different formats
        self.assertEquals(str(dates.parse_date('04/05/22')), '2022-05-04 00:00:00')
        self.assertEquals(str(dates.parse_date('4th May 2022')), '2022-05-04 00:00:00')

    def test_format_datetime_to_str(self):
        input = dates.format_datetime_to_str(datetime.datetime(2022, 5, 4, 0, 0, 0))
        self.assertIsInstance(input , str)
        self.assertEquals(input, '2022-05-04 00:00 AM')

    def test_now(self):
        self.assertIsInstance(dates.now(), datetime.datetime)

    def test_relative_datetime(self):
        initial_date = datetime.datetime(2022, 5, 4, 0, 0, 0)
        self.assertEquals(dates.relative_datetime(initial_date, delta_year=1, delta_month=1, delta_day=1, delta_hour=1, delta_minute=1, delta_second=1), datetime.datetime(2023, 6, 5, 1, 1, 1))





