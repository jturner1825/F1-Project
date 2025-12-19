class Driver:
    def __init__(self, name, team, rating):
        self.name = name
        self.team = team
        self.rating = rating
        self.points = 0
        self.wins = 0
    
    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"Team: {self.team}\n"
            f"Rating: {self.rating}\n"
            f"Total Points: {self.points}\n"
            f"Total Wins: {self.wins}\n"
        )
    
    def add_points(self, n):
        self.points += n

    def add_win(self):
        self.wins += 1
        
        