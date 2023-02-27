import sys
import numpy as np

RedScore =0
BlackScore=0

WinningScore = 5 #sys.argv[1]



class Grid:
    ColumnSize = 3
    RowSize = 4

    def __init__(self,grid_mat= np.zeros((RowSize,ColumnSize))):

        self.grid_mat = grid_mat
    def get_grid(self):
        return self.grid_mat

class Pawn:
    def __init__(self,name:str):
        self.name = name
    def spawn_options(self,grid=Grid):
        
        if self.name[0] == 'B':
            return [i for i in [(0,0),(0,1),(0,2)] if grid.get_grid()[i[0],i[1]]==0]
        if self.name[0] == 'R':
            return [i for i in [(3,0),(3,1),(3,2)] if grid.get_grid()[i[0],i[1]]==0]

class Player:
    
    def __init__(self,color):
        self.color = color
        self.PawnsOnHand = 4
    def spawn_coords(self):
        if self.color == 'Black':
            return [(0,0),(0,1),(0,2)]
        if self.color == 'Red':
            return [(3,0),(3,1),(3,2)]
    def is_goal():


"""
    def insert(self,grid=Grid,Icord=tuple):
        if Icord in self.spawn_options(grid.get_grid()):
            self.grid.grid_mat[Icord]=self.name
"""


        
b1=Pawn('R1')
my_grid=Grid()
print(b1.spawn_options(my_grid))
b1.insert
"""

"""
    

