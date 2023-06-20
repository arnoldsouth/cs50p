import random


def main():
    # Get the difficulty level from the user.
    level = get_level()

    score = 0
    # Generate 10 problems, calculate score based on user's answers.
    for _ in range(10):
        score += generate_problem(level)

    # Print the final score.
    print("Score:", score)


def get_level():
    while True:
        try:
            # Get input from user and convert it to an integer.
            n = int(input("Level: "))
            # If the input is valid (1, 2, or 3), return it as the level.
            if n in [1, 2, 3]:
                return n
        except ValueError:
            # If the input is not a valid integer, ignore it and ask again.
            pass


def generate_integer(level):
    # Calculate the maximum and minimum value for the given level.
    max_value = 10**level - 1
    min_value = 10 ** (level - 1)

    if level == 1:
        min_value = 0

    # Generate and return a random integer within the calculated range.
    random_int = random.randint(min_value, max_value)
    return random_int


def generate_problem(level):
    # Generate two random integers of the given level.
    x = generate_integer(level)
    y = generate_integer(level)

    # Give the user three chances to answer the problem correctly.
    for _ in range(3):
        try:
            # Ask the user the math problem and get their answer.
            user_answer_input = int(input(f"{x} + {y} = "))
            # If the answer is correct, return 1 (signifying a correct answer).
            if user_answer_input == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")

    # If the user doesn't answer correctly after three attempts, print the correct answer and return 0 (signifying an incorrect answer).
    print(f"{x} + {y} = {x + y}")
    return 0


if __name__ == "__main__":
    main()


# Pseudocode:

# Start main function:
#     Ask for difficulty level
#     Initialize score to 0

#     For each problem in 10 problems:
#         Increase score by the return value of generate_problem

#     Print final score

# End main function

# Start get_level function:
#     Forever:
#         Get input from user
#         If input is 1, 2, or 3:
#             Return input as level

# End get_level function

# Start generate_integer function:
#     Calculate max value and min value based on level
#     If level is 1:
#         Set min value to 0

#     Generate and return random integer between min and max values

# End generate_integer function

# Start generate_problem function:
#     Generate two random integers of the given level

#     For each attempt in 3 attempts:
#         Ask user the math problem and get their answer
#         If answer is correct:
#             Return 1 (signifying a correct answer)
#         If answer is incorrect or not a number:
#             Print error message ("EEE")

#     If user didn't answer correctly after three attempts:
#         Print correct answer
#         Return 0 (signifying an incorrect answer)

# End generate_problem function

# Start generate_score function:
#     Print final score

# End generate_score function
