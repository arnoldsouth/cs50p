import requests


API_KEY = "RGAPI-c470d09b-d237-4099-b888-e6c2a601c87c"
SUMMONER_DATA_API_URL = (
    "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}"
)
MATCH_LIST_API_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?start=0&count=20&api_key={}"
MATCH_DATA_API_URL = (
    "https://americas.api.riotgames.com/lol/match/v5/matches/{}?api_key={}"
)


def main():
    try:
        username = get_username()
        puuid = get_puuid(username)
        match_id_list = get_match_id_list(puuid)

        print(f"Recent Match History for {username}")
        print("")

        for match_id in match_id_list:
            print_match_data(match_id)

    except requests.RequestException:
        print(f"Username not found. Please try again.")


# get input from user
def get_username():
    username_inp = input("Enter username: ").strip().lower().replace(" ", "%20")
    print("")

    return username_inp


# helper function
def get_data_from_api_url(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    # response.raise_for_status().json()
    api_data = response.json()

    return api_data


# get summoner's puuid
def get_puuid(username):
    data = get_data_from_api_url(SUMMONER_DATA_API_URL.format(username, API_KEY))
    puuid = data["puuid"]

    return puuid


def get_match_id_list(puuid):
    data = get_data_from_api_url(MATCH_LIST_API_URL.format(puuid, API_KEY))
    match_id_list = data

    return match_id_list


def get_match_data(match_id):
    data = get_data_from_api_url(MATCH_DATA_API_URL.format(match_id, API_KEY))
    participants = data["info"]["participants"]

    participants_stats = []

    for participant in participants:
        stats = (
            participant["teamId"],
            participant["win"],
            participant["summonerLevel"],
            participant["summonerName"],
            participant["role"].capitalize(),
            participant["championName"],
            participant["kills"],
            participant["deaths"],
            participant["assists"],
        )
        participants_stats.append(stats)

    return participants_stats


def print_match_data(match_id):
    participants_stats = get_match_data(match_id)

    print(f"Match ID: {match_id}")

    print(
        f"{'Team':<20} {'Win':<20} {'Summoner Level':<20} {'Summoner Name':<20} {'Role':<20} {'Champion Name':<20} {'Kills':<20} {'Deaths':<20} {'Assists':<20}"
    )

    print("➖" * 95)

    for stats in participants_stats:
        (
            teamId,
            win,
            summonerLevel,
            summonerName,
            role,
            championName,
            kills,
            deaths,
            assists,
        ) = stats

        print(
            f"{teamId:<20} {win:<20} {summonerLevel:<20} {summonerName:<20} {role:<20} {championName:<20} {kills:<20} {deaths:<20} {assists:<20}"
        )

    print("➖" * 95)
    print("")
    print("")


if __name__ == "__main__":
    main()
