from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello, Newman") == 0

def test_h():
    assert value("hi") == 20
    assert value("How are you?") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100