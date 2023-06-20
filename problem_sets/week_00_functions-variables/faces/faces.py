# Create `main` function that calls `convert` on the user's input and prints the result
def main():
    # Get user input
    str = input()

    # Call `convert` function on user input
    converted_str = convert(str)

    # Print converted user input
    print(converted_str)


# Create `convert` function to replace :) and :( emoticons to happy and sad emojis
def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()
