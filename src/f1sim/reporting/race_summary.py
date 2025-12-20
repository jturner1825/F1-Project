class RaceSummary:
    def __init__(self, winner, results, drivers, teams):
        self.winner = winner
        self.results = results          # List[Driver]
        self.drivers = drivers          # List[Driver]
        self.teams = teams              # List[Team]

    def return_race_results(self):
        lines = []
        lines.append("Final Grid")
        lines.append("-------------------")

        for i, driver in enumerate(self.results, start=1):
            lines.append(f"{i}. {driver[0].name}")
        lines.append("")
        return "\n".join(lines)

    def return_winner(self):
        return f"{self.winner[0].name} has won the race!\n"

    def return_podium(self):
        lines = []
        lines.append("Final Podium")
        lines.append("-------------------")

        for i, driver in enumerate(self.results[:3], start=1):
            lines.append(f"{i}. {driver[0].name}")
        lines.append("")
        return "\n".join(lines)

    def return_wdc_standings(self):
        drivers_sorted = sorted(self.drivers, key=lambda d: d.points, reverse=True)
        lines = []
        lines.append("Current WDC Standings")
        lines.append("-------------------------------")

        for i, driver in enumerate(drivers_sorted, start=1):
            lines.append(f"{i}. {driver.name} — {driver.points} ({driver.wins} wins)")
        lines.append("")
        return "\n".join(lines)

    def return_constructors_standings(self):
        teams_sorted = sorted(self.teams, key=lambda t: t.points, reverse=True)
        lines = []
        lines.append("Constructors Standings")
        lines.append("-------------------------------")

        for i, team in enumerate(teams_sorted, start=1):
            lines.append(f"{i}. {team.name} — {team.points} ({team.wins} wins)")
        return "\n".join(lines)
