# Prompt user to input one item per line, case insensitively
# Pressing control-d ends the program,which then outputs the list
# List is in all uppercase, sorted alphabetically, prefix each line with the number of times the user inputted that item. Count how many times each input was made


# Defined as empty dict outside of `main` function
grocery_list_dict = {}


def main():
    get_grocery_list()


def get_grocery_list():
    while True:
        try:
            # Assigns `item_name` to user inputs, capitalized and stipped of whitespaces
            item_name = input().upper().strip()

            if item_name not in grocery_list_dict:
                # If inputted item is not in grocery_list_dict, set the dict's key (item_name) to 1
                grocery_list_dict[item_name] = 1
            else:
                # If inputted item is already in grocery_list_dict, add 1 to that key
                grocery_list_dict[item_name] += 1

        except EOFError:
            # Add a line break after user inputs and before printed outputs
            print()

            # `sorted()` function is applied to `grocery_list_dict.items()` to sort the `dict` items
            sorted_alphabetically = sorted(grocery_list_dict.items())

            for item_name, count in sorted_alphabetically:
                print(f"{count} {item_name}")

            # The loop is terminated using `break` after printing the outputs, which allows the program to exit the loop correctly
            break

        except KeyError:
            pass


main()
