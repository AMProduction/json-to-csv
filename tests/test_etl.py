import unittest

from bets_etl import _get_year_week_number_month_day_from_string, _parse_and_save_date


class TestETLtool(unittest.TestCase):

    def test_parse_string(self):
        self.assertEqual(_get_year_week_number_month_day_from_string('2021-10-04 18:56:52'), (2021, 40, 10, 4))
        self.assertEqual(_get_year_week_number_month_day_from_string('wrong formatted string'), ("", "", "", ""))

    def test_parse_and_add(self):
        dict_with_datetime = {
            "bet_dt": "2021-10-04 18:56:52",
            "test_key": "test_value"
        }
        expected_dict_with_datetime = {
            "bet_dt": "2021-10-04 18:56:52",
            "test_key": "test_value",
            "bet_year": 2021,
            "bet_week": 40,
            "bet_month": 10,
            "bet_day": 4
        }
        self.assertEqual(_parse_and_save_date(dict_with_datetime), expected_dict_with_datetime)


if __name__ == '__main__':
    unittest.main()
