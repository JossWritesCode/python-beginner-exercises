from .main import bubble_sort

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([2, 2, 1]) == [1, 2, 2]
