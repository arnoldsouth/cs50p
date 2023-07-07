# This code is a Python script that expects one command-line argument, the name or path of a Python file. It then checks if the provided argument is valid (exists, ends with '.py', and not too many or too few arguments) and calculates the number of lines of code in that file (excluding comments and blank lines) using the count_lines function. If the conditions are not met, the program exits with an appropriate error message using sys.exit().

import sys


# The main function to handle command-line arguments and call the count_lines function.
def main():
    # Check if there are too few command-line arguments.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Check if there are too many command-line arguments.
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if the provided command-line argument is not a Python file.
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        # If the argument is valid, print the number of lines of code in the file.
        print(count_lines(sys.argv[1]))


# Function to count the number of lines of code in the file.
def count_lines(file_name):
    try:
        lines_of_code = 0

        # Open the file in read mode.
        with open(file_name, "r") as file:
            # Iterate through each line in the file.
            for line in file:
                line = line.strip()

                # Check if the line is not a comment or a blank line, and increment the counter.
                if not (line.startswith("#") or line == ""):
                    lines_of_code += 1

            return lines_of_code

    except FileNotFoundError:
        sys.exit("File does not exist")


# Check if this script is being run as the main program.
if __name__ == "__main__":
    # Call the main function to start the program.
    main()
