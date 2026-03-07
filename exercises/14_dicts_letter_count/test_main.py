from .main import letter_count

def test_letter_count():
    assert letter_count("aba") == {"a": 2, "b": 1}
    assert letter_count("") == {}
    assert letter_count("  ") == {" ": 2}
