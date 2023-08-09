import requests, time

api_key = "RGAPI-f6f05fcd-1cd2-479d-a140-edd0aebbc8c9"

summoner_by_name_api_url = (
    "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/200mph"
)
full_summoner_by_name_api_url = summoner_by_name_api_url + "?api_key=" + api_key

response = requests.get(full_summoner_by_name_api_url)
summoner_info = response.json()

# summoner_info["id"]
# summoner_info["accountId"]
# summoner_info["puuid"]
# summoner_info["name"]
# summoner_info["profileIconId"]
# summoner_info["summonerLevel"]

summoner_id = summoner_info["id"]
summoner_account_id = summoner_info["accountId"]
summoner_puuid = summoner_info["puuid"]
summoner_name = summoner_info["name"]
summoner_profileIconId = summoner_info["profileIconId"]
summoner_level = summoner_info["summonerLevel"]


# print("summoner_info:", summoner_info)
# print("summoner_account_id:", summoner_account_id)
# print("summoner_puuid:", summoner_puuid)


# matches_by_puuid_api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ/ids?start=0&count=20"
recent_matches_by_puuid_api_url = (
    "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
)
full_recent_matches_by_puuid_api_url = (
    recent_matches_by_puuid_api_url
    + summoner_puuid
    + "/ids?start=0&count=20"
    + "&api_key="
    + api_key
)
# print("full_recent_matches_by_puuid_api_url:", full_recent_matches_by_puuid_api_url)

response = requests.get(full_recent_matches_by_puuid_api_url)
recent_matches = response.json()
# print("recent_matches:", recent_matches)

recent_matches0 = recent_matches[0]
# recent_matches1 = recent_matches[1]
# recent_matches2 = recent_matches[2]
# recent_matches3 = recent_matches[3]
# recent_matches4 = recent_matches[4]
# recent_matches5 = recent_matches[5]
# recent_matches6 = recent_matches[6]
# recent_matches7 = recent_matches[7]
# recent_matches8 = recent_matches[8]
# recent_matches9 = recent_matches[9]
# recent_matches10 = recent_matches[10]
# recent_matches11 = recent_matches[11]
# recent_matches12 = recent_matches[12]
# recent_matches13 = recent_matches[13]
# recent_matches14 = recent_matches[14]
# recent_matches15 = recent_matches[15]
# recent_matches16 = recent_matches[16]
# recent_matches17 = recent_matches[17]
# recent_matches18 = recent_matches[18]
# recent_matches19 = recent_matches[19]
# print("recent_matches0:", recent_matches0)


# match_data_api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4740748523"
match_data_api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
full_match_data_api_url = match_data_api_url + recent_matches0 + "?api_key=" + api_key

response = requests.get(full_match_data_api_url)
match_data = response.json()

# print("match_data:", match_data.keys())
# print("match_data:", match_data["metadata"])
# print("match_data:", match_data["info"])

# print("match_data:", match_data["info"].keys())
# print("match_data:", match_data["info"]["participants"][0])

# print("match_data:", len(match_data["info"]["participants"]))


participant_index = match_data["metadata"]["participants"].index(summoner_puuid)
# print("participant_index:", participant_index)


player_match_data = match_data["info"]["participants"][participant_index]

player_lane = player_match_data["lane"]
player_role = player_match_data["role"]
player_championName = player_match_data["championName"]
player_kills = player_match_data["kills"]
player_deaths = player_match_data["deaths"]
player_assists = player_match_data["assists"]
player_win = player_match_data["win"]
player_item0 = player_match_data["item0"]
player_item1 = player_match_data["item1"]
player_item2 = player_match_data["item2"]
player_item3 = player_match_data["item3"]
player_item4 = player_match_data["item4"]
player_item5 = player_match_data["item5"]
player_item6 = player_match_data["item6"]

# print("player_lane:", player_lane)
# print("player_role:", player_role)
# print("player_championName:", player_championName)
# print("player_kills:", player_kills)
# print("player_deaths:", player_deaths)
# print("player_assists:", player_assists)
# print("player_win:", player_win)
# print("player_item0:", player_item0)
# print("player_item1:", player_item1)
# print("player_item2:", player_item2)
# print("player_item3:", player_item3)
# print("player_item4:", player_item4)
# print("player_item5:", player_item5)
# print("player_item6:", player_item6)


def get_match_data(region, match_id, api_key):
    api_url = (
        "https://"
        + region
        + ".api.riotgames.com/lol/match/v5/matches/"
        + match_id
        + "?api_key="
        + api_key
    )

    while True:
        response = requests.get(api_url)

        if response.status_code == 429:
            print("Sleep...")
            time.sleep(10)
            continue

        data = response.json()
        # print(data)

        return data


def did_win(summoner_puuid, match_data):
    participant_index = match_data["metadata"]["participants"].index(summoner_puuid)
    player_match_data = match_data["info"]["participants"][participant_index]
    player_win = player_match_data["win"]

    return player_win


region = "americas"
# match_id = recent_matches


# match_data = get_match_data(region, match_id, api_key)
# print(match_data)

# win = did_win(summoner_puuid, match_data)
# print(win)

game_no = 1

for match_id in recent_matches:
    print(game_no)
    print(match_id)

    match_data = get_match_data(region, match_id, api_key)
    win = did_win(summoner_puuid, match_data)

    print(win)
    print("")

    game_no += 1


# https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/JqYjY_hjOLj8Kzy7k7ZcgI-67LtIZWQTnEEKHzgi-vkJZ2ti_CQm-HkaQmT9BiQOKwJqhyISihvbuQ/ids?start=0&count=20
def get_matches(region, summoner_puuid, count, api_key):
    api_url = (
        "https://"
        + region
        + ".api.riotgames.com/lol/match/v5/matches/by-puuid/"
        + summoner_puuid
        + "/ids"
        + "?type=ranked&"
        + "start=0&"
        + "count="
        + str(count)
        + "&api_key="
        + api_key
    )

    response = requests.get(api_url)
    return response.json()


matches = get_matches(region, summoner_puuid, 10, api_key)
