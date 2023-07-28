from seasons import (
    get_user_dob,
    get_current_date,
    calculate_difference,
    convert_to_words,
)

from datetime import date, timedelta
from unittest.mock import patch


@patch("builtins.input", return_value="1991-07-10")
def test_get_user_dob(mock_input):
    assert get_user_dob() == date(1991, 7, 10)


def test_get_current_date():
    assert get_current_date() == date.today()


def test_calculate_difference():
    dob = date(1991, 7, 10)
    current_date = date(2023, 7, 31)
    difference = current_date - dob
    assert calculate_difference(current_date, dob) == difference


def test_convert_to_words():
    difference = timedelta(days=1)  # arbitrary chosen difference of 1 day
    assert convert_to_words(difference) == "One thousand, four hundred forty"
