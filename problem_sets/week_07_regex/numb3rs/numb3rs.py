import re


def main():
    # Prompt the user to enter an IPv4 address and remove any leading/trailing whitespace from the input
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        # Regular expression pattern to match each segment of the IPv4 address (0-255)
        pattern = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"

        # Combine the pattern four times to match a complete IPv4 address (X.X.X.X format)
        # The '^' at the beginning and '$' at the end ensure that the entire string is matched
        matches = re.search(
            r"^" + pattern + "\." + pattern + "\." + pattern + "\." + pattern + "$", ip
        )

        # Check if the regex pattern matches the input IPv4 address
        if matches:
            return True  # The IPv4 address is valid
        else:
            return False  # The IPv4 address is invalid

    except ValueError:
        return False  # An exception occurred, so the input is considered invalid


if __name__ == "__main__":
    main()
