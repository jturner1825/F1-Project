from f1sim.models.driver import Driver
from f1sim.models.team import Team

def main():
    d1 = Driver("Verstappen", "Red Bull", 95)
    d2 = Driver("Tsunoda", "Red Bull", 82)

    team = Team("Red Bull", [d1, d2])

    d1.add_points(25)
    d1.add_win()

    team.add_points(25)
    team.add_win()

    print(d1)
    print(team)

if __name__ == "__main__":
    main()