import unittest

from main import myabs


class TestAbs(unittest.TestCase):
    def test__positive(self):
        self.assertEqual(myabs(4), 4)

    def test__negative(self):
        self.assertEqual(myabs(-4), 4)

# def myabs(num):
#     """ 絶対値を計算する関数
#     num がゼロ以上の整数はそのまま返す。負の整数は正にして返す。
#     """
#     if num >= 0:
#         return num
#     else:
#         return -num