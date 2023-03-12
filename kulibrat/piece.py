class Piece:

    def __init__(self, row, col, name=str):
        self.row = row
        self.col = col
        self.name = name

    def move(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return str(self.name)