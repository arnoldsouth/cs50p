# Define a class called Jar to represent a cookie jar
class Jar:
    # Constructor method (__init__) initializes new instance of the class
    def __init__(self, capacity=12):
        # Initialize the attributes of the class
        self.capacity = capacity  # Maximum number of cookies the jar can hold
        self.size = 0  # Current number of cookies in jar, initially set to 0

        # Check if the provided capacity is negative, if yes, raise a ValueError
        if capacity < 0:
            raise ValueError

    # __str__ method returns a string of the Jar instance
    def __str__(self):
        # Each cookie is represented by emoji "🍪" for 'size' times
        return "🍪" * self.size

    # The deposit method adds 'n' cookies to the jar
    def deposit(self, n):
        # Check if adding 'n' cookies would exceed the capacity, if yes, raise a ValueError
        if n + self.size > self.capacity:
            raise ValueError("Deposit error")
        # If it doesn't exceed the capacity, update the size of the jar
        else:
            self.size += n

    # The withdraw method removes 'n' cookies from the jar
    def withdraw(self, n):
        # Check if there are enough cookies to withdraw, if not, raise a ValueError
        if n > self.size:
            raise ValueError("Withdraw error")
        # If there are enough cookies, update the size of the jar
        else:
            self.size -= n

    # The capacity `property` is a getter that returns the value of `_capacity` (private attribute)
    @property
    def capacity(self):
        return self._capacity

    # The `capacity` property is a setter that allows updating the value of `_capacity` (private attribute)
    @capacity.setter
    def capacity(self, capacity):
        # Check if the provided capacity is negative, if yes, raise a ValueError
        if capacity < 0:
            raise ValueError

        # If the capacity is valid, update the private attribute `_capacity`
        self._capacity = capacity

    # The `size` property is a getter that returns the value of `_size` (private attribute)
    @property
    def size(self):
        return self._size

    # The `size` property is a setter that allows updating the value of `_size` (private attribute)
    @size.setter
    def size(self, size):
        # Check if the size exceeds the capacity, if yes, raise a ValueError
        if size > self.capacity:
            raise ValueError

        # If the size is valid, update the private attribute _size
        self._size = size


def main():
    # Create a new instance of the Jar class with the default capacity of 12 from Class
    jar = Jar()

    # Deposit 2 cookies into the jar
    jar.deposit(2)
    print(f"{jar}")  # Print the current state of the jar
    print(f"Current size: {jar.size}")  # Print the current number of cookies in the jar

    # Deposit 5 more cookies into the jar
    jar.deposit(5)
    print(f"{jar}")  # Print the current state of the jar
    print(f"Current size: {jar.size}")  # Print the current number of cookies in the jar

    # Withdraw 6 cookies from the jar
    jar.withdraw(6)
    print(f"{jar}")  # Print the current state of the jar
    print(f"Current size: {jar.size}")  # Print the current number of cookies in the jar

    # Print the maximum capacity of the jar
    print(f"Capacity: {jar.capacity}")


if __name__ == "__main__":
    main()
