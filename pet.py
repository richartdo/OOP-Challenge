import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating now...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping now...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} cannot play now.")
            return
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        print(f"{self.name} is being trained a new trick: {trick}...")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)

    def show_tricks(self):
        print(f"{self.name}'s learned new tricks: {', '.join(self.tricks) if self.tricks else 'None'}")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        self.show_tricks()
