# Fuel Gauge

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():
    fuel_fraction = get_fuel_fraction("Fraction: ")
    print(fuel_fraction)


def get_fuel_fraction(prompt):
    while True:
        try:
            fraction_input = input(prompt)
            x, y = fraction_input.split("/")
            x = int(x)
            y = int(y)

            if x > y or y == 0:
                continue

            fuel_percentage = round(x / y * 100)

            if fuel_percentage <= 1:
                return "E"
            elif fuel_percentage >= 99:
                return "F"
            else:
                return str(fuel_percentage) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
