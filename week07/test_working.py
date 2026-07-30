import pytest
from working import convert


def test_am():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 4 PM") == "10:00 to 16:00"


def test_pm():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_noon_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM.")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
