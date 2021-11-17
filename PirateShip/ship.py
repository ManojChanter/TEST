import random

from pirate import Pirate

class Ship:
    def __init__(self, captain = None, crew = []):
        if len(crew) == 0 and captain is None:
            self.fill_ship()
        else:
            self.captain = captain
            self.crew = crew

    @property
    def captain(self):
        return self._captain

    @captain.setter
    def captain(self, value):
        if not isinstance(value, Pirate):
            raise ValueError("The captain provided is not a Pirate.")
        self._captain = value

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, value):
        if not isinstance(value, list):
            raise ValueError("The crew is not a list.")
        for index, item in enumerate(value):
            if not isinstance(item, Pirate):
                raise ValueError(f"Crew member {index} is not a Pirate")
        self._crew = value

    def calculate_score(self):
        return sum([p.status for p in self.crew]) - self.captain.alcohol_level

    def battle(self, otherShip):
        if self.calculate_score() > otherShip.calculate_score():
            self.kill_random_people(otherShip)
            self.party(self)
            return "won"
        elif self.calculate_score() < otherShip.calculate_score():
            self.kill_random_people(self)
            self.party(otherShip)
            return "lost"
        else:
            return "draw"

    def party(self, otherShip):
        shots = random.randint(1, 3)
        for i in range(shots):
            otherShip.captain.drink_some_rum()
            for member in otherShip.crew:
                member.drink_some_rum()

    def kill_random_people(self, otherShip):
        losses = random.randint(1, len(otherShip.crew))
        for i in range(losses):
            otherShip.crew[i].die()

    def fill_ship(self):
        self.captain = Pirate()
        crew_count = random.randint(1,5)
        crew = []
        for i in range(crew_count):
            crew.append(Pirate())
        self.crew = crew