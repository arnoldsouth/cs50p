# Coke Machine

# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Prompt user to insert a coin. Ignore any integer that isn't 25, 10, or 5 cents
# Inform user amount still due after each coin input. Calculate difference (50 cents - user inserted coin). Output amount due
# Once user inputted at least (>=) 50 cents, output how many cents is owed to user if overpaid


def main():
    # Start by initializing the `cost` and `amount_inserted`
    cost = 50
    amount_inserted = 0
    # Print initial cost (amount due) for Coke
    print("Amount Due:", cost)

    # Loop through user's inserted coin amount
    while amount_inserted < cost:
        # Get user input
        coin = get_coin_input()
        # Check coin whether it's valid or not (25, 10, 5 cent coins) and update the user amount inserted
        if check_coin(coin):
            amount_inserted = amount_inserted + coin

        # Call `calculate_amount_due` function calculation
        amount_due = calculate_amount_due(cost, amount_inserted)

        if amount_due <= 0:
            print(end="")
        else:
            print("Amount Due:", amount_due)

    # Call `calculate_change` function
    change = calculate_change(amount_inserted, cost)
    print("Change Owed:", change)


def get_coin_input():
    coin_input = int(input("Insert Coin: "))
    return coin_input


def check_coin(coin_input):
    if coin_input == 5 or coin_input == 10 or coin_input == 25:
        return coin_input


def calculate_amount_due(cost, amount_inserted):
    amount_due = cost - amount_inserted
    return amount_due


def calculate_change(amount_inserted, cost):
    change = amount_inserted - cost
    return change


main()
