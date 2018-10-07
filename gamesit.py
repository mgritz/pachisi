from termcolor import colored

# Class that represents a certain game situation
class GameSit:
    def __init__(self):
        # container for figures
        self.field = [None] * 40
        # starting points for players
        self.starts = [0, 10, 20, 30]
        # wait zones for every player (first index is payer)
        self.waitZones = [[None] * 4] * 4
        # safe-zone gates for players
        self.gates = [39, 9, 19, 29]
        # safe-zones for every player (first index is payer)
        self.safeZones = [[None] * 4] * 4

class FieldViewer:
    def __init__(self, game, colors = ['red', 'green', 'blue', 'yellow']):
        self.game = game
        self.colors = colors

    def draw(self):
        field = ""
        for s in self.game.field:
            slot = "|"
            if s == None :
                slot = slot + " "
            else:
                slot = slot + colored("█", self.colors[s.player])
            field = field + slot
        print(field)

