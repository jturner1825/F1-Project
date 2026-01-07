import json
from pathlib import Path

from f1sim.models.team import Team
from f1sim.models.driver import Driver
from f1sim.models.circuit import Circuit


def load_teams(path: str | Path) -> dict[str, Team]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {t["id"]: Team(id=t["id"], name=t["name"]) for t in data}


def load_drivers(path: str | Path, teams_by_id: dict[str, Team]) -> list[Driver]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    drivers: list[Driver] = []

    for d in data:
        team = teams_by_id[d["team_id"]]  # keep it simple; let it KeyError if wrong for now
        driver = Driver(
            id=d["id"],
            name=d["name"],
            overall=d["overall"],
            experience=d.get("experience"),
            race=d.get("race"),
            awareness=d.get("awareness"),
            pace=d.get("pace"),
            team=team
        )
        drivers.append(driver)

        # optional: if you want team -> drivers relationship
        if hasattr(team, "drivers"):
            team.drivers.append(driver)

    return drivers


def load_circuits(path: str | Path) -> list[Circuit]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [
        Circuit(
            round=c["round"],
            name=c["name"],
            location=c["location"],
            laps=c["laps"],
            difficulty=c.get("difficulty", 1.0)
        )
        for c in data
    ]