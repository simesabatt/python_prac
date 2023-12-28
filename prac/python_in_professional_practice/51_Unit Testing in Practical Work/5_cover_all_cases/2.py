import unittest

from smartphone import detect_smartphone_os


class TestDetectSmartPhoneOS(unittest.TestCase):
    def test__ios(self):
        actual = detect_smartphone_os('iPhone9')
        self.assertEqual(actual, 'iOS')
    
    def test__blackberry(self):
        actual = detect_smartphone_os('BlackBerry111')
        self.assertEqual(actual, 'BlackBerry')
    
    def test__android(self):
        actual = detect_smartphone_os('Galaxy')
        self.assertEqual(actual, 'Android')
    
    def test__other(self):
        actual = detect_smartphone_os('sonota')
        self.assertEqual(actual, 'Unknown')

# ANDROID_PREFIXES = (
#     'Nexus',
#     'Galaxy',
#     'Zenfone',
# )


# def detect_smartphone_os(name):
#     """ スマートフォン端末名 name から OS を判定する関数
#     """
#     if name.startswith('iPhone'):
#         return 'iOS'
#     elif name.startswith('BlackBerry'):
#         return 'BlackBerry'

#     for prefix in ANDROID_PREFIXES:
#         if name.startswith(prefix):
#             return 'Android'

#     return 'Unknown'