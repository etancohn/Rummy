
# SIGNATURE

# Tiles():

    # Tile(color, number, isJoker):
        # color : string
        # number : int "option"
        # isJoker : bool

    # makeDeck : unit -> deck
        # ENSURES : makeDeck() => returns a 106 tile deck
        # @staticmethod

    # isRack : list -> bool
        # ENSURES : isRack(L) => L is an int * string list
        # @staticmethod

    # isDeck : list -> bool
        # ENSURES : isDeck(L) => L is an int * string list
        # @staticmethod

    # createRack : int -> rack
        # REQUIRES : size < 106
        # ENSURES : createRack(size) => returns a rack with the given size.
        # optional parameter shuffled for whether you want the cards shuffled
        # @staticmethod
