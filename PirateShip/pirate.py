import random

class Pirate:

    status_alive = 1
    status_dead = 0

    def __init__(self, name = "Jack"):
        self.alcohol_level = 0
        self.name = name
        self.status = Pirate.status_alive
        self.has_parrot = False

    def drink_some_rum(self):
        try:
            self.check_death()
            self.alcohol_level += 1
        except ValueError as e:
            print(e)

    def check_death(self):
        if self.status == Pirate.status_dead:
            raise ValueError("This pirate is dead")

    def hows_it_going_mate(self):
        try:
            self.check_death()
            if self.alcohol_level <= 4:
                print("Pour me anudder!")
            else:
                print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
                self.alcohol_level = 0
        except ValueError as e:
            print(e)

    def die(self):
        self.status = Pirate.status_dead
        self.alcohol_level = 0

    def brawl(self, opponent):
        try:
            self.check_death()
            opponent.check_death()
            outcome = random.randint(1,3)
            if outcome == 1:
                self.die()
                opponent.has_parrot = True
            elif outcome == 2:
                opponent.die()
                self.has_parrot = True
            else:
                self.die()
                opponent.die()
        except ValueError as e:
            print(e)