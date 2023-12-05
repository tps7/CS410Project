import stats as s
class Player():
    def __init__(self, name, team, pos):
        self.name = name #store full name and abbreviated name?
        self.first = ""
        self.last = ""
        self.team = team
        self.pos = pos
        self.weekly_stats = {}
        for i in range(1, 19):
            self.weekly_stats[i] = s.Stats()
        self.plays = []
    
    def set_first_last(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def add_play(self, play):
        self.plays.append(play)




    
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
    
    def get_score(self, week):
        self.weekly_stats[week].print_all()
        return self.weekly_stats[week].get_score()
    




