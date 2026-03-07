from .main import find_max

def test_find_max():
    assert find_max([1, 5, 2]) == 5
    assert find_max([-10, -3, -20]) == -3
    assert find_max([7]) == 7
