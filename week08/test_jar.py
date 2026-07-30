import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

    jar2 = Jar(5)
    assert jar2.size == 0
    assert jar2.capacity == 5

    # Negative or non-int capacity should raise ValueError
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("not a number")


def test_str():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(4)
    assert jar.size == 4

    jar.deposit(6)
    assert jar.size == 10

    # Depositing beyond capacity should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    # Withdrawing more than what's in the jar should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(1)
