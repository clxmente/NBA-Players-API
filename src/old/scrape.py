""" This file is now useless. Could work if I found a way to change the table 
pages but since the table is not all loaded at once in HTML, it only fetches 
the first 50 rows of the table. """
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.nba.com/players"
html = urlopen(url)
soup = BeautifulSoup(html, features="html.parser")

table = soup.find("table")
x = (len(table.findAll("tr"))-1)
i = 0
for row in table.findAll("tr")[1:]:
    i += 1
    player = row.findAll("td")
    player_fname =  player[0].find_all(class_="t6 mr-1")[0].getText()
    player_lname =  player[0].find_all(class_="t6")[2].getText()

    player_full_name = f"{player_fname} {player_lname}"

    player_team = player[1].getText()
    player_num = player[2].getText()
    player_position = player[3].getText()
    print(f"ROW: {i} | Player: {player_full_name} | Team: {player_team} | Number: {player_num} | Position: {player_position}")