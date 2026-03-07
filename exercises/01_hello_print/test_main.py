from .main import say_hello

def test_say_hello_prints(capsys):
    say_hello()
    out = capsys.readouterr().out
    assert out == "Hello, world!\n"
