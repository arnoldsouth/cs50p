class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance = self._balance + n

    def withdraw(self, n):
        self._balance = self._balance - n


def main():
    account = Account()

    print("Balance:", account.balance)
    account.deposit(100)
    print("Balance after deposit:", account.balance)
    account.withdraw(25)
    print("Balance after withdraw:", account.balance)


if __name__ == "__main__":
    main()


# balance = 0


# def main():
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)


# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n


# if __name__ == "__main__":
#     main()
