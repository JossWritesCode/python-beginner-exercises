from pathlib import Path
from .main import count_words, count_words_in_file

def test_count_words():
    assert count_words("hello") == 1
    assert count_words("hello world") == 2
    assert count_words("  lots   of   spaces  ") == 3

def test_count_words_in_file():
    path = Path(__file__).parent / "sample.txt"
    assert count_words_in_file(path) == 7
