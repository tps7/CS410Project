import pandas as pd
import player as P
import project

"""
This function actual does analysis on the data calculated project.py
"""

global players #Will hold all the player data calculated in project.py
players = project.calc_stats()


def write_to_file(output, file="out.txt"):
    """
    Helper function to write the given dataframe to a file. out.txt is the default file

    Parameters
    ----------
    Output : Pandas dataframe
        This is a dataframe created in one of the calulating functions that will be written to the given input file
    file : file
        This is the file that the inputted dataframe will be written to. Default is out.txt

    Returns
    -------
    None, but does write to a file. 
    """
    with open(file, 'w') as outfile:
        output.to_string(outfile, output.columns)

def most_effective_short_yard():
    """
    Calculates the players who had the highest success rate on converting first downs on either 3rd or 4th down. 
    Only calculates for players with over 5 attempts to make the data better.
    """
    lst = []
    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        opps = 0
        succ = 0
        avg = 0
        curr_player = p.first + " " + p.last #assume no identical first and last names
        for ply in p.plays:
            if (ply.down == 3 or ply.down == 4) and ply.distance <= 2:
                opps += 1
                if (ply.first_down_gained):
                    succ += 1
        if opps > 0:
            avg = succ / opps
        if (opps > 5):
            #counts[curr_player] = (succ, opps, avg)
            lst.append([curr_player, succ, opps, avg])
    lst = sorted(lst, key=lambda x: x[3], reverse=True)
    output = pd.DataFrame(lst, columns=["Player", "Attempts", "Success", "Percentage"])
    write_to_file(output)


def most_chances_inside_10():
    """ Finds players who have had the most attemps inside the 10 yard line and calculates there scoring percentage. """
    lst = []
    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        opps = 0
        succ = 0
        avg = 0
        curr_player = p.first + " " + p.last
        for ply in p.plays:
            if ply.yard_line_start >= 90:
                opps += 1
                if (ply.td):
                    succ += 1
        if opps > 0:
            avg = succ / opps
        if (opps > 5):
            lst.append([curr_player, opps, succ, avg] )
    
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    output = pd.DataFrame(lst, columns=["Player", "Attempts", "Success", "Percentage"])
    write_to_file(output)

def most_touchdowns_in_Q4():
    """ Gets Players who scored the most touchdowns in the 4th quarter throughout the season. Writes output to out.txt"""
    lst = []
    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        tds = 0
        curr_player = p.first + " " + p.last
        for ply in p.plays:
            if ply.quarter == 4:
                if (ply.td):
                    tds += 1
        lst.append([curr_player, tds])
    
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    output = pd.DataFrame(lst, columns=["Player", "Touchdowns"])
    write_to_file(output)




def gained_most_firsts(week_start=1, week_end=14):
    """
    Gets players who have gained the most first downs in a range of weeks.
    Assume range of weeks is in bounds. 

    Parameters:
    ----------
    week_start : int
        The start week. The default value is 1
    week_end : int
        The end week of the search range. The default value is 14.

    Returns
    -------
    No returns, but it does print statistics out to out.txt. 
    """
    lst = []
    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        firsts = 0
        curr_player = p.first + " " + p.last
        for ply in p.plays:
            if ply.week >= week_start and ply.week <= week_end:
                if (ply.first_down_gained):
                    firsts += 1
        lst.append([curr_player, firsts])

    
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    output = pd.DataFrame(lst, columns=["Player", "First Downs"])
    write_to_file(output)

def point_per_first(week_start=1, week_end=14):
    """
    Calculates fantasy scores for players over a week range if they were to receive a point per first down.
    Assume range of weeks is in bounds. 

    Parameters:
    ----------
    week_start : int
        The start week. The default value is 1
    week_end : int
        The end week of the search range. The default value is 14.

    Returns
    -------
    No returns, but it does print statistics out to out.txt. 
    """
    lst = []
    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        firsts = 0
        curr_player = p.first + " " + p.last
        for ply in p.plays:
            if ply.week >= week_start and ply.week <= week_end:
                if (ply.first_down_gained):
                    firsts += 1
        total_score = 0
        for i in range(week_start, week_end + 1):
            total_score += p.get_score(i)
        score_with_firsts = total_score + firsts
        lst.append([curr_player, p.pos, firsts, total_score, score_with_firsts])

    lst = sorted(lst, key=lambda x: x[4], reverse=True)
    output = pd.DataFrame(lst, columns=["Player", "Position", "First Downs", "Fantasy score normal", "Score with point per first"])
    write_to_file(output)







most_effective_short_yard()
#most_chances_inside_10()
#most_touchdowns_in_Q4()
#gained_most_firsts(1, 5)
#point_per_first()


