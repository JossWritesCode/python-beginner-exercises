from .main import letter_grade

def test_letter_grade_boundaries():
    assert letter_grade(100) == "A"
    assert letter_grade(90) == "A"
    assert letter_grade(89) == "B"
    assert letter_grade(80) == "B"
    assert letter_grade(79) == "C"
    assert letter_grade(70) == "C"
    assert letter_grade(69) == "D"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "F"
    assert letter_grade(0) == "F"
