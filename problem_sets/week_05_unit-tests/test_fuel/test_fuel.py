import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("4/4") == 100


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("one/four")
