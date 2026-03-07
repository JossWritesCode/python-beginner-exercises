from .main import to_int

def test_to_int():
    assert to_int("7") == 7
    assert to_int("0") == 0
    assert to_int("42") == 42
