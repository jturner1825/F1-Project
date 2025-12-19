# Formula 1 Season Simulation 🏎️

An object-oriented Formula 1 season simulation written in Python.  
This project models drivers and teams, simulates race results, allocates points and wins, and tracks Drivers’ and Constructors’ Championship standings across a season.

---

## 📌 Project Overview

The goal of this project is to simulate a Formula 1 season using clean, modular, and extensible Python code.  
It emphasizes strong object-oriented design, clear data flow, and realistic championship logic rather than graphics or real-time visualization.

The simulation currently supports:
- Driver and team modeling
- Deterministic race result simulation
- Official-style F1 points allocation
- Tracking of wins and championship standings

The project is designed to be extended over time with additional realism such as ratings, randomness, circuits, and season-level analysis.

---

## 🧠 Core Concepts Practiced

- Object-Oriented Programming (classes, encapsulation, relationships)
- State management across multiple races
- Separation of responsibilities (models vs simulation logic)
- Deterministic simulation design
- Clean data modeling for sports simulations

---

## 🏁 Current Features

- **Driver model** including:
  - Name
  - Team
  - Rating (placeholder for future use)
  - Total points
  - Race wins

- **Team model** including:
  - Team name
  - Drivers
  - Constructors’ points
  - Constructors’ wins

- **Race simulation**:
  - Ordered finishing positions
  - Point distribution based on finishing position
  - Updates to driver and team standings

---

## 🔧 Planned Features

- Multi-race season simulation
- Circuit modeling (lap count, location, difficulty)
- Driver and team performance ratings
- Probabilistic race outcomes based on ratings
- Constructors’ Championship logic refinement
- Season summary and standings output
- Optional data analysis or visualization

---

## 📂 Project Structure (Planned)

```text
F1-Project/
│
├── src/
│   └── f1sim/
│       ├── models/
│       │   ├── driver.py
│       │   ├── team.py
│       │   └── circuit.py
│       ├── sim/
│       │   ├── race.py
│       │   └── season.py
│       └── __init__.py
├── main.py
└── README.md
