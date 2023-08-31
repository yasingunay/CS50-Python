from working import convert
import pytest


def test_valid_input():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_input_without_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("33:90 AM 35:90 PM")


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("cat")
