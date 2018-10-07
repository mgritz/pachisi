from enum import Enum
class PieceState(Enum):
    WAITING = 0
    ACTIVE = 1
    BEATEN = 2
    SAVED = 3

# This class represents a single game piece (figure) and its properties.
class Piece:
    def __init__(self, player):
        self.state = PieceState.WAITING
        self.player = player

    def setState(self, newState):
        self.state = newState