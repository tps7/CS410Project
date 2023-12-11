import pandas as pd
import numpy as np
from collections import defaultdict
import player as P

#old file not used anymore


def getPlayers():
    """Gets the names, positions, and team for all NFL players in the 2022 NFL season.
    The function also reformatts player names from "first last" to all caps "first intial.last". 
    Name formatting is done to make names the same as they appear in the pbp data. 
    Returns: A dictionary of player name (key) and list of player objects associated with that name (values)
    """
    all_players = defaultdict(list)
    df = pd.read_csv("player_2022_season.csv")
    players = df['Player']
    team = df['Team']
    pos = df['Pos']
    new_players = []
    new_players_two = set()
    counts = defaultdict(int)
    for i, p in enumerate(players):
        if type(p) is not str:#weird error with csv that a couple nan values get added
            continue
         #for each edge case player need to do an if stament for that player specifically. Should be few edge cases
        if p == "Amon-Ra St. Brown":
            #Specific edge case
            formatted = "A.ST. BROWN"
        else:
            name = p.split()
            formatted = name[0][0] + "." + name[1]
            formatted = formatted.upper()
        curr_player = P.Player(formatted, team[i], pos[i]) #create player object
        all_players[formatted].append(curr_player)
        # new_players.append(formatted)
        # if formatted in new_players_two:
        #     print(p, formatted)
        # new_players_two.add(formatted)
        #counts[formatted] += 1
        return all_players

    
    # for k, v in counts.items():
    #     if v > 1:
    #         print(k, v)

getPlayers()

def getFromatted():
    df = pd.read_csv("player_2022_season.csv")
    players = df['Player']
    f_players = {}
    for i, p in enumerate(players):
        if type(p) is not str:#weird error with csv that a couple nan values get added
            continue
         #for each edge case player need to do an if stament for that player specifically. Should be few edge cases
        if p == "Amon-Ra St. Brown":
            #Specific edge case
            formatted = "A.ST. BROWN"
        else:
            name = p.split()
            formatted = name[0][0] + "." + name[1]
            formatted = formatted.upper()
        f_players[p] = formatted
    return f_players


"""
Ideas

Player Class:
    Player class will have all information about a player. 
    Will store data for each week and each play. 
    This will allow me to calulate advanced stats on a per player basis
    If I want to compare players I will need to make a compare function or something
Each time you find a player 
Ignore Defense and kicker
Only a couple players with problems

Problem 1:
Players have same first intial and last name. Can check based on team, but if a player is traded midseason team that they are currently on won't check out.
There is a possible edge case that no matter what I do will fail as what if player has same first intial and last name on same team?
Can't check with numbers bc 1. don't have data 2. player can be traded/change number
Solution is manually adjust for any traded players. Only check team if there is a conflict. Not too many trades so should be fine.

Problem 2:
How to ignore defensive players as they can cause name conflicts as well. 
    Defensive players are always in the end surrounded by (). Can use this fact to eleminate them

Need to list out all cases of play formats and how to handle them.

Problem 3
Yardline data in CSV is messed up. No it is just 100/0 When somehting like a quarter ends or a time out is called.

Yardline data is yardline at start of play

Problem 4:
Game data is not in time order what soever. 

Problem 5:
Quater data isn't accurate. Has 5th quaters. Okay Q5 is OT

Problem 6:
Current CSV does not keep track of game score.

Edge Cases I am missing:
Player fumbles into forward into endzone and teamate falls on ball for TD.
"""