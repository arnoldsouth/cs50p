from twttr import shorten


def test_only_vowels():
    assert shorten("AEIOUaeiou") == ""


def test_no_vowels():
    assert shorten("hello world") == "hll wrld"
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"
    assert shorten("h3ll0 w0rld!") == "h3ll0 w0rld!"
