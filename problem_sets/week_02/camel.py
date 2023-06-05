# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


def main():
    # Get user input for variable name in camelCase and assign it to `camel_case`
    camel_case = input("camelCase: ")
    # Convert the user input from camel case to snake case
    snake_case = convert_to_snake_case(camel_case)
    # Print the converted user input
    print("snake_case:", snake_case)


# Create function to take camel case `string` as an input and return converted snake case `string`
def convert_to_snake_case(string):
    converted_snake_case_string = ""

    # Iterate over each character in the input string
    for char in string:
        # If character is found to be uppercase letter, add underscore before the letter, and convert the letter to lowercase using the lower() method
        if char.isupper():
            converted_snake_case_string += "_" + char.lower()
        # If character is not an uppercase letter, append to the converted_string as is
        else:
            converted_snake_case_string += char
    # Return the converted snake case string as a value
    return converted_snake_case_string


main()
