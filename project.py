import pandas as pd
from collections import defaultdict
import player as P
import play as ply

"""
This module contains all the main code needed to run the project. 
The methods in this file deal with getting all the data form csvs and calulating all the basic weekly stats for each player. 
The stats calculated using the methods in this document are used to do analysis in other files (analysis.py)
"""

def getPlayers():
    """
    Gets the names, positions, and team for all NFL players in the 2022 NFL season.
    The function also reformatts player names from "first last" to all caps "first intial.last". 
    Name formatting is done to make names the same as they appear in the pbp data. 
    Returns: A dictionary of player name (key) and list of player objects associated with that name (values)
    """
    all_players = defaultdict(list)
    df = pd.read_csv("player_2022_season.csv")
    players = df['Player']
    team = df['Team']
    pos = df['Pos']
    for i, p in enumerate(players):
        if type(p) is not str:#weird error with csv that a couple nan values get added
            continue
         #for each edge case player need to do an if stament for that player specifically. Should be few edge cases
        if p == "Amon-Ra St. Brown":
            #Specific edge case
            formatted = "A.ST."
            name = ["Amon-Ra", "St. Brown"]
        elif p == "Jamaal Williams":
            formatted = "JA.WILLIAMS"
            name = ["Jamaal", "Williams"]
        elif pos[i] not in ['QB', 'RB', 'WR', 'TE']: #don't care about defenses or kickers
            continue
        else:
            name = p.split()
            formatted = name[0][0] + "." + name[1]
            formatted = formatted.upper()
        curr_player = P.Player(formatted, team[i], pos[i]) #create player object
        curr_player.set_first_last(name[0], name[1])
        all_players[formatted].append(curr_player)
    return all_players

def get_week_dates():
    """
    Gets the date each week is played to associate pbp data with a week.
    I need this because the play by play data only has date and I need to associate date with week

    Parameters
    ---------
    None

    Returns
    rtrn: dict
        key = date (month/day/year) (string), value = week associated with date.
    """
    df = pd.read_csv("2022_week_date_data.csv")
    week = df['Week']
    date = df['Date']
    rtrn = {}
    for i in range(0, len(week)):
        rtrn[date[i]] = week[i]
    return rtrn


def get_players_from_pbp(play):
    """
    Helper function to seperate the players in the play from the play data itself

    Parameters
    ----------
    play: str
        One line of play by play data
    
    Returns
    -------
    play_players: list
        Returns a list of strings, where each string in the list is a player that appeared in the play. 
        The list is in the order the players appeared in the play
    """
    play_strs = play.split()
    play_players = []
    for str in play_strs:
        if (len(str) < 3):
            continue
        if (str[0:2].isnumeric and str[2] == '-') or (str[0].isnumeric() and str[1] == '-'):
            j = 0
            while str[j].isnumeric():
                j += 1
            j += 1
            str = str[j:]
            play_players.append(str)
    return play_players

def get_yards(play):
    """
    Helper function to get yards out of a play by play string.
    Only used for the case where I need to find out yards on a play where there is a penalty

    Parameters
    ---------
    play: str
        Play by play string.

    Returns
    -------
    Yards: int
        The yards from the play by play string
    """
    play_strs = play.split()
    yards = 0 #default value. If yards doesn't come up its no gain (0 yards)
    for i, str in enumerate(play_strs):
        if str == "FOR" and i + 2 < len(play_strs) and "YARD" in play_strs[i + 2]:
            yards = float(play_strs[i + 1])
            break 
    return yards


