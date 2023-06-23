def main():
    tweet_input = input("Input: ")
    shortened_tweet = shorten(tweet_input)

    print(f"Output: {shortened_tweet}")


# expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""

    for char in word:
        if char not in vowels:
            result += char

    return result


if __name__ == "__main__":
    main()
