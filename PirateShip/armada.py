from ship import Ship

class Armada:
    def __init__(self, ships):
        self.ships = ships

    @property
    def ships(self):
       return self._ships

    @ships.setter
    def ships(self, value):
        if not isinstance(value, list):
            raise ValueError("The provided value is not a list")
        for ix, item in enumerate(value):
            if not isinstance(item, Ship):
                raise ValueError(f"Element index {ix} is not a Ship")
        self._ships = value

    def war(self, opponent_armada):
        our_index = 0
        opponent_index = 0
        while our_index < len(self.ships) and opponent_index < len(opponent_armada.ships):
            print(f"Battle between our ship {our_index} and their ship {opponent_index}")
            battle_result = self.ships[0].battle(opponent_armada.ships[0])
            print(battle_result)
            if battle_result == "won":
                opponent_index += 1
            elif battle_result == "lost":
                our_index += 1
            else:
                our_index += 1
                opponent_index += 1
        if our_index == len(self.ships) and opponent_index == len(opponent_armada.ships):
            return "draw"
        elif our_index == len(self.ships):
            return "won"
        else:
            return "lost"