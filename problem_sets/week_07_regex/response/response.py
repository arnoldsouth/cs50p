import validators


def main():
    validation_result = get_validation()

    print(validation_result)


def get_validation():
    email = input("What's your email address? ")

    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
