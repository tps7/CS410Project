class Play():
    def __init__(self, week, yards, type, td, yard_line_start, quarter, minute, second, down, distance, first_down_gained):
        self.week = week
        self.yards = yards
        self.type = type
        self.td = td
        self.yard_line_start = yard_line_start
        self.quarter = quarter
        self.minute = minute
        self.second = second 
        self.down = down 
        self.distance = distance
        self.first_down_gained = first_down_gained
    
    def print(self):
        print("week",self.week,"yards",self.yards,"type",self.type,"td",self.td,"yardline",self.yard_line_start,"quarter",self.quarter,"down", self.down, "distance", self.distance, "first",self.first_down_gained)
        return

