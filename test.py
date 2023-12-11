import unittest
import pandas as pd
import project as p


class TestProject(unittest.TestCase):
    #testing function
    global test_data 
    global player_data
    test_data = pd.read_csv("player_2022_season.csv")
    player_data = p.calc_stats()

    def test_one_player(self):
        """
        Tests one specfic player to see if that players weekly score is within an acceptable range.
        Asserts false if any score from any week falls outside that range.
        """
        results = test_data.loc[test_data["Player"] == "Patrick Mahomes II"]
        for i in range(1, 16):
            if (results[str(i)][0] == "BYE"):
                continue
            expected = float(results[str(i)][0])
            actual = player_data["P.MAHOMES"][0].get_score(i)
            error = "Week " + str(i) + " Expected: " + str(expected) + " Acutal" + str(actual)
            self.assertTrue((expected - 5) <= actual <= (expected + 5), error)

    def test_top_50(self):
        """
        Compares the score of the top 50 fantasy scorers on the season from my calculations to the actual values. 
        Compares the totals for each player every week.
        Gets the percentage that are correct and asserts false if the percent correct is too low. 
        """
        f_players = getFormatted()
        bound = 1
        total = 0
        correct = 0
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
                actual = round(player_data[player][0].get_score(j), 1)
                error = "Week " + str(j) + " " + player + " Expected: " + str(expected) + " Acutal " + str(actual)
                total += 1
                if not ((expected - bound) <= actual and actual <= (expected + bound)):
                    #print(error)
                    pass
                else:
                    correct += 1
        correct_percent = correct / total
        wrong = total - correct

        #self.assertTrue((expected - 5) <= actual <= (expected + 5), error)
        print(correct, total, correct_percent, wrong)
        self.assertTrue(correct_percent >= 0.90)

def getFormatted():
    """
    Helper function to get formatted version of full player name.
    Goes through each player in the player_2022_season.csv and gets there formatted name. Used for testing
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


