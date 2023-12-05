import pandas as pd
import numpy as np
from collections import defaultdict
import player as P
import project

global players 
players = project.calc_stats()

def most_effective_short_yard():
    counts = {}

    for name, pl in players.items():
        if len(pl) < 1:
            continue
        p = pl[0]
        opps = 0
        succ = 0
        avg = 0
        curr_player = p.first + " " + p.last
        for ply in p.plays:
            if p.name == "D.HENRY":
                ply.print()
                print(type(ply.down))
            if (ply.down == 3 or ply.down == 4) and ply.distance <= 2:
                opps += 1
                if (ply.first_down_gained):
                    succ += 1
        if opps > 0:
            avg = succ / opps
        print(opps, succ, avg)
        if (opps > 5):
            counts[curr_player] = (succ, opps, avg)
    
    output = sorted(counts.items(), key=lambda item: item[1][2], reverse=True)
    print(output)

def most_chances_inside_10():
    counts = {}

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
        print(opps, succ, avg)
        if (opps > 5):
            counts[curr_player] = (succ, opps, avg)
    
    output = sorted(counts.items(), key=lambda item: item[1][1], reverse=True)
    print(output)

#most_effective_short_yard()
most_chances_inside_10()