def calc_stats():
    """
    This is the function that actually goes through the pbp (play by play) data and calculates player stats.
    It goes through each play, each week and stores player stats in there respective player objects.

    Parameters
    ---------
    None

    Returns
    -------
    Returns 
    players: dict
        A dictionary matching player name (formatted) to a player object containing the data for that player. Key = Player name, value = list of player objects.
        The reason for having a list of player objects is for situation where there are mutiple players with the same name. Allows code to go through list and match player
    """
    df = pd.read_csv("pbp-2022.csv")
    global players
    players = getPlayers()
    week_dats = get_week_dates()
    #Get pre parsed data from pbp data. 
    pbp = df["Description"]
    yards = df["Yards"]
    is_noplay = df["IsNoPlay"] #used to check if play happened
    td = df["IsTouchdown"]
    play_type = df["PlayType"]
    date = df["GameDate"]
    team = df["OffenseTeam"]
    rush = df["IsRush"]
    isPass = df["IsPass"]
    int = df["IsInterception"]
    incomplete = df["IsIncomplete"]
    fumble = df["IsFumble"]
    quarter = df["Quarter"]
    minute = df["Minute"]
    second = df["Second"]
    down = df["Down"]
    distance = df["ToGo"]
    first_down = df["SeriesFirstDown"]
    yard_line_start = df["YardLine"] #yard line at start of play. 0 is on your own endzone 100 is at opponents endzone
    type = "Pass"
    two_point = df["IsTwoPointConversionSuccessful"]
    for i in range(0, len(pbp)):
        week = week_dats[date[i]]
        if is_noplay[i]: #no play means no fantasy points so continue
            continue
        elif isPass[i] and incomplete[i]: #no fantasy points skip for now
            continue
        elif (isPass[i] and int[i]): #int
            play_data = get_players_from_pbp(pbp[i])
            if len(players[play_data[0]]) > 0:
                players[play_data[0]][0].add_int(week) #QB who threw pick will be first player mentioned
        elif (two_point[i]): #two point conversion
            players_in_play = get_players_from_pbp(pbp[i])
            for str in players_in_play:
                if len(players[str]) > 0:
                    curr_player = players[str][0]
                    curr_player.add_two_point(week)
        else: #normal plays
            play = pbp[i]
            yard = yards[i]
            reversed = False
            if "REVERSED" in play:
                #special case. Ruled TD on the field and overturned ball at 1. Need to subtract yards and not count td
                actual_play = play.find("REVERSED") + 10
                play = play[actual_play:]
                #need to update yards
                yard = get_yards(play)
                reversed = True
            if "NULLIFIED" in play: #TD nullfied by penalty don't count
                reversed = True
            end_of_offense_data = play.find("YARDS") + 5 #what about no gain. Does this even matter? May matter for receptiions.
            if end_of_offense_data == 4: #play goes for 1 yard
                end_of_offense_data = play.find("YARD") + 1
            if "YARD" not in play and "NO GAIN" in play: #play goes for no gain
                end_of_offense_data = play.find("NO GAIN") + 7 
            play = play[0:end_of_offense_data] #remove defensive information from play
            players_in_play = get_players_from_pbp(play)
            for str in players_in_play:
                #checks to see if player listed. All players have same format "number-"
                if len(players[str]) >= 1:
                    curr_player = players[str][0]
                    if (len(players[str]) > 1): #duplicate players
                        for j in range(0, len(players[str])):
                            curr_player = players[str][j]
                            if curr_player.team == team[i]:
                                break
                    if (isPass[i]):
                        if (play.find("PASS") > play.find(str)): #QB's name will be before the word pass. WR will be after
                            curr_player.add_yards(week, yard, "Pass")
                            type = "Pass"
                        else:
                            curr_player.add_yards(week, yard, "Rec")
                            type = "Rec"
                    elif (rush[i]):
                        curr_player.add_yards(week, yard, "Rush")
                        type = "Rush"
                    elif (play_type[i] != "SACK"): #edge case for rush, but sheet doesn't count it as rush
                        #print(pbp[i])
                        yard = get_yards(play)
                        curr_player.add_yards(week, yard, "Rush")
                        type = "Rush"
                    if (td[i] and not reversed):
                        if (play.find("PASS") > play.find(str)):
                            curr_player.add_td(week, "Pass") 
                        else:
                            curr_player.add_td(week, "Other") 
                    look = "RECOVERED BY " + curr_player.team.upper()
                    if (fumble[i] and not look in pbp[i] and "RECOVERED BY" in pbp[i]):
                        if (isPass[i] and play.find("PASS") > play.find(str)): 
                            #fumbles after pass so don't add fumble to QB
                            break
                        else:
                            curr_player.add_fumble(week)
                elif len(players[str]) == 0:
                    #Error, or defensive player accicdently captured. Do nothing
                    a = 5
            
            is_td = td[i] and not reversed
            curr_play = ply.Play(week, yard, type, is_td, yard_line_start[i], quarter[i], minute[i], second[i], down[i], distance[i], first_down[i])
            curr_player.add_play(curr_play)
    return players


#Local test cases on Project.py
# calc_stats()
# print(players["P.MAHOMES"][0].get_score(1))
# print(players["T.KELCE"][0].get_score(1))
# print(players["K.MURRAY"][0].get_score(1))
# print(players["J.ALLEN"][0].get_score(2))
# print(players["A.EKELER"][0].get_score(9))
# print(players["T.HILL"][0].get_score(1))
# print(players["J.FIELDS"][0].get_score(5))
# print(players["J.FIELDS"][0].get_score(8))
# print(players["J.HURTS"][0].get_score(9))
# print(players["P.MAHOMES"][0].get_score(11))
#print(players["D.HENRY"][0].get_score(4))
# print(players["A.ST."][0].get_score(2))
        

