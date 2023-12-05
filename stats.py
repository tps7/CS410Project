class Stats():
    def __init__(self):
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
        score = 0
        score += round(self.passing / 25.0, 2)
        score += round(self.rushing / 10, 1)
        score += round(self.receiving / 10, 2)
        score += self.rec
        score += self.pass_tds * 4
        score += self.other_tds * 6
        score += self.sacks * -0.5
        score += self.ints * -1
        score += self.fumbles * -2
        score += self.two_pt * 2
        return score
    
    def print_all(self):
        #mainly used for debugging
        print("Passing:",self.passing,"Rushing:",self.rushing,"Receptions",self.rec,"Receiving",self.receiving,"PassTDs:",self.pass_tds, "OtherTDS", self.other_tds, "Ints", self.ints)


    
    

