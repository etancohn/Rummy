

class State(object):
    def __init__(self, currentPlayer, pool, isOver):
        self.currentPlayer = currentPlayer          # whose turn it is
        self.pool = pool                            # tile pool
        self.isOver = isOver                        # game completed



