class Play():
    """
    A class to represent a play. 
    Basically the play class is a breakdown of all the information on a single play for a player. 
    The breakdown of all aspects of the play allows us to calculate advanced statistics 

    ...

    Attributes
    ---------
    week: int
        The week that the play occurs. 
    yards: int
        The yards gained on the play
    type: string
        Type of yards gained on play (pass, rush/rec)
    td: boolean
        True if a touchdown was scored on the play false otherwise
    yard_line_start: int
        The yard line the play was started on. 100 means oppenents endzon 0 means own endzone 
    quarter: int
        The current quarter the game is in. 1-5 where 5 is overtime
    minute: int
        Minutes left on clock for current quarter at time of play
    second: int
        Seconds left on clock at time of play
    down: int
        down the team was at before the play (1st, 2nd, 3rd, 4th)
    distance: int
        Distance needed to go (yards) to get first down
    first_down_gained: bool
        True if the player gained a first down on the play. False otherwise
    
    Methods
    ------
    print():
        Just a helper function to print all attributes of the current play 
    
    """
    def __init__(self, week, yards, type, td, yard_line_start, quarter, minute, second, down, distance, first_down_gained):
        """
        Construct all the necesary attributes for the player object
        Attributes are all same as class attributes, so I won't list again here. 
        """
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

