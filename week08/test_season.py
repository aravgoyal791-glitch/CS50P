import pytest
from seasons import minutes


def test_valid_date_format():
    # A valid date should return a string ending in "minutes"
    result = minutes("2000-01-01")
    assert isinstance(result, str)
    assert result.endswith("minutes")


def test_valid_date_capitalized():
    # The returned string should start with a capital letter
    result = minutes("1998-06-20")
    assert result[0].isupper()


def test_invalid_format():
    # Wrong format (not YYYY-MM-DD) should trigger sys.exit
    with pytest.raises(SystemExit):
        minutes("January 1, 2000")


def test_invalid_date_value():
    # Invalid date values (month 13, day 45) should trigger sys.exit
    with pytest.raises(SystemExit):
        minutes("2000-13-45")


def test_invalid_separator():
    # Using slashes instead of dashes should also fail
    with pytest.raises(SystemExit):
        minutes("2000/01/01")
