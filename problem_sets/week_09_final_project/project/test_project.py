from project import (
    get_username,
    get_puuid,
    get_match_id_list,
    get_match_history,
    get_match_data,
    get_summoner_data,
)


def test_get_username():
    assert get_username("200mph") == "200 mph"
    assert get_username("200 mph") == "200 mph"
    assert get_username("200 MPH") == "200 mph"
    assert get_username("200    MPH    ") == "200 mph"


# def test_get_puuid():
#     assert (
#         get_username(
#             "JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ"
#         )
#         == "JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ"
#     )


# def test_get_match_id_list():
#     ...


# def test_get_match_history():
#     ...


# def test_get_match_data():
#     ...


# def test_get_summoner_data():
#     ...
