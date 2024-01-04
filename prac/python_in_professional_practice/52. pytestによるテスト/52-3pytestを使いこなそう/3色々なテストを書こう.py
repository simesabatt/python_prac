import pytest

from four_color import solve_four_color


params = [
    (3, [[0, 1], [1, 2]], "RGR"),
    (4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], "RGCC"),
    (4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]], "RGCY"),
]


@pytest.mark.parametrize("n, adj, expected", params)
def test_solve_four_color(n, adj, expected):
    actual = solve_four_color(n, adj)
    assert actual == expected
