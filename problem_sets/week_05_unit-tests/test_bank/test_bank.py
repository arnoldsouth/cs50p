from bank import value


def test_value_hello():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0


def test_value_h():
    assert value("hi world") == 20
    assert value("HI WORLD") == 20


def test_value_else():
    assert value("what's up world") == 100
    assert value("WHAT'S UP WORLD") == 100
