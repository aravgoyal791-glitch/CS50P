from numb3rs import validate


def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True


def test_invalid_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("300.300.300.300") == False


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat") == False
    assert validate("1.1.1.11111") == False


def test_invalid_leading_zeros():
    assert validate("000.001.010.100") == False
    assert validate("01.1.1.1") == False


def test_ipv6():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
