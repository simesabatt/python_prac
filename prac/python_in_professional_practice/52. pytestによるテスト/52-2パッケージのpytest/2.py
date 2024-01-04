# pytest tests/unit/test_four_color2.py -m simple
# で実行するとマーカーのついたテストのみ実行される


import pytest
from four_color import solve_four_color


@pytest.mark.simple
def test_solve_four_color_simple():
    n, adj, expected = 2, [], "RR"
    actual = solve_four_color(n, adj)
    print(actual)
    assert actual == expected



# def solve_four_color(n, adj):
#     """四色問題を解いて割当を返す

#     :param n: 領域数（領域は0, 1, ..., n - 1）
#     :param adj: 同色を禁止する「領域の組」のリスト
#     :return: 領域ごとの色（RGCY）を表す文字列
#     """
#     res = [0] * n
#     dj = [[] for _ in range(n)]  # 領域ごとの禁止領域リスト
#     for i, j in adj:
#         dj[max(i, j)].append(min(i, j))
#     for i in range(n):
#         res[i] = ({1, 2, 3, 4} - {res[j] for j in dj[i]}).pop()
#     return "".join("RGCY"[i - 1] for i in res)