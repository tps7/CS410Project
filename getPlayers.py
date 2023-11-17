import pandas as pd
import numpy as np
from collections import defaultdict

class Player():
    def __init__(self, name, team, pos):
        self.name
        self.team
        self.pos

def getPlayers():
    df = pd.read_csv("player_2022_season.csv")
    players = df['Player']
    print(players)
    new_players = []
    counts = defaultdict(int)
    for p in players:
        if type(p) is not str:#weird error with csv that a couple nan values get added
            continue
        if p == "Amon-Ra St. Brown":
            #Specific edge case
            formatted = "A.ST. BROWN"
        #for each edge case player need to do an if stament for that player specifically. Should be few edge cases
        name = p.split()
        formatted = name[0][0] + "." + name[1]
        formatted = formatted.upper()
        new_players.append(formatted)
        counts[formatted] += 1
    for k, v in counts.items():
        if v > 1:
            print(k, v)

getPlayers()