def main():
    x = int(input("What's X? "))
    print("X squared is", square(x))


def square(n):
    squared = n * n
    return squared


if __name__ == "__main__":
    main()
