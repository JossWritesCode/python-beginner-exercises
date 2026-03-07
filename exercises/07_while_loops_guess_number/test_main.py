from .main import attempts_until_guess

def test_attempts_until_guess_found():
    assert attempts_until_guess(5, [1, 2, 5, 9]) == 3
    assert attempts_until_guess(1, [1]) == 1

def test_attempts_until_guess_not_found():
    assert attempts_until_guess(3, [1, 2, 4]) == -1
    assert attempts_until_guess(0, []) == -1
