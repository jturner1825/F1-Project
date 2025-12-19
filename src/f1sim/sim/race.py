import random

class Race():
    POINTS_TABLE = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

    def __init__(self, drivers, teams, noise_range=(-10,10)):
        self.drivers = drivers
        self.teams = teams
        self.noise_range = noise_range
        self.results = []
        self.winner = None
        
    
    def simulate_race(self):
        print("Simulating Race...\n")

        # Result results each race
        self.results = []

        # Build a quick lookup so we don't nested-loop teams every time
        team_by_name = {t.name: t for t in self.teams}


        # Computer performance = rating + noise
        for driver in self.drivers:
            noise = random.randrange(self.noise_range[0], self.noise_range[1])
            performance = driver.rating + noise
            self.results.append((driver, performance))
        
        # Sort drivers by  performance (descending)
        self.results.sort(key=lambda x: x[1], reverse=True)
        self.winner = self.results[0][0]

        # Driver win
        self.winner.add_win()

        # Award driver + constructor points
        for i, (driver, _) in enumerate(self.results, start=1):
            points = self.POINTS_TABLE.get(i,0)

            driver.add_points(points)

            team = team_by_name.get(driver.team)
            if team is not None:
                team.add_points(points)

        # Award constructor win to winner's team
        winner_team = team_by_name.get(self.winner.team)
        if winner_team is not None:
            winner_team.add_win()
            
        return self.winner, self.results
