import unittest

from main import get_none, get_num, get_list, raise_value_error

class TestGetNone(unittest.TestCase):
    def test_get(self):
        self.assertIsNone(get_none())

class TestGetNum(unittest.TestCase):
    def test_get(self):
        actual = get_num()
        # 0-9の整数が返るので、その範囲でだけテストをする
        self.assertGreaterEqual(actual, 0)
        self.assertLess(actual, 10)

class TestGetList(unittest.TestCase):
    def test_get(self):
        actual = get_list()
        self.assertEqual(len(actual), 5) # 長さは5
        self.assertIn(0, actual) # 0は必ず含む
        # 返った数のリストを集合にすると、候補の数の部分集合になる
        # リストの最大長が5なので候補の集合と同値にはならない
        self.assertLess(set(actual), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

class TestRaiseValueError(unittest.TestCase):
    def test_raise(self):
        with self.assertRaises(ValueError):
            raise_value_error()

# よく使うassertメソッドは、以下のようになります。

# assertEqual: == かどうか
# assertIsNone: is None かどうか
# assertTrue: 真かどうか
# assertFalse: 偽かどうか
# assertGreater: > かどうか
# assertLess: < かどうか
# assertGreaterEqual: >= かどうか
# assertLessEqual: <= かどうか
# assertIn: ... in ... かどうか
# assertNotIn: ... not in ... かどうか
# assertRaises: with 内で例外をあげるか
# https://docs.python.org/ja/3/library/unittest.html#unittest.TestCase.assertEqual

# import random


# def get_none():
#     """ Noneを返す
#     """
#     return None


# def get_num():
#     """ 0 - 9 の整数を返す
#     """
#     return random.randint(0, 9)


# def get_list():
#     """ 長さが5の、1 - 9 のランダムな値を含むリストを返す。ただし 0 は必ず含む
#     """
#     candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     return [random.choice(candidates) for _ in range(4)] + [0]


def raise_value_error():
    raise ValueError