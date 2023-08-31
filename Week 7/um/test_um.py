from um import count


def test_only_um():
    assert count("um") == 1


def test_um_with_punctuation():
    assert count("um?") == 1


def test_um_in_a_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_um_in_a_word():
    assert count("instrumentation") == 0
    assert count("corynebacterium") == 0


def test_um_case_insensitive():
    assert count("UM, thanks, UM...") == 2
    assert count("CORYNEBACTERIUM") == 0
