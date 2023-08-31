from numb3rs import validate


def test_min_max():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True


def test_invalid_ip():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("75.456.76.65") == False


def test_invalid_input():
    assert validate("cat") == False
