from plates import is_valid


def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("A") == False
    assert is_valid("OUTATIME") == False


def test_first_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False
    assert is_valid("12ABC") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True


def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_symbols():
    assert is_valid("PI3.14") == False
    assert is_valid("HEL LO") == False
    assert is_valid("CS-50") == False