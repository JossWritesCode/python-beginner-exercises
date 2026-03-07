from .main import area_of_rectangle

def test_area_of_rectangle():
    assert area_of_rectangle(3, 4) == 12
    assert area_of_rectangle(5, 2) == 10
    assert area_of_rectangle(0, 10) == 0
