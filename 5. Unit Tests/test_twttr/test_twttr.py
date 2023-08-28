from twttr import shorten


def test_lower_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("yasin") == "ysn"


def test_upper_vowels():
    assert shorten("DAVID") == "DVD"
    assert shorten("YASIN") == "YSN"


def test_lower_and_upper_vowels():
    assert shorten("DaVID") == "DVD"
    assert shorten("YASiN") == "YSN"


def test_no_vowels():
    assert shorten("twttr") == "twttr"
    assert shorten("YSNGNY") == "YSNGNY"


def test_only_numbers():
    assert shorten("0123456") == "0123456"
    assert shorten("Ya123sin") == "Y123sn"


def test_punctuation_marks():
    assert shorten("?YaSin?") == "?YSn?"
    assert shorten("/DAVID!") == "/DVD!"


def test_empyty_str():
    assert shorten("") == ""


def test_space():
    assert shorten(" ") == " "
