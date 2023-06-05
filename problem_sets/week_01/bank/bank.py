# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Get user input
greet = input("Greeting: ")

# Remove leading/trailing whitespaces in user greet and convert to lowercase to ignore cases
clean_greet = greet.strip().lower()

# Check for conditions, starting with 'hello' first

if clean_greet.startswith("hello"):
    print("$0")
elif clean_greet.startswith("h"):
    print("$20")
else:
    print("$100")
