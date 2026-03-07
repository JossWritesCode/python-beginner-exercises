from .main import count_up

def test_count_up():
    assert count_up(1) == [1]
    assert count_up(3) == [1, 2, 3]
    assert count_up(5) == [1, 2, 3, 4, 5]
