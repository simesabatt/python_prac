import pytest
from four_color import solve_four_color


@pytest.fixture
def sample_data():
    return 2, [], "RR"


def test_solve_four_color_simple(sample_data):
    n, adj, expected = sample_data
    actual = solve_four_color(n, adj)
    assert actual == expected