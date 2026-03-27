from .main import get_first_n

def test_get_first_n():
    assert get_first_n([1, 2, 3, 4], 2) == [1, 2]
    assert get_first_n([1, 2], 5) == [1, 2]
    assert get_first_n([], 3) == []
    assert get_first_n([1, 2, 3], 0) == []
