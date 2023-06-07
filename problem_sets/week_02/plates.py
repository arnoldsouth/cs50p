# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “All vanity plates must start with at least two letters.”
    if not s[0:2].isalpha():
        return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    # aka check whether the second to last char in the string is a number, and if it is, then the last char in the string cannot be a letter

    # Initialize variable `contains_digit` starting as False. Then iterates over the rest of the characters (after 2 chars since first 2 cannot be digits is already checked above) 1) first checking whether a char isn't isalpha or isnum (aka punctuation, space, etc), and 2) and for every character after, if it finds a letter, it returns False because letter should not follow a digit
    contains_digit = False
    for char in s[2:]:
        # “No periods, spaces, or punctuation marks are allowed.”
        if not char.isalnum():
            return False
        if char.isdigit():
            contains_digit = True
        elif contains_digit:
            return False

    # Checks if the first digit after the first 2 chars is 0
    if s[2] == "0":
        return False

    return True


main()


# def is_valid(s):
#     # Check the length of the vanity plate
#     if len(s) < 2 or len(s) > 6:
#         return False
#     # Check if the first two characters are letters
#     if not s[0:2].isalpha():
#         return False
#     # Check if any characters after the first two are not digits,
#     # or if any characters are not alphanumeric
#     has_digit = False
#     for ch in s[2:]:
#         if not ch.isalnum():
#             return False
#         if ch.isdigit():
#             has_digit = True
#         elif has_digit:
#             # If a letter is found after a digit, it's invalid
#             return False
#     # Check if the first digit is 0
#     if len(s) > 2 and s[2] == '0':
#         return False
#     return True
