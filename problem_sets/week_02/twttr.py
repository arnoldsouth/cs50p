# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    # prompts the user to enter a string of text
    text = input("Input: ")
    # function is called to remove all the vowels from the text
    new_text = omit_vowels(text)

    print("Output:", new_text)


# Create function to output user string but omit vowels (user input can be upper or lowercase)


def omit_vowels(text):
    # string variable `all_vowels` is defined to store all the vowels
    all_vowels = "AaEeIiOoUu"
    # initialized as an empty string
    no_vowels_text = ""

    # function iterates over each character in the input `text` using a `for` loop
    for char in text:
        # if the character is not found in the `all_vowels` string, it is appended to the `no_vowels_text` string
        if char not in all_vowels:
            no_vowels_text = no_vowels_text + char

    # `no_vowels_text` is returned which is printed in the main() function
    return no_vowels_text


main()
