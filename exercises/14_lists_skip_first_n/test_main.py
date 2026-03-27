from .main import skip_first_n

def test_skip_first_n():
    assert skip_first_n([1, 2, 3, 4], 2) == [3, 4]
    assert skip_first_n([1, 2], 5) == []
    assert skip_first_n([], 3) == []
    assert skip_first_n([1, 2, 3], 0) == [1, 2, 3]
