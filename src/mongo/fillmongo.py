import json
from pymongo import MongoClient

# connect to local host mongo
client = MongoClient("localhost", 27017)

# create new db named "nba"
db = client.nba

db.players.drop() # delete all data from before.

# open the json file to convert to mongodb
with open("./players.json", "r") as file:
    data = json.load(file)
 
# insert into collection named "players"
for i in data["players"]:
    db.players.insert_one({
        'NBA_ID': i['NBA_ID'],
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