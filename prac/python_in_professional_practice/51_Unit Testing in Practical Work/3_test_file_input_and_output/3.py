import tempfile
import unittest

from agg import parse_ltsv, agg_ltsv_file


class TestParseLTSV(unittest.TestCase):
    def test_parse(self):
        actual = parse_ltsv('level:INFO\tmessage:メッセージ\tcreated_at:14000000')
        self.assertEqual(actual, {
            'level': 'INFO',
            'message': 'メッセージ',
            'created_at': '14000000',
        })


class TestAggLTSVFile(unittest.TestCase):
    def test_aggregate(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""level:INFO\tmessage:msg1
level:INFO\tmessage:msg2
level:ERROR\tmessage:error
""")
            f.flush()
            actual = agg_ltsv_file(f.name, 'level')
        self.assertEqual(actual, {
            'INFO': 2,
            'ERROR': 1,
        })


# def parse_ltsv(row):
#     """ LTSV形式の文字列 row を辞書に変換して返す

#     ## LTSV:

#     "キー:値<タブ>キー:値<タブ>..." というように、キー、値がコロンで区切られていて、
#     データ同士がタブで区切られている。
#     Pythonで書くとこんなかんじ "level:INFO\tmessage:メッセージ\t..."

#     仕様: http://ltsv.org/
#     """
#     return dict(d.split(':', 1) for d in row.split('\t'))


# def agg_ltsv_file(filepath, count_key):
#     """
#     LTSVのファイル filepath を読み込んで、キーごとに集計して返す。

#     ファイル内のデータが下の場合

#     level:INFO<タブ>message:msg1
#     level:INFO<タブ>message:msg2
#     level:ERROR<タブ>message:error
#     level:ERROR<タブ>message:error

#     count_key が 'level' であれば {'INFO': 2, 'ERROR': 2}
#     count_key が 'message' であれば {'msg1': 1, 'msg2': 1, 'error': 2}
#     が返る
#     """
#     agged = {}
#     with open(filepath, encoding='utf-8') as f:
#         for row in f:
#             data = parse_ltsv(row.strip())
#             key = data[count_key]
#             if key in agged:
#                 agged[key] += 1
#             else:
#                 agged[key] = 1
#     return agged