from datetime import datetime
import unittest
from unittest import mock

from daterange import now_to


class TestNowTo(unittest.TestCase):
    @mock.patch('daterange.get_now')
    def test_per_an_hour(self, m):
        m.return_value = datetime(2000, 11, 5, 23, 0, 0)

        g = now_to()
        self.assertEqual(next(g), datetime(2000, 11, 5, 23, 0, 0))
        self.assertEqual(next(g), datetime(2000, 11, 6, 0, 0, 0))
        self.assertEqual(next(g), datetime(2000, 11, 6, 1, 0, 0))

    @mock.patch('daterange.get_now')
    def test_per_4hours(self, m):
        m.return_value = datetime(2000, 11, 5, 23, 0, 0)

        g = now_to(4)
        self.assertEqual(next(g), datetime(2000, 11, 5, 23, 0, 0))
        self.assertEqual(next(g), datetime(2000, 11, 6, 3, 0, 0))
        self.assertEqual(next(g), datetime(2000, 11, 6, 7, 0, 0))




# from datetime import datetime, timedelta


# def get_now():
#     return datetime.now()


# def now_to(hours=1):
#     """ 現在時刻から後の時刻を1時間刻みに返すジェネレーター。時間は hours に指定できる。

#     >>> g = now_to()
#     >>> next(g)
#     datetime(2015, 8, 1, 12, 32, 00)
#     >>> next(g)
#     datetime(2015, 8, 1, 13, 32, 00)
#     >>> next(g)
#     datetime(2015, 8, 1, 14, 32, 00)
#     ...
#     """
#     now = get_now()
#     while True:
#         yield now
#         now += timedelta(hours=hours)
