import random

class Race():
    def __init__(self, drivers, round, circuit):
        self.drivers = drivers
        self.round = round
        self.circuit = circuit
        self.results = []
        
    def simulate_race(self):
        print(f"Simulating Round {self.round}")

        # Result results each race
        self.results = []
        
        for driver in self.drivers:
            # Build performance for each driver
            base_pace = driver.overall_norm
            qualifying_speed = base_pace * (0.9 + 0.2 * driver.pace_norm)
            race_pace = base_pace * (0.9 + 0.15 * driver.race_norm)
            
            # Variability based on consistency
            sigma = (1 - driver.consistency) * 0.12

            # Apply circuit difficulty modifier
            sigma *= self.circuit.difficulty
            
            # Add Gaussian noise
            noise = random.gauss(0, sigma)
            performance = race_pace + noise
            
            # Add awareness-based errors
            mistake_prob = (1 - driver.awareness_norm) * 0.12
            if random.random() < mistake_prob:
                performance -= random.uniform(0.05, 0.25) 
        
            self.results.append((driver, performance))

        # Sort drivers by performance (descending)
        self.results.sort(key=lambda x: x[1], reverse=True)
        print("Race Complete!")
            
        return self.results
