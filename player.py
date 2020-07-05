
from tiles import *

class Player(object):
    def __init__(self, rack, isOut, name):
        self.rack = rack        # player's tile rack
        assert(Tiles.isRack(self.rack) and len(self.rack) == numStartTiles)
        self.isOut = isOut      # player has played tiles
        assert(self.isOut == False)
        self.name = name        # string

    def __eq__(self,other):
        return isinstance(other, Player) and self.name == other.name \
            and self.isOut == other.isOut and self.rack == other.rack


    def nextPlayer(self, Rum):
        index = Rum.players.index(self)



P1 = Player()