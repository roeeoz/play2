from greetlib.greet import farewell


def test_default_farewell():
    assert farewell() == "goodbye, world"


def test_named_farewell():
    assert farewell("Ada") == "goodbye, Ada"


def test_blank_name_falls_back():
    assert farewell("  ") == "goodbye, world"


def test_empty_name_falls_back():
    assert farewell("") == "goodbye, world"


def test_name_is_stripped():
    assert farewell("  Ada  ") == "goodbye, Ada"
    assert farewell("\tAda\n") == "goodbye, Ada"
