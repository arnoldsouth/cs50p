def main():
    # Prompt the user to enter a fraction in X/Y format and store it in 'fractn' variable.
    fractn = input("Fraction: ")
    # Convert the fraction to a percentage using the 'convert()' function and store the result in 'percntg' variable.
    percntg = convert(fractn)
    # Determine the gauge value based on the percentage using the 'gauge()' function and print the result.
    print(gauge(percntg))


def convert(fraction):
    try:
        # Split the fraction string into X and Y parts using '/' as the delimiter and convert them to integers.
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        # Calculate the percentage by dividing X by Y and then multiplying by 100. Return the rounded percentage.
        return round(x / y * 100)

    except ValueError:
        # If the conversion to integers or the calculation of percentage raises a ValueError, raise it again to be handled in 'main()'.
        raise ValueError("Invalid input. Both X and Y must be integers.")
    except ZeroDivisionError:
        # If the calculation involves division by zero, raise a ZeroDivisionError to be handled in 'main()'.
        raise ZeroDivisionError("ZeroDivisionError. Y cannot be zero.")


def gauge(percentage):
    # Determine the gauge value based on the percentage.
    if percentage <= 1:
        return "E"  # Return "E" if the percentage is less than or equal to 1.
    elif percentage >= 99:
        return "F"  # Return "F" if the percentage is greater than or equal to 99.
    else:
        return f"{percentage}%"  # Return the percentage followed by a percentage sign otherwise.


if __name__ == "__main__":
    main()
