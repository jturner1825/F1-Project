# main.py
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

if SRC_DIR.exists():
    sys.path.insert(0, str(SRC_DIR))

from f1sim.sim.season import Season
from f1sim.services.loader import load_teams, load_drivers, load_circuits


def print_menu() -> str:
    lines = []
    lines.append("\n2025 F1 Season Menu")
    lines.append("-------------------------------")
    lines.append("1. Run next race")
    lines.append("2. Show last race results")
    lines.append("3. Show WDC Standings")
    lines.append("4. Show Constructors Standings")
    lines.append("5. Run entire season")
    lines.append("6. Quit\n")
    return "\n".join(lines)


def main() -> None:
    data_dir = SRC_DIR / "f1sim" / "data"

    teams_by_id = load_teams(str(data_dir / "teams.json"))
    teams = list(teams_by_id.values())
    drivers = load_drivers(str(data_dir / "drivers.json"), teams_by_id)
    circuits = load_circuits(str(data_dir / "circuits_2025.json"))

    season = Season(drivers, teams, circuits)

    while True:
        print(print_menu())
        user_input = input("Enter an option to advance: ").strip()

        match user_input:
            case "1":
                print(season.run_next_race())
            case "2":
                print(season.return_race_results())
            case "3":
                print(season.return_wdc_standings())
            case "4":
                print(season.return_constructors_standings())
            case "5":
                print(season.run_entire_season())
            case "6":
                break
            case _:
                print("Invalid input! Please try again!")


if __name__ == "__main__":
    main()
