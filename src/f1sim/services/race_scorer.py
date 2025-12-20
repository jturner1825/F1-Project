class RaceScorer:
    POINTS_TABLE = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

    def __init__(self, results, teams):
        self.results = results
        self.teams = teams
        self.winner = None

    def apply_points(self):
        if not self.results:
            self.winner = None
            return
        
        # Build a quick lookup so we don't nested-loop teams every time
        team_by_name = {t.name: t for t in self.teams}

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