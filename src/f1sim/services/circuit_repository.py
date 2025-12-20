import json
from f1sim.models.circuit import Circuit

class CircuitRepository:
    @staticmethod
    def load_from_json(path: str) -> list[Circuit]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        circuits = []
        for entry in data:
            circuits.append(
                Circuit(
                    name=entry["name"],
                    location=entry["location"],
                    laps=entry["laps"],
                    difficulty=entry["difficulty"],
                    round=entry.get("round")
                )
            )
        return circuits
