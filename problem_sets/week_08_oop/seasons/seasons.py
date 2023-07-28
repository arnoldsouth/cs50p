# Import necessary libraries
from datetime import date
import inflect
import sys
import operator

# Create an inflect engine to convert numbers to words
p = inflect.engine()


# Main function that executes the entire program
def main():
    # Get the user's date of birth (DOB) from the user
    dob = get_user_dob()

    # Get the current date
    current_date = get_current_date()

    # Calculate the difference between the current date and the DOB
    difference = calculate_difference(current_date, dob)

    # Convert the difference (in minutes) to words
    minutes_as_words = convert_to_words(difference)

    # Print the result
    print(f"{minutes_as_words} minutes")


# Function to get the user's date of birth (DOB)
def get_user_dob():
    try:
        dob = input("Date of Birth: ")  # Prompt the user to enter their DOB
        return date.fromisoformat(dob)  # Convert the input string to a date object

    except ValueError:
        sys.exit(
            "Invalid date"
        )  # If the input is not in the correct format, exit the program with an error message


# Function to get the current date
def get_current_date():
    return date.today()  # Return the current date as a date object


# Function to calculate the difference between two dates (current date and DOB)
def calculate_difference(current_date, dob):
    return operator.sub(
        current_date, dob
    )  # Return the difference between the two dates


# Function to convert minutes to words using inflect engine
def convert_to_words(difference):
    minutes_as_integer = difference.days * 24 * 60  # Convert the difference to minutes
    minutes_as_words = p.number_to_words(
        minutes_as_integer, andword=""
    ).capitalize()  # Convert minutes to words
    return minutes_as_words  # Return the result


if __name__ == "__main__":
    main()
