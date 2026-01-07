class Driver:
    def __init__(self, id, name, overall, experience=None, race=None, awareness=None, pace=None, team=None):
        self.id = id 
        self.name = name
        self.overall = overall
        self.experience = experience
        self.race = race
        self.awareness = awareness
        self.pace = pace
        self.team = team
        self.points = 0
        self.wins = 0
        
    @property
    def overall_norm(self) -> float:
        return self.overall / 100.0
    
    @property
    def experience_norm(self) -> float:
        return (self.experience if self.experience is not None else self.overall) / 100.0
    
    @property
    def race_norm(self) -> float:
        return (self.race if self.race is not None else self.overall) / 100.0
    
    @property
    def awareness_norm(self) -> float:
        return (self.awareness if self.awareness is not None else self.overall) / 100.0
    
    @property
    def pace_norm(self) -> float:
        return (self.pace if self.pace is not None else self.overall) / 100.0
    
    @property
    def consistency(self) -> float:
        # weight experience higher than awareness
        return 0.5 + 0.5 * (0.6 * self.experience_norm + 0.4 * self.awareness_norm)
    
    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"Team: {self.team}\n"
            f"Overall: {self.overall}\n"
            f"Experience: {self.experience}\n"
            f"Racecraft: {self.racecraft}\n"
            f"Awareness: {self.awareness}\n"
            f"Pace: {self.pace}\n"
            f"Total Points: {self.points}\n"
            f"Total Wins: {self.wins}\n"
        )
    
    def add_points(self, n):
        self.points += n

    def add_win(self):
        self.wins += 1
        
        