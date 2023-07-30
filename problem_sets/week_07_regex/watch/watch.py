import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # takes str of html as input, extracts value of src attribute of an iframe element
    # returns shorter, shareable youtu.be link as str
    # src value is surrounded by double quotes
    # If the input does not contain any such URL at all, return None
    if link := re.search(
        r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)\"></iframe>",
        s,
    ):
        shortened_link = f"https://youtu.be/{link.group(1)}"
        return shortened_link
    else:
        return None


if __name__ == "__main__":
    main()
