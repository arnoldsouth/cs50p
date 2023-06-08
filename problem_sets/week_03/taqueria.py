# Prompt to input user's order
# Input is case insensitive

# Display total cost of all items inputted
# Prefixed with dollar sign `$` and formatted to two decimals

# Ignore inputs that aren't in `menu_dict`
# Note that `menu_dict` items are titlecased


# 1) Create main function to prompt user
# Input is case insensitive

# 2) use `str.title()` method on input and compare with `menu_dict` items, then get the price value using dict keys
# 3) add cost of each inputted item to the running total and then output that running total
# Display total cost of all items inputted
# Prefixed with dollar sign `$` and formatted to two decimals
# 4) keep prompting the user for inputs until the user presses `control-d` (catching an `EOFError`)
# try:
#     item = input()
# except EOFError:
#     ...
# Print a new line (print("\n")) so user's cursor doesn't remain on same line as program's own prompt

# If there's a KeyError, we want to prompt the user again to input more items or give them option to input control-d. So our `get_total` menu should hold the error when looking up the dict key to grab its value


menu_dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    # Initialize `total` variable within `main` function
    total = 0
    get_order("Item: ", total)


def get_order(prompt, total):
    while True:
        try:
            item = input(prompt).title()

            price = menu_dict[item]
            total += price

            print("Total:", f"${total:.2f}")

        except KeyError:
            pass

        except EOFError:
            print()
            break


main()
