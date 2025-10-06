class GameState:
    def __init__(self, difficulty="EASY"):
        self.difficulty = difficulty
        self.NUM_BOMBS = None
        self.GRID_SIZE = None
        self.CELL_SIZE = None
        self.WINDOW_SIZE = None
        self.FONT_SIZE = None
        self.FONT = None
        
        self.screen = None
        self.marked_bombs = None
        self.grid = None
        self.buttons = None