# Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and n names with n-1 commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


import inflect


def main():
    p = inflect.engine()

    # `names` list defined outside while loop in `main` function to prevent it from being re-initialized on every iteration
    names = []

    # the names are collected until the user inputs `control-d` (EOF)
    # then the program prints the adieu message in the required format using the `inflect.engine().join()` method
    while True:
        try:
            # `join_names` function accepts the `names` list as an argument, and returns this `names` list after appending the input name
            # append `names` to the `names` list inside while loop
            names = join_names(names)

        except EOFError:
            print()
            break

    # `print_adieu` function takes the `names` list as an argument
    print_adieu(p, names)


def join_names(names):
    input_str = input("Name: ")

    names.append(input_str)

    return names


def print_adieu(p, names):
    print("Adieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
