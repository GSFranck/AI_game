import sys
import numpy as np

RedScore =0
BlackScore=0

Black_start_row =[(0,0),(0,1),(0,2)]
Red_start_row = [(3,0),(3,1),(3,2)]

WinningScore = 5 #sys.argv[1]



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
    
    def __init__(self,color=str,pawns=None):
        self.color = color
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




class Action:
    def __init__(self,player=Player,grid=Grid):
        self.player=player
        self.grid=grid
        
    def get_spawns(self):
        possible_moves={}
        for piece in self.player.pawns:
            my_list=[]
            if piece.cord==(None,None):
                if self.player.color == 'Black':
                    
                    for field in Black_start_row:
                        if self.grid.get_grid()[field[0],field[1]]=="":
                            
                            my_list.append(field)
                    possible_moves[piece.name]=my_list
                    return possible_moves
                            


                elif self.player.color == 'Red':
                    for field in Red_start_row:
                        if self.grid.get_grid()[field[0],field[1]]=="":
                            
                            my_list.append(field)
                    possible_moves[piece.name]=my_list
                    return possible_moves
    

    def get_all_actions(self):
        return self.get_spawns()


class Client:
    def __init__(self, grid=Grid, player=Player):
        self.grid=grid
        self.player=player
    def insert(self,dest):
        
        possible_moves=Action(self.player,self.grid).get_all_actions()
        piece=list(possible_moves.keys())[0]
        self.grid.grid_mat[dest[0],dest[1]]=piece

        for pawn in self.player.pawns:
            if pawn.name==piece:
                pawn.cord=dest
        return self.grid

"""         
    def get_diagonals(self):
        diagonals={}
        if self.player.color == 'Black':
            for piece in self.player.pawns:
                piece_cord=piece.cord
                if piece_cord!=(None,None):
                    if 0<piece_cord[1]<3:

                    
                
                    

                elif self.player.color == 'Red':
                    for field in Red_start_row:
                        if self.grid.get_grid()[field[0],field[1]]=="":
                            spawns[piece.name]=field
"""
    


my_grid=Grid()
Gustav=Player('Black')
Line=Player('Red')
Gustav_actions=Action(Gustav,my_grid)
Line_actions=Action(Line,my_grid)
#print(Gustav_actions.get_all_actions())
#print(Line_actions.get_spawns())
interface = Client(my_grid,Gustav)
interface = Client(my_grid,Line)
"""
interface.insert((0,2))
print(my_grid.grid_mat)
for i in Gustav.pawns:
    print(i.name,i.cord)
"""

wtd= input("Your possible actions are:\n {}".format(Gustav_actions.get_all_actions()))




 
