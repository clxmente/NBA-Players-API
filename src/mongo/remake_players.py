""" This file takes the data from nba.com and formats into players.json"""
import json

def move():
    players = {}
    players["players"] = []

    with open("./nba_data.json", "r") as nba_data:
        unformatted_data = json.load(nba_data)
    
    with open("./players.json", "w") as players_data:
        for i in unformatted_data["props"]["pageProps"]["players"]:
            players["players"].append({
                "NBA_ID": i["PERSON_ID"],
                "FULL_NAME": i["PLAYER_FIRST_NAME"] + " " + i["PLAYER_LAST_NAME"],
                "FNAME": i["PLAYER_FIRST_NAME"],
                "LNAME": i["PLAYER_LAST_NAME"],
                "JERSEY_NUM": i["JERSEY_NUMBER"],
                "POS": i["POSITION"],
                "TEAM": i["TEAM_ABBREVIATION"]
            })
        json.dump(players, players_data, indent=4)

if __name__ == "__main__":
    move()
    print("done")