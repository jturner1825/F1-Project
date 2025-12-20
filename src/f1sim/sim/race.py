import random

class Race():
    def __init__(self, drivers, noise_range=(-10,10)):
        self.drivers = drivers
        self.noise_range = noise_range
        self.results = []
        
    def simulate_race(self):
        print("Simulating Race...\n")

        # Result results each race
        self.results = []

        # Compute performance = rating + noise
        for driver in self.drivers:
            noise = random.randrange(self.noise_range[0], self.noise_range[1])
            performance = driver.rating + noise
            self.results.append((driver, performance))
        
        # Sort drivers by  performance (descending)
        self.results.sort(key=lambda x: x[1], reverse=True)
            
        return self.results
