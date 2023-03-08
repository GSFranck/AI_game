import numpy as np


class Grid:
    ColumnSize = 3
    RowSize = 4

    def __init__(self,grid_mat= np.zeros((RowSize,ColumnSize),dtype="U2")):
        self.grid_mat = grid_mat
        
    def get_grid(self):
        return self.grid_mat

class Pawn:
    def __init__(self,name:str,cord=(None,None)):
        self.name = name
        self.cord = cord

class Player:
    
    def __init__(self,color=str):
        self.color = color
        self.score = 0
        self.player_type=None
        if self.color=='Black':
            self.pawns=[
                Pawn("B1",(None,None)),
                Pawn("B2",(None,None)),
                Pawn("B3",(None,None)),
                Pawn("B4",(None,None))
            ]
            
        else:
            self.pawns=[
                Pawn("R1",(None,None)),
                Pawn("R2",(None,None)),
                Pawn("R3",(None,None)),
                Pawn("R4",(None,None))
            ]

