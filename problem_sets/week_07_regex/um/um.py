import re


def main():
    print(count(input("Text: ")))


def count(s):
    # `\b` matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of word characters. Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa), or between \w and the beginning/end of the string. This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
    # searches for the word "um" as a whole word (using \b to match word boundaries) and returns the count of occurrences, case-insensitively
    pattern = r"\bum\b"

    matches = re.findall(pattern, s, re.IGNORECASE)

    if matches:
        return len(matches)


if __name__ == "__main__":
    main()
