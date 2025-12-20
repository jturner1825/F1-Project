from f1sim.models.driver import Driver
from f1sim.models.team import Team
from f1sim.sim.race import Race
from f1sim.reporting.race_summary import RaceSummary
from f1sim.services.circuit_repository import CircuitRepository
from f1sim.services.race_scorer import RaceScorer

def main():
    circuits = CircuitRepository.load_from_json(
        "src/f1sim/data/circuits_2025.json"
    )

    print(circuits[0])
    
    drivers_names = ["Norris", "Verstappen", "Piastri", "Russel", "Leclerc", "Hamilton", "Antonelli", "Albon", "Sainz", "Alonso", "Hulkenberg",
                     "Hadjar", "Bearman", "Lawson", "Ocon", "Stroll", "Tsunoda", "Gasly", "Bortoleto", "Colapinto"]
    team = ["McLeran", "Red Bull", "McLeran", "Mercedes", "Ferrari", "Ferrari", "Mercedes", "Williams", "Williams", "Aston Martin", 
            "Kick Sauber", "Racing Bulls", "Hass", "Racing Bulls", "Hass", "Aston Martin", "Red Bull", "Alpine", "Kick Sauber", "Alpine"]
    ratings = [90, 96, 89, 86, 86, 82, 79, 77, 78, 76, 
               71, 68, 68, 66, 69, 70, 67, 67, 65, 62]
    
    drivers = []
    for name, team, rating in zip(drivers_names, team, ratings):
        drivers.append(Driver(name, team, rating))

    teams_dict = {}
    for driver in drivers:
        if driver.team not in teams_dict:
            teams_dict[driver.team] = []
        teams_dict[driver.team].append(driver.name)

    teams = []
    for team_name, team_drivers in teams_dict.items():
        teams.append(Team(team_name, team_drivers))

    r = Race(drivers)
    results = r.simulate_race()
    scorer = RaceScorer(results, teams)
    scorer.apply_points()

    print("Race Complete!")
    
    summary = RaceSummary(results[0], results, drivers, teams)
    print(summary.return_winner())
    print(summary.return_podium())
    print(summary.return_race_results())
    print(summary.return_wdc_standings())
    print(summary.return_constructors_standings())

if __name__ == "__main__":
    main()