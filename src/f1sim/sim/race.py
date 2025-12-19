import random

class Race():
    POINTS_TABLE = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

    def __init__(self, drivers, teams):
        self.drivers = drivers
        self.teams = teams
        self.results = []
        self.winner = None
        self.noise_range = (-10,10)
    
    def simulate_race(self):
        for driver in self.drivers:
            noise = random.randrange(self.noise_range[0], self.noise_range[1])
            performance = driver.rating + noise
            self.results.append((driver, performance))
        
        print("Simulating Race...\n")
        # Sort drivers by random performance
        self.results = sorted(self.results, key = lambda x: x[1], reverse = True)
        self.winner = self.results[0][0]

        # Driver win
        self.winner.add_win()

        # Award driver points
        for i, (driver, _) in enumerate(self.results, start=1):
            points = self.POINTS_TABLE.get(i,0)
            driver.add_points(points)

            # Award team points
            for team in self.teams:
                if driver.team == team.name:
                    team.add_win()
                    break
        return self.winner, self.results
