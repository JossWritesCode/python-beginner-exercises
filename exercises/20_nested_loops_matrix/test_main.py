from .main import make_matrix

def test_make_matrix():
    assert make_matrix(1, 1) == [[1]]
    assert make_matrix(2, 3) == [[1,2,3],[4,5,6]]
