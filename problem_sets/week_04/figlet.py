from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        figlet = get_random_font(figlet)
        print_figlet(figlet)

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = sys.argv[2]

            if f not in figlet.getFonts():
                exit_with_error()

            figlet = get_specific_font(f)
            print_figlet(figlet)

        else:
            exit_with_error()

    else:
        exit_with_error()


def get_random_font(figlet):
    fonts_list = figlet.getFonts()
    f = random.choice(fonts_list)

    figlet.setFont(font=f)

    return figlet


def get_specific_font(f):
    figlet = Figlet(font=f)

    return figlet


def print_figlet(figlet):
    input_str = input("Input: ")

    print("Output: \n", figlet.renderText(input_str))


def exit_with_error():
    error_message = "Invalid usage"

    sys.exit(error_message)


if __name__ == "__main__":
    main()
