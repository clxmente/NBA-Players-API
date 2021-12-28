# NBA-Players-API
API created with FastAPI to return player information from an NBA player, or teams.
## Setup
### Using a virtual environment
Create the virtual environment:
`python3 -m venv venv-folder-name`

Then activate the virtual environment:
- On Windows:
`venv-folder-name\Scripts\activate.bat`
- On unix or MacOS:
`source venv-folder-name/bin/activate`

And finally, install the requirements:
`pip install -r requirements.txt`

### Run the API on Uvicorn:
You can run the API locally using Uvicorn by executing the following command:
`python3 -m uvicorn main:app`

Now the API can be accessed at `http://127.0.0.1:8000`, however there is no default path so nothing will be returned.

# Usage
## Endpoints
| Endpoint |
|----------|
| /nba/player/{player_name} |
| /nba/player/{team_abbreviation} |
## /nba/player/{player_name}
You can retrieve information about an nba player using the `/nba/player/{player_name}` path. JSON response includes player name, position, number, and team.

For example, to get information about the NBA player james harden, you can make a `GET` request to 

`http://127.0.0.1:8000/nba/player/james-harden`.

The JSON response for a query like the one above:
```JSON
{
  "FULL_NAME":"James Harden",
  "JERSEY_NUM":"13",
  "POS":"G",
  "TEAM":"BKN"
}
```
## /nba/team/{team_abbreviation}
Using this endpoint, you can retrieve information about each player on a specified team. JSON response includes player name, position, and number for each member
of the team.

For example, to get player information for each player on the NBA team Atlanta Hawks, you can use the abbreviation for the team `ATL` in the endpoint like so:
`http://127.0.0.1:8000/nba/team/ATL`.

The JSON response for a query like the one above contains player information for each player on the team.
```JSON
[
  {"FULL_NAME":"Bogdan Bogdanovic","JERSEY_NUM":"13","POS":"G"},
  {"FULL_NAME":"Clint Capela","JERSEY_NUM":"15","POS":"C"},
  ...
  {"FULL_NAME":"Trae Young","JERSEY_NUM":"11","POS":"G"}
]
```
