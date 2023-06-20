import random


# `main` function gets the level, generates the random number, and then evaluates the user's guesses until they guess correctly
def main():
    level = get_level()
    random_int = get_random_int(level)
    evaluate_guess(level, random_int)


# `get_level` function continues prompting the user until they provide a valid positive integer as the level
def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level <= 0:
                raise ValueError
            break

        except ValueError:
            pass

    return level


# `get_random_int` function generates a random integer between 1 and the input level
def get_random_int(level):
    random_int = random.randint(1, level)

    return random_int


# `evaluate_guess` function prompts the user to guess the generated number and provides feedback on whether the guess is too small, too large, or just right
def evaluate_guess(level, random_int):
    while True:
        guess = get_user_guess(level)

        if guess < random_int:
            print("Too small!")

        elif guess > random_int:
            print("Too large!")

        else:
            print("Just right!")

            break


# `get_user_guess` function continues prompting the user until they provide a valid positive integer within the correct range as their guess
def get_user_guess(level):
    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0 or guess > level:
                raise ValueError
            break

        except ValueError:
            pass

    return guess


if __name__ == "__main__":
    main()
