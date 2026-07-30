from um import count


def test_single_um():
    assert count("um, hi") == 1
    assert count("Hello, um, world") == 1


def test_multiple_um():
    assert count("um, um, hi") == 2
    assert count("Um... what are um regular um expressions?") == 3


def test_no_um():
    assert count("hello world") == 0
    assert count("yummy fruit") == 0
    assert count("umbrella") == 0


def test_case_insensitive():
    assert count("UM, hi") == 1
    assert count("Um, hi") == 1


def test_um_with_punctuation():
    assert count("This is, um... CS50.") == 1
