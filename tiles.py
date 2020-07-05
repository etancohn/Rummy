

from termcolor import colored, cprint
import random
from hofs import *

class Tiles(object):
    colors = ["blue", "red", "orange", "black"]

    # rummikub tile
    class Tile(object):   
        def __init__(self, color, number, isJoker):
            self.color = color
            self.number = number
            self.isJoker = isJoker

        def __eq__(self, other):
            return isinstance(other, Tiles.Tile) and self.color == other.color \
                    and self.number == other.number

        # def __repr__(self):
        #     if self.isJoker:
        #         return f"Tile(Joker, {self.color})"
        #     else:
        #         return f"Tile({self.number}, {self.color})"

        def __repr__(self):
            if self.isJoker:
                if self.color == "black":
                    return colored("J", "white", "on_grey")
                return colored("J", "white", "on_" + self.color)
            else:
                if self.color == "orange":
                    return colored(str(self.number), "grey", "on_yellow")
                elif self.color == "black":
                    return colored(str(self.number), "white", "on_grey")
                else:
                    return colored(str(self.number), "white", "on_" + self.color)

    # makeDeck : unit -> deck
    # ENSURES : makeDeck() => returns a 106 tile deck
    @staticmethod
    def makeDeck(shuffled = True):
        deck = []
        for i in range(2):
            for color in Tiles.colors:
                for num in range(1,14):
                    deck.append(Tiles.Tile(color, num, False))
        deck.append(Tiles.Tile("black", None, True))        # black Joker
        deck.append(Tiles.Tile("red", None, True))          # red Joker
        if shuffled:
            random.shuffle(deck)
        assert(Tiles.isDeck(deck))
        return deck


    # isRack : list -> bool
    # ENSURES : isRack(L) => L is an int * string list
    @staticmethod
    def isRack(L):
        for e in L:
            if not(isinstance(e, Tiles.Tile)):
                return False
        return True 

    # isDeck : list -> bool
    # ENSURES : isDeck(L) => L is an int * string list
    @staticmethod
    def isDeck(L):
        return Tiles.isRack(L)

    # createRack : int -> rack
    # REQUIRES : size < 106
    # ENSURES : createRack(size) => returns a rack with the given size.
    # optional parameter shuffled for whether you want the cards shuffled
    @staticmethod
    def createRack(size, shuffled = True):
        assert(size < 106)
        deck = Tiles.makeDeck(shuffled)
        res = deck[:size]
        assert(Tiles.isRack(res))
        return res
        


# TESTS

T = Tiles()
deck = T.makeDeck()
print(f"deck length: {len(deck)}")

filtered = filter(lambda T : T.number == 5, deck)
colors = [x.color for x in filtered]
numbers = [x.number for x in filtered]

blue2 = Tiles.Tile("blue", 2, False)





