# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

# Get user input
answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

# Account for user input's case insensitivity and whitespaces
new_answer = answer.lower().strip()

# Check conditionally for '42' or 'forty-two' or 'forty two', output 'Yes' if so, 'No' if not
match new_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
