def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the string is between 2 and 6 characters and if it contains only alphanumeric characters (letters and digits)
    if not (2 <= len(s) <= 6 and s.isalnum()):
        return False
    # Check if the string contains only alphabetic characters
    if s.isalpha():
        return True

    # Check if the string starts with two alphabetic characters and ends with two numeric characters
    if not (s[:2].isalpha() and s[-2:].isdigit()):
        return False

    # Check the string for specific conditions related to digits and alphabetic characters
    for i in range(len(s)):
        if s[i].isdigit():
            # Check if a digit starts with "0" or if the rest of the string contains alphabetic characters
            if s[i].startswith("0") or s[i:].isalpha():
                return False
            else:
                return True

    # If none of the previous conditions are met, return False
    return False


if __name__ == "__main__":
    main()
