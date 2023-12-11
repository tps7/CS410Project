import stats as s


class Player():
    """
    A class to represent a player
    ...

    Attributes
    ----------
    name: str
        name of player in form "first letter.last name" in all caps. Example Bob Joe = B.JOE
    first: str
        first name of player
    last: str
        last name of player
    team: str
        team that the player plays for
    pos: str
        Position that the player plays. Either QB (Quarterback), RB (Running back), WR (Wide Reciever), TE (Tight End)
    weekly_stats: dict
        Dictionary with key = week number, and value = Stats object that stores stats for a player
    plays: list
        list of Play objects for each player. Stores all the plays the player participated in

    Methods
    ------
    set_first_last(firstname, lastname):
        sets the first and last name attributes of the player
    add_play(play):
        Adds play object to the player plays list
    add_two_point(week):
        Adds to point converstion for the player on week (given)
    add_yards(week, yards, type)
        Adds yards to the players stats for a week
    add_td(week, type):
        Adds td to players stats for a week
    add_int(week):
        Adds int to players stats for a week
    def add_fumble(week)
        Adds fumble to players stats for a week
    def get_score(week)
        gets player score for a week
    """
    def __init__(self, name, team, pos):
        """
        Construct all the necesary attributes for the player object

        Parameters
        ----------
            name: str
                 name of player in form "first letter.last name" in all caps. Example Bob Joe = B.JOE
            team: str
                Team that the player plays for
            pos: str
                Position the player plays (QB, RB, WR, TE)
        """
        self.name = name #store full name and abbreviated name?
        self.first = ""
        self.last = ""
        self.team = team
        self.pos = pos
        self.weekly_stats = {}
        for i in range(1, 19):
            self.weekly_stats[i] = s.Stats()
        self.plays = []
    #not doing docstrings for functions below as they are self explainitory
    def set_first_last(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def add_play(self, play):
        self.plays.append(play)

    def add_two_point(self, week):
        self.weekly_stats[week].two_pt += 1
    
    def add_yards(self, week, yards, type):
        if (type == "Pass"):
            self.weekly_stats[week].passing += yards
        elif (type == "Rush"):
            self.weekly_stats[week].rushing += yards
        elif (type == "Rec"):
            self.weekly_stats[week].receiving += yards 
            self.weekly_stats[week].rec += 1
        return

    def add_td(self, week, type):
        if (type == "Pass"):
            self.weekly_stats[week].pass_tds += 1
        else:
            self.weekly_stats[week].other_tds += 1
    
    def add_int(self, week):
        self.weekly_stats[week].ints += 1
    
    def add_fumble(self, week):
        self.weekly_stats[week].fumbles += 1
    
    def get_score(self, week):
        #self.weekly_stats[week].print_all()
        return self.weekly_stats[week].get_score()
    




