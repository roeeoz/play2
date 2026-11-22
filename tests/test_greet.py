from greetlib import greet
from greetlib.greet import main


def test_default_greeting():
    assert greet() == "hello, world"


def test_named_greeting():
    assert greet("ada") == "hello, ada"


def test_blank_name_falls_back():
    assert greet("  ") == "hello, world"


def test_cli_prints_greeting(capsys):
    assert main(["bob"]) == 0
    assert capsys.readouterr().out == "hello, bob\n"
