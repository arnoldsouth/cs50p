import re  # import the Python regex module


# This is the main function that is executed when the program starts
def main():
    # The function first prompts the user for input, then passes this input to the `convert` function.
    # The result from `convert` is then printed to the console.
    print(convert(input("Hours: ")))


# This is a function that converts a time range in 12-hour AM/PM format to 24-hour format
def convert(s):
    # This regex pattern matches a time range in 12-hour AM/PM format. It allows optional spaces between the numbers and symbols.
    # The time range should start with 1 or 2 digits (for the hours), optionally followed by a colon and 2 digits (for the minutes), followed by either "AM" or "PM".
    # Then, there should be a "to" before the second time. The second time follows the same pattern as the first.
    pattern = r"^\s*(\d{1,2})\s*(?::\s*(\d{2}))?\s* (AM|PM)\s*to\s*(\d{1,2})\s*(?::\s*(\d{2}))?\s* (AM|PM)\s*$"

    # We use the `re.search` function to match the input string `s` against the regex pattern.
    matches = re.search(pattern, s, re.IGNORECASE)

    # If no match is found, the input format is invalid, so we raise a ValueError.
    if not matches:
        raise ValueError("Invalid time format inputted")

    # If a match is found, we extract the start hours, start minutes, start AM/PM, end hours, end minutes, and end AM/PM from the match.
    start_hr, start_min, start_ampm, end_hr, end_min, end_ampm = matches.groups()

    # We convert the start and end hours and minutes to integers. If the minutes are not given, we assume they are 0.
    start_hr = int(start_hr)
    start_min = int(start_min) if start_min else 0
    end_hr = int(end_hr)
    end_min = int(end_min) if end_min else 0

    # We validate the hours and minutes. If any of them are outside their valid range, we raise a ValueError.
    if (
        not (1 <= start_hr <= 12)
        or not (0 <= start_min <= 59)
        or not (1 <= end_hr <= 12)
        or not (0 <= end_min <= 59)
    ):
        raise ValueError("Invalid hour/minute inputted")

    # We convert the start and end hours from 12-hour format to 24-hour format.
    if start_ampm == "PM" and start_hr != 12:
        start_hr = start_hr + 12
    elif start_ampm == "AM" and start_hr == 12:
        start_hr = 0

    if end_ampm == "PM" and end_hr != 12:
        end_hr = end_hr + 12
    elif end_ampm == "AM" and end_hr == 12:
        end_hr = 0

    # We return the converted time range in 24-hour format.
    return f"{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}"


# This line ensures that `main` is called when the script is executed directly, but not when it's imported as a module.
if __name__ == "__main__":
    main()
