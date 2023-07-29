# Import the Jar class from the jar module and the pytest library
from jar import Jar
import pytest


# Test case: Testing the initialization of a Jar instance
def test_init():
    jar = Jar()  # Create a new instance of the Jar class using the default capacity


# Test case: Testing the string representation of the Jar instance
def test_str():
    jar = Jar()  # Create a new instance of the Jar class using the default capacity

    jar.deposit(1)  # Deposit 1 cookie into the jar
    assert str(jar) == "🍪"  # Assert that the string representation of the jar is "🍪"


# Test case: Testing the deposit method of the Jar instance
def test_deposit():
    jar = Jar()  # Create a new instance of the Jar class using the default capacity

    jar.deposit(3)  # Deposit 3 cookies into the jar
    assert jar.size == 3  # Assert that the current size of the jar is 3

    # Trying to deposit 10 cookies, which exceeds the jar's capacity, should raise a ValueError
    with pytest.raises(ValueError):
        jar.deposit(10)


# Test case: Testing the withdraw method of the Jar instance
def test_withdraw():
    jar = Jar()  # Create a new instance of the Jar class using the default capacity

    jar.deposit(3)  # Deposit 3 cookies into the jar

    jar.withdraw(1)  # Withdraw 1 cookie from the jar
    assert jar.size == 2  # Assert that the current size of the jar is 2

    # Trying to withdraw 5 cookies, which exceeds the number of cookies in the jar, should raise a ValueError
    with pytest.raises(ValueError):
        jar.withdraw(5)
