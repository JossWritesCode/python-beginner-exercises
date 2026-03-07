from .main import sum_list, average_list

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([10]) == 10

def test_average_list():
    assert average_list([1, 2, 3]) == 2
    assert average_list([10, 20]) == 15
