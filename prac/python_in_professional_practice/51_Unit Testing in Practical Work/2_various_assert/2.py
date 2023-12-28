import unittest

# テスト対象のモジュール
import math


class TestPow(unittest.TestCase):
    def test_pow(self):
        """ 正の整数を正の整数でべき乗
        """
        actual = math.pow(4, 2)
        self.assertEqual(actual, 16)

    def test_negative(self):
        """ 正の整数を負の整数でべき乗
        """
        actual = math.pow(4, -2)
        self.assertEqual(actual, 0.0625)


class TestCeil(unittest.TestCase):
    def test_float(self):
        """ 入力が float の場合
        """
        actual = math.ceil(4.8)
        self.assertEqual(actual, 5)

    def test_int(self):
        """ 入力が int の場合
        """
        actual = math.ceil(4)
        self.assertEqual(actual, 4)


class TestFactorial(unittest.TestCase):
    def test_int(self):
        """ 入力が正の整数の場合
        """
        actual = math.factorial(8)
        self.assertEqual(actual, 40320)

    def test_negative(self):
        """ 入力が負の整数の場合、ValueErrorを送出する
        """
        with self.assertRaises(ValueError):
            math.factorial(-8)




# import inspect
# import sys
# import unittest
# from unittest.mock import MagicMock, Mock


# def check_test(self, smdl, slib, targets, extdirs=None, mintest=None):
#     try:
#         if extdirs:
#             for s in extdirs:
#                 sys.path.append(s)
#         mdl = __import__(smdl)
#         lib = __import__(slib) if slib else mdl
#         flgs = []
#         for cnam, cbdy in inspect.getmembers(mdl, inspect.isclass):
#             if cnam.startswith('Test'):
#                 obj = cbdy()
#                 flgs.append(0)
#                 for fnam, fbdy in inspect.getmembers(obj, inspect.isroutine):
#                     if fnam.startswith('test'):
#                         fbdy()
#                         flgs[-1] += 1
#         if targets:
#             targets_new = []
#             for target in targets:
#                 if not isinstance(target, tuple):
#                     m = Mock()
#                     m._mock_name = target
#                     target = (target, m)
#                 setattr(lib, *target)
#                 targets_new.append(target)
#             for cnam, cbdy in inspect.getmembers(mdl, inspect.isclass):
#                 if cnam.startswith('Test'):
#                     obj = cbdy()
#                     for fnam, fbdy in inspect.getmembers(obj, inspect.isroutine):
#                         if fnam.startswith('test'):
#                             with self.assertRaises(AssertionError,
#                                     msg='テストを見直してください（{}.{}）'.format(cnam, fnam)):  # noqa
#                                 fbdy()  # AssertionErrorを起こす
#             for target in targets_new:
#                 if isinstance(target, tuple) and isinstance(target[1], Mock):
#                     Mock.assert_called(target[1])
#         if not flgs:
#             self.fail('Testで始まるテストクラスにtestで始まるメソッドを作成してください')
#         else:
#             if mintest is None:
#                 mintest = []
#             if len(flgs) < len(mintest):
#                 flgs += [0] * (len(mintest) - len(flgs))
#             elif len(mintest) < len(flgs):
#                 mintest += [1] * (len(flgs) - len(mintest))
#             if not all([i >= j for i, j in zip(flgs, mintest)]):
#                 self.fail('testで始まるメソッドが不足しています')
#     except ImportError:
#         self.assertFalse('プログラムを作成してください。')


# class Test1(unittest.TestCase):
#     def test_it(self):
#         m1 = MagicMock()
#         m1.return_value.__ge__.return_value = False
#         m1.return_value.__lt__.return_value = False
#         m2 = MagicMock()
#         m2.__len__.return_value = 9999
#         targets = ['get_none', ('get_num', m1), ('get_list', m2), 'raise_value_error']
#         check_test(self, 'test_main', None, targets, ['tests'], [1, 1, 1, 1])


# class Test2(unittest.TestCase):
#     def test_it(self):
#         check_test(self, 'test_math', 'math',
#                    ['pow', 'ceil', 'factorial'], ['tests'], [2, 2, 2])