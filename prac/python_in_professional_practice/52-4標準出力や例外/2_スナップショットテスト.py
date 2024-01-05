from four_color import print_result


def test_print_result(capsys, snapshot):
    print_result("RRG")
    out, _ = capsys.readouterr()
    snapshot.assert_match(out)


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


# def print_result(assigns):
#     """結果の表示

#     :param assigns: 割当
#     """
#     for i, assign in enumerate(assigns):
#         print(f"{i}:{assign}")
