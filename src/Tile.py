class Tile() :
    def __init__(self, X, Y):
        # X -> row, Y -> col
        self.x , self.y = X, Y
        self.bomb = False
        self.label = None
        self.revealed = False
        self.marked = False

    def __repr__(self):
        return "X: (row) {}, Y: (col) {}, Label: {} , Bomb : {}".format(self.x, self.y, self.label, self.bomb)
