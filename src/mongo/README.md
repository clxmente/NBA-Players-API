# nba_data.json
This data comes from [The NBA Website](https://nba.com/players) and can be found by
inspecting element, and finding the first `<script>` tag in the `<body>` section.

# remake_players.py
This file takes the data from the NBA website and formats it to have only the values
used by the API and makes a separate file called `players.json`.

# fillmongo.py
This file takes all the data from `players.json` and inserts it into a mongodb
collection called 'players'.