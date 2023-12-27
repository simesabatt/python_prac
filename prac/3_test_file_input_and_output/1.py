import tempfile
import unittest

from counter import count_file_lines


class TestCountFileLines(unittest.TestCase):
    def test_count(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""one
two
three
four
""")
            f.flush()
            actual = count_file_lines(f.name)
        self.assertEqual(actual, 4)


# def count_file_lines(filepath):
#     """ filepath にあるファイルの行数を返す関数
#     """
#     with open(filepath, encoding='utf-8') as read_f:
#         num_lines = len(read_f.readlines())
#         return num_lines