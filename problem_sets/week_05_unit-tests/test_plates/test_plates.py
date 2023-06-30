from plates import is_valid


def test_atleast_two_char():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("1A") == False
    assert is_valid("1") == False


def test_between_two_and_six_char():
    assert is_valid("AA") == True
    assert is_valid("ABC") == True
    assert is_valid("AABBCC") == True
    assert is_valid("A1B2C3") == False
    assert is_valid("AABBCC11") == False


def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_alphanum():
    assert is_valid("AA11!@") == False
