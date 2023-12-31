import unittest

from ext import find_extension

class TestFindExtension(unittest.TestCase):
    def test_existed(self):
        actual = find_extension('/path/to/main.py')
        self.assertEqual(actual, 'python')
        
    def test_not_exist(self):
        actual = find_extension('/path/to/some.notexisted')
        self.assertEqual(actual, 'NONE')
        
# import os

# EXTENSION_MAP = {
#     'py': 'python',
#     'md': 'markdown',
#     'markdown': 'markdown',
# }


# def find_extension(filepath):
#     """ ファイルへのパス filepath (/foo/bar/path.py など) を受け取り拡張子のファイルの種類を返す
#     見つからない場合は `"NONE"` という文字列で返す
#     """
#     path, ext = os.path.splitext(filepath)
#     return EXTENSION_MAP.get(ext.lstrip('.'), 'NONE')
