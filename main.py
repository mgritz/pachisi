#!/usr/bin/python3

from piece import *
from gamesit import *

p = Piece(0)
p.setState(PieceState.ACTIVE)
g = GameSit()
g.field[3] = p
FieldViewer(g).draw()
