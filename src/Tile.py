class Tile() :
    def __init__(self, X, Y):
        # X -> row, Y -> col
        self.bomb = False
        self.x , self.y = X, Y
        self.label = None

    def __repr__(self):
        return "X: (row) {}, Y: (col) {}, Label: {} , Bomb : {}".format(self.x, self.y, self.label, self.bomb)
