from kulibrat.piece import Piece

COLS = 3
ROWS = 4

class Board:

    def __init__(self, max_score=5):
        self.grid = []
        self.max_score=max_score
        self.black_score = self.red_score= 0
        self.black_pieces=[
            Piece(None,None,"B1"),
            Piece(None,None,"B2"),
            Piece(None,None,"B3"),
            Piece(None,None,"B4")
                    ]
        self.red_pieces=[
            Piece(None,None,"R1"),
            Piece(None,None,"R2"),
            Piece(None,None,"R3"),
            Piece(None,None,"R4")
                    ]
        
        self.create_grid()

    def evaluate(self):
        return self.black_score - self.red_score

    def get_pieces(self, color):
        if color == "Black":
            return self.black_pieces
        if color == "Red":
            return self.red_pieces

    def get_piece_by_pos(self, row, col):
        return self.grid[row][col]

    def get_piece_by_name(self, name):
            all_pieces = self.black_pieces + self.red_pieces
            for piece in all_pieces:
                if piece.name == name:
                    return piece

    def create_grid(self):
        for row in range(ROWS):
            self.grid.append([])
            for col in range(COLS):
                self.grid[row].append(0)
        
    def draw_grid(self):
        print_values=[]
        for row in range(ROWS):
            for col in range(COLS):   
                if self.grid[row][col]==0:
                    print_values.append('  ')
                else:
                    print_values.append(self.grid[row][col].name)           
        print("+--+--+--+")
        print("|{0}|{1}|{2}|".format(print_values[0],print_values[1],print_values[2]))
        print("+--+--+--+")
        print("|{0}|{1}|{2}|".format(print_values[3],print_values[4],print_values[5]))
        print("+--+--+--+")
        print("|{0}|{1}|{2}|".format(print_values[6],print_values[7],print_values[8]))
        print("+--+--+--+")
        print("|{0}|{1}|{2}|".format(print_values[9],print_values[10],print_values[11]))
        print("+--+--+--+")

    def remove_piece(self, piece):
        self.grid[piece.row][piece.col] = 0
        piece.move(None,None)
    
    def move_piece(self, piece, row, col):
        if piece.row != None:
            self.grid[piece.row][piece.col] = 0

        if row != None:
            self.grid[row][col] = piece

        piece.move(row, col)

    def update_score(self, color):
        if color == "Black":
            self.black_score+=1
        
        elif color == "Red":
            self.red_score+=1
    
    def is_locked(self, loser_color=None, locked=False):
        if locked:
            if loser_color == "Black":
                return self.winner("Red")
            else:
                return self.winner("Black")
    
    def winner(self, winner_color=None):
        if self.black_score == self.max_score:
            return "BLACK"
        elif self.red_score == self.max_score:
            return "RED"
        elif winner_color != None:
            return winner_color
        
        return None 
    