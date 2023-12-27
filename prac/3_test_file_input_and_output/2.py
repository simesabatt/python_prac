import os
import tempfile
import unittest

from dircounter import count_files


class TestCountFiles(unittest.TestCase):
    def test_count(self):
	        with tempfile.TemporaryDirectory() as dirpath:
	            with open(os.path.join(dirpath, 'file1'), mode='w', encoding='utf-8') as f1, \
	                    open(os.path.join(dirpath, 'file2'), mode='w', encoding='utf-8') as f2:
	                actual = count_files(dirpath)
	        self.assertEqual(actual, 2)



# import os


# def count_files(dirpath):
#     """ dirpath にあるディレクトリー内のファイルの総数を返す関数
#     """
#     return len(os.listdir(dirpath))