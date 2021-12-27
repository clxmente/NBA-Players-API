""" Command-line version of the game. A simple proof of concept on how the game
    work. """

from pymongo import MongoClient

def app(table):
    score = 0
    guessed = set()
    while (name:=input("Enter an NBA Player's name: ")) != "exit":
        # don't increment score if player already guessed
        if (name.lower() in guessed):
            print("Already guessed player!")
            continue
        if (table.find_one({"LOWER_NAME": name.lower()})):
            score += 1
            guessed.add(name.lower())
            print(f"Correct! Score: {score}")
        else: print("NO MATCHING PLAYER")
    print("You guessed these players: ")
    # print all the players guessed correctly after exit
    for x in guessed: print(x)
    print(f"final score: {score}")

if __name__ == "__main__":
    client = MongoClient(host="localhost", port=27017)
    db = client.nba
    table = db.players
    app(table)
