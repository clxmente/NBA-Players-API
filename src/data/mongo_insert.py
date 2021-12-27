import json
from pymongo import MongoClient

# connect to local host mongo
client = MongoClient('mongodb://127.0.0.1:27017')

# create new db named "nba"
db = client.nba

# open the json file to convert to mongodb
with open("./src/data/players.json", "r") as file:
    data = json.load(file)
 
# insert into collection named "players"
for i in data["players"]:
    db.players.insert_one({
        'FULL_NAME': i['FULL_NAME'],
        'FNAME': i['FNAME'],
        'LNAME': i['LNAME'],
        'JERSEY_NUM': i['JERSEY_NUM'],
        'POS': i['POS'],
        'TEAM': i['TEAM'],
        'LOWER_NAME': i['FULL_NAME'].lower()
    })

# Sample query to find all Centers
all_centers = db.players.find({"POS": "C"})
for player in all_centers:
    print(player["FULL_NAME"])