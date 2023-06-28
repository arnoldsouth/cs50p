def main():
    greeting = input("Greeting: ")
    result = value(greeting)

    print(f"${result}")


def value(greeting):
    greeting_stripped_lowercase = greeting.strip().lower()

    if greeting_stripped_lowercase.startswith("hello"):
        return 0
    elif greeting_stripped_lowercase.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
