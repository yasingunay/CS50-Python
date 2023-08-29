from bank import value


def test_lower_hello():
    assert value("hello") == 0


def test_upper_hello():
    assert value("Hello") == 0


def test_hello_and_output():
    assert value("Hello, Newman") == 0


def test_only_h():
    assert value("How you doing?") == 20


def test_not_h_or_hello():
    assert value("What's happening?") == 100


def test_empty_str():
    assert value("") == 100


def test_numbers():
    assert value("123Hello") == 100


def test_punctuation_marks():
    assert value("?123Hello") == 100
    assert value("/123Hello?") == 100


def test_whitespace_characters():
    assert value(" 123Hello") == 100
    assert value("          123Hello") == 100
    assert value("\n123Hello") == 100
