class Stats():
    """
    A class to represent the stats for a player in a given week

    ...
    Attributes
    ----------

    passing: int
        weekly passing yards
    rushing: int
        weekly rushing yards
    receiving: int
        weekly receiving yards
    rec: int
        weekly receptions
    pass_tds:
        weekly passing touchdowns
    other_tds:
        weekly other touchdowns (rushing/receiving)
    sacks:
        weekly sacks taken
    ints:
        weekly interceptions
    fumbles: int
        weekly fumbles
    two_pt:
        weekly two_pt conversions
    
    Methods
    ------
    get_score():
        Gets the players fantasy point total for the week. Scoring is based on scoring used in test set.
    print_all():
        Prints all the players stats for a week. Used for debugging
    """
    def __init__(self):
        """
        Constructs all necessary attributes for the Stats object
        """
        self.passing = 0
        self.rushing = 0
        self.receiving = 0
        self.rec = 0
        self.pass_tds = 0
        self.other_tds = 0
        self.sacks = 0
        self.ints = 0
        self.fumbles = 0
        self.two_pt = 0
    
    
    def get_score(self):
        """
        Gets the fantasy socre for the player based on the stats for the week.
        The scoring system used is based on the test cases provided. Below is the scoring system used in the test cases. 
        Passing yards: 1 point per 25 yards
        Rushing/Receiving yards: 1 point per 10 yards
        Receptions: 1 point per reception
        Passing Touchdowns: 4 points per td
        Rushing/Receiving Touchdowns: 6 points per td
        Interceptions: -1 per interception
        Fumbles: -2 points per fumble
        Two_pt: 2 points per two point conversion (rushing, receiving, or passing )
        
        Parameters
        ----------
        None

        Returns
        score: int
            The total number of points for the player that week based on the scoring system above
        """
        score = 0
        score += round(self.passing / 25.0, 2)
        score += round(self.rushing / 10, 1)
        score += round(self.receiving / 10, 2)
        score += self.rec
        score += self.pass_tds * 4
        score += self.other_tds * 6
        #score += self.sacks * -0.5
        score += self.ints * -1
        score += self.fumbles * -2
        score += self.two_pt * 2
        return score
    
    def print_all(self):
        #Prints all player stats. Used for debugging 
        print("Passing:",self.passing,"Rushing:",self.rushing,"Receptions",self.rec,"Receiving",self.receiving,"PassTDs:",self.pass_tds, "OtherTDS", self.other_tds, "Ints", self.ints,  "two_point",self.two_pt,"fumble", self.fumbles)


    
    

