from .main import are_anagrams

def test_are_anagrams():
    assert are_anagrams("abc", "cba") is True
    assert are_anagrams("aab", "aba") is True
    assert are_anagrams("aab", "abb") is False
    assert are_anagrams("abc", "ab") is False
