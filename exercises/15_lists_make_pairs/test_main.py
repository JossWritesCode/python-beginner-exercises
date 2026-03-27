from .main import make_pairs

def test_make_pairs():
    assert make_pairs([1, 2, 3, 4]) == [[1, 2], [3, 4]]
    assert make_pairs([1, 2, 3, 4, 5]) == [[1, 2], [3, 4], [5]]
    assert make_pairs([]) == []
