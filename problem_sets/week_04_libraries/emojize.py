import emoji


def main():
    get_emoji()


def get_emoji():
    user_input = input("Input: ")
    converted_emoji_str = emoji.emojize(user_input, language="alias")

    print(converted_emoji_str)


if __name__ == "__main__":
    main()
