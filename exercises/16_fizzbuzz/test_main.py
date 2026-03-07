from .main import fizzbuzz

def test_fizzbuzz_15():
    result = fizzbuzz(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    assert len(result) == 15
