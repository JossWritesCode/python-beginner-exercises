from .main import add_tax

def test_add_tax():
    assert add_tax(10, 0.13) == 11.3
    assert add_tax(0, 0.13) == 0
    assert add_tax(100, 0.0) == 100
