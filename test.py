import unittest
import pandas as pd
import numpy as np
import project as p


class TestProject(unittest.TestCase):
    global test_data 
    global player_data
    test_data = pd.read_csv("player_2022_season.csv")
    player_data = p.calc_stats()

    def test_one_player(self):
        results = test_data.loc[test_data["Player"] == "Patrick Mahomes II"]
        for i in range(1, 16):
            if (results[str(i)][0] == "BYE"):
                continue
            expected = float(results[str(i)][0])
            actual = player_data["P.MAHOMES"][0].get_score(i)
            error = "Week " + str(i) + " Expected: " + str(expected) + " Acutal" + str(actual)
            self.assertTrue((expected - 5) <= actual <= (expected + 5), error)

        # print(results)
        # print(type(results["1"]))
        # print(type(results["1"][0]))

    def test_top_50(self):
        f_players = getFromatted()
        for i in range(0, 50):
            curr = test_data.loc[i]
            player = f_players[curr["Player"]]
            for j in range(1, 15):
                if (curr[str(j)] == "BYE"):
                    continue
                elif (curr[str(j)] == '-'):
                    expected = 0 #didn't play so no points
                else:
                    expected = float(curr[str(j)])
                actual = player_data[player][0].get_score(j)
                error = "Week " + str(j) + " " + player + " Expected: " + str(expected) + " Acutal " + str(actual)
                if not ((expected - 5) <= actual and actual <= (expected + 5)):
                    print(error)
                #self.assertTrue((expected - 5) <= actual <= (expected + 5), error)

def getFromatted():
    """Helper function to get formatted version of full player name
    """
    df = pd.read_csv("player_2022_season.csv")
    players = df['Player']
    f_players = {}
    for i, p in enumerate(players):
        if type(p) is not str:#weird error with csv that a couple nan values get added
            continue
         #for each edge case player need to do an if stament for that player specifically. Should be few edge cases
        if p == "Amon-Ra St. Brown":
            #Specific edge case
            formatted = "A.ST."
        elif p == "Jamaal Williams":
            formatted = "JA.WILLIAMS"
        else:
            name = p.split()
            formatted = name[0][0] + "." + name[1]
            formatted = formatted.upper()
        f_players[p] = formatted
    return f_players


if __name__ == '__main__':
    unittest.main()


