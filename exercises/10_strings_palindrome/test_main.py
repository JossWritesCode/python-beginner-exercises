from .main import is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("abc") is False
    assert is_palindrome("") is True
    assert is_palindrome("Aba") is False
