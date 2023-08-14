from unittest.mock import patch

from project import (
    get_username,
    get_data_from_api_url,
    get_puuid,
    get_match_id_list,
    get_match_data,
    # print_match_data,
)


@patch("builtins.input")
def test_get_username(mock_input):
    mock_input.return_value = "200 MPH"

    result = get_username()
    assert result == "200%20mph"


@patch("project.requests.get")
def test_get_data_from_api_url(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"key": "value"}

    result = get_data_from_api_url(
        "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}"
    )
    assert result == {"key": "value"}


@patch("project.get_data_from_api_url")
def test_get_puuid(mock_get_data):
    mock_get_data.return_value = {
        "puuid": "JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ"
    }

    puuid = get_puuid("200mph")
    assert (
        puuid
        == "JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ"
    )


@patch("project.get_data_from_api_url")
def test_get_match_id_list(mock_get_data):
    mock_get_data.return_value = ["match1", "match2"]

    match_id_list = get_match_id_list(
        "JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ"
    )
    assert match_id_list == ["match1", "match2"]


@patch("project.get_data_from_api_url")
def test_get_match_data(mock_get_data):
    mock_get_data.return_value = {
        "info": {
            "participants": [
                {
                    "teamId": 200,
                    "win": True,
                    "summonerLevel": 441,
                    "summonerName": "200 mph",
                    "role": "SUPPORT",
                    "championName": "Akali",
                    "kills": 7,
                    "deaths": 7,
                    "assists": 16,
                }
            ]
        }
    }

    result = get_match_data("NA1_4746220856")
    assert result[0][3] == "200 mph"
    # {
    #     "info": {
    #         "participants": [
    #             {
    #                 "teamId": 200,
    #                 "win": True,
    #                 "summonerLevel": 441,
    #                 "summonerName": "200 mph",
    #                 "role": "SUPPORT",
    #                 "championName": "Akali",
    #                 "kills": 7,
    #                 "deaths": 7,
    #                 "assists": 16,
    #             }
    #         ]
    #     }
    # }


# @patch("project.get_match_data")
# def test_print_match_data(mock_get_match_data):
#     mock_get_match_data.return_value = [
#         (200, True, 441, "200 mph", "SUPPORT", "Akali", 7, 7, 16)
#     ]

#     print_match_data("NA1_4746220856")
