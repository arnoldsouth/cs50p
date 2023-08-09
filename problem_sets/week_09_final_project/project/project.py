import requests, time


API_KEY = "RGAPI-f6f05fcd-1cd2-479d-a140-edd0aebbc8c9"


def main():
    username = get_username()

    puuid = get_puuid(username)
    summoner_data = get_summoner_data(username)

    name = summoner_data["name"]

    match_id_list = get_match_id_list(puuid)
    match_history = get_match_history(match_id_list, puuid)

    print(f"Match History for: {name}")

    for match_id, match_data in match_history.items():
        if match_data:
            role, championName, kills, deaths, assists = match_data
            print(
                f"Match ID: {match_id} / Kills: {kills}, Deaths: {deaths}, Assists: {assists} / {role}, {championName}"
            )
        else:
            print(f"Match ID: {match_id}. No match data available.")


def get_username():
    username_inp = input("Enter username: ").strip()
    return username_inp


def get_puuid(username):
    api_url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={API_KEY}"

    response = requests.get(api_url)
    data = response.json()
    puuid = data["puuid"]

    return puuid


def get_match_id_list(puuid):
    api_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}"

    response = requests.get(api_url)
    data = response.json()
    match_id_list = data

    return match_id_list


def get_match_history(match_id_list, puuid):
    match_history = {}

    for match_id in match_id_list:
        match_data = get_match_data(match_id, puuid)
        match_history[match_id] = match_data

    return match_history


def get_match_data(match_id, puuid):
    api_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}"

    response = requests.get(api_url)
    data = response.json()

    participants = data["info"]["participants"]

    for participant in participants:
        if participant["puuid"] == puuid:
            role = participant["role"].capitalize()
            championName = participant["championName"]
            kills = participant["kills"]
            deaths = participant["deaths"]
            assists = participant["assists"]

            return role, championName, kills, deaths, assists

    return None


def get_summoner_data(username):
    api_url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={API_KEY}"

    response = requests.get(api_url)
    data = response.json()
    summoner_data = data

    return summoner_data


if __name__ == "__main__":
    main()
