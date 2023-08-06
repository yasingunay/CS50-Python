import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(3)
    assert jar.capacity == 3

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(9)
    assert jar.size == 12

    with pytest.raises(ValueError) as e:
        jar.deposit(100)
        assert str(e.value) == "Max number of cookies reached"

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(3)
    assert jar.size == 9
    jar.withdraw(8)
    assert jar.size == 1

    with pytest.raises(ValueError) as e:
        jar.withdraw(100)
        assert str(e.value) == "Not enough cookies"