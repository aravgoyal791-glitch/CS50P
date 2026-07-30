from response import validate


def test_valid_simple():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("malan@cs50.harvard.edu") == "Valid"


def test_valid_with_symbols():
    assert validate("malan+cs50@harvard.edu") == "Valid"
    assert validate("malan-cs50@harvard.edu") == "Valid"
    assert validate("malan.cs50@harvard.edu") == "Valid"
    assert validate("malan_cs50@harvard.edu") == "Valid"


def test_invalid_missing_username():
    assert validate("@harvard.edu") == "Invalid"


def test_invalid_missing_domain():
    assert validate("malan@") == "Invalid"
    assert validate("malan@harvard") == "Invalid"


def test_invalid_no_at_symbol():
    assert validate("malan.harvard.edu") == "Invalid"


def test_invalid_extra_at_symbol():
    assert validate("malan@@harvard.edu") == "Invalid"
