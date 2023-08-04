# https://cs50.harvard.edu/python/2022/notes/9/#map


def main():
    yell("This", "is", "CS50")


def yell(*words):
    # str.upper is a function argument, not called here
    # uppercased = map(str.upper, words)

    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
