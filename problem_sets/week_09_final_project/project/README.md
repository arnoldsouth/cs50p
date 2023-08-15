# LEAGUE OF LEGENDS MATCH HISTORY VIEWER

#### Video Demo: <URL HERE>

#### Description:

This script fetches and displays the recent match history of a given Summoner's username from the official Riot Games' API.

### Features:

-   Fetches Summoner's unique identifier (**puuid**) based on the provided **username**.
-   Retrieves the most recent **20** match IDs associated with the Summoner's **puuid**.
-   Displays detailed information about each match, including other players, their roles, champions, and K/D/A (Kills/Deaths/Assists).

### How to Use:

1. Make sure you have Python installed.
2. Ensure the `requests` library is installed: `pip install requests`
3. Clone/download the script.
4. Run the script: `python <script_name>.py`
5. Enter the Summoner's username when prompted.
6. View the displayed recent match history.

### Important Notes:

-   The script uses an API key which is hardcoded and may expire. To ensure continuous functionality, replace the `API_KEY` variable with your Riot Games API key.
-   Handle the API key with care.

### Error Handling:

If a username is not found, the script will notify the user and gracefully exit.

### Modules and Functions:

-   **get_username()**: Fetches and processes the username from user input.
-   **get_data_from_api_url(api_url)**: Utility function to retrieve JSON data from a provided API URL.
-   **get_puuid(username)**: Fetches the puuid for the given username.
-   **get_match_id_list(puuid)**: Fetches the list of recent match IDs for the provided puuid.
-   **get_match_data(match_id)**: Retrieves detailed data for a specific match.
-   **print_match_data(match_id)**: Prints the detailed data of a given match.
