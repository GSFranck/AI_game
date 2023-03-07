import sys
import numpy as np



Black_start_row =[(0,0),(0,1),(0,2)]
Red_start_row = [(3,0),(3,1),(3,2)]

WinningScore=5#int(input("Max score:"))

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
        self.score = 0
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
        current_grid=self.grid.get_grid()
        possible_moves={}
        for piece in self.player.pawns:
            my_list=[]
            if piece.cord==(None,None):
                if self.player.color == 'Black':
                    
                    for field in Black_start_row:
                        if current_grid[field[0],field[1]]=="":
                            
                            my_list.append(field)
                    possible_moves[piece.name]=my_list
                    return possible_moves
                            


                elif self.player.color == 'Red':
                    for field in Red_start_row:
                        if self.grid.get_grid()[field[0],field[1]]=="":
                            
                            my_list.append(field)
                    possible_moves[piece.name]=my_list
                    return possible_moves
    
    def get_diagonal_moves(self):
        current_grid=self.grid.get_grid()
        possible_moves={}
        for piece in self.player.pawns:
            my_list=[]
            if piece.cord!=(None,None):
                if self.player.color == 'Black':
                    current_position=piece.cord
                    if current_position[0]==3:
                        potential_move=("Goal")
                        my_list.append(potential_move)
                    elif current_position[1]==0:
                        potential_move= (current_position[0]+1,current_position[1]+1)
                        if current_grid[potential_move[0],potential_move[1]]=="":
                            my_list.append(potential_move)

                    elif current_position[1]==1:
                        potential_move_1= (current_position[0]+1,current_position[1]+1)
                        potential_move_2= (current_position[0]+1,current_position[1]-1)
                        if current_grid[potential_move_1[0],potential_move_1[1]]=="":
                            my_list.append(potential_move_1)
                        if current_grid[potential_move_2[0],potential_move_2[1]]=="":
                            my_list.append(potential_move_2)

                    elif current_position[1]==2:
                        potential_move= (current_position[0]+1,current_position[1]-1)
                        if current_grid[potential_move[0],potential_move[1]]=="":
                            my_list.append(potential_move)

                    possible_moves[piece.name]=my_list
            
            
                elif self.player.color == 'Red':
                    current_position=piece.cord
                    if current_position[0]==0:
                        potential_move=("Goal")
                        my_list.append(potential_move)
                    if current_position[1]==0:
                        potential_move= (current_position[0]-1,current_position[1]+1)
                        if current_grid[potential_move[0],potential_move[1]]=="":
                            my_list.append(potential_move)

                    elif current_position[1]==1:
                        potential_move_1= (current_position[0]-1,current_position[1]+1)
                        potential_move_2= (current_position[0]-1,current_position[1]-1)
                        if current_grid[potential_move_1[0],potential_move_1[1]]=="":
                            my_list.append(potential_move_1)
                        if current_grid[potential_move_2[0],potential_move_2[1]]=="":
                            my_list.append(potential_move_2)

                    elif current_position[1]==2:
                        potential_move= (current_position[0]-1,current_position[1]-1)
                        if current_grid[potential_move[0],potential_move[1]]=="":
                            my_list.append(potential_move)

                    possible_moves[piece.name]=my_list
        return possible_moves
    
    def get_attacks(self):
        current_grid=self.grid.get_grid()
        possible_moves={}
        for piece in self.player.pawns:
            my_list=[]
            if piece.cord!=(None,None):
                if self.player.color == 'Black':
                    current_position=piece.cord
                    if current_position[0]==3:
                        continue
                    attack_position=(current_position[0]+1,current_position[1])
                    
                    if current_grid[attack_position[0],attack_position[1]]!="":
                        if current_grid[attack_position[0],attack_position[1]][0]=="R":
                            my_list.append(attack_position)
                if self.player.color == 'Red':
                    current_position=piece.cord
                    if current_position[0]==0:
                        continue
                    attack_position=(current_position[0]-1,current_position[1])
                    
                    if current_grid[attack_position[0],attack_position[1]]!="":
                        if current_grid[attack_position[0],attack_position[1]][0]=="B":
                            my_list.append(attack_position)
            possible_moves[piece.name]=my_list
        return possible_moves

    def get_jumps(self):
        current_grid=self.grid.get_grid()
        possible_moves={}
        for piece in self.player.pawns:
            my_list=[]
            if piece.cord!=(None,None):
                if self.player.color == 'Black':
                    current_position=piece.cord
                    if current_position[0]==3 or current_grid[current_position[0]+1,current_position[1]]=="":
                        continue
                    if current_grid[current_position[0]+1,current_position[1]][0]=="R":
                        if current_position[0]==2:
                            my_list.append(("Goal"))
                        else:
                            jump_column=current_grid[:,current_position[1]]
                            for i in range(current_position[0]+2,4):
                                if jump_column[i]=="":
                                    my_list.append((i,current_position[1]))
                                    break
                                elif jump_column[i][0]=="B":
                                    break
                                elif i==3:
                                    my_list.append(("Goal"))
                                elif jump_column[i][0]=="R":
                                    continue
                                
            

                else:
                    current_position=piece.cord
                    if current_position[0]==0 or current_grid[current_position[0]-1,current_position[1]]=="":
                        continue
                    if current_grid[current_position[0]-1,current_position[1]][0]=="B":
                        if current_position[0]==1:
                            my_list.append(("Goal"))
                        else:
                            jump_column=current_grid[:,current_position[1]]
                            for i in range(current_position[0]-2,0,-1):
                                if jump_column[i]=="":
                                    my_list.append((i,current_position[1]))
                                    break
                                elif jump_column[i][0]=="R":
                                    break
                                elif i==0:
                                    my_list.append(("Goal"))
                                elif jump_column[i][0]=="B":
                                    continue
                                
            possible_moves[piece.name]=my_list
        return possible_moves                       
                                

             
    def get_all_possible_moves(self):
        dict_1=self.get_spawns()
        dict_2=self.get_diagonal_moves()
        dict_3=self.get_attacks()
        dict_4=self.get_jumps()


        all_moves={'spawns':dict_1,'diagonals':dict_2,'attacks':dict_3,'jumps':dict_4}

        return all_moves






class Client:
    def __init__(self, grid=Grid, player=Player):
        self.grid=grid
        self.player=player
    def insert(self,dest):
        
        possible_moves=Action(self.player,self.grid).get_spawns()
        piece=list(possible_moves.keys())[0]
        self.grid.grid_mat[dest[0],dest[1]]=piece

        for pawn in self.player.pawns:
            if pawn.name==piece:
                pawn.cord=dest
        return self.grid

    def diagonal_move(self,piece,dest):
        grid_d= self.grid.grid_mat
        if dest==(None,None):
            for pawn in self.player.pawns:
                if pawn.name==piece:
                    current_cord=pawn.cord
                    grid_d[current_cord[0],current_cord[1]]=""
                    pawn.cord=dest
                    self.player.score+=1
            return self.grid

        grid_d[dest[0],dest[1]]=piece
        for pawn in self.player.pawns:
            if pawn.name==piece:
                current_cord=pawn.cord
                grid_d[current_cord[0],current_cord[1]]=""
                pawn.cord=dest
        return self.grid

    def attack_move(self,piece,piece_to_attack):
        grid_a= self.grid.grid_mat
        if self.player.color=='Black':
            opponent=Red_player
        else:
            opponent=Black_player
        
        for pawn in opponent.pawns:
            if pawn.name==piece_to_attack:
                opponent_cord=pawn.cord
                pawn.cord=(None,None)
        for pawn in self.player.pawns:
            if pawn.name==piece:
                grid_a[pawn.cord[0],pawn.cord[1]]=""
                pawn.cord=opponent_cord
        grid_a[opponent_cord[0],opponent_cord[1]]=piece
        
        return grid_a
    
    def jump_move(self,piece,dest):
        grid_d= self.grid.grid_mat
        if dest==(None,None):
            for pawn in self.player.pawns:
                if pawn.name==piece:
                    current_cord=pawn.cord
                    grid_d[current_cord[0],current_cord[1]]=""
                    pawn.cord=dest
                    self.player.score+=1
            return self.grid

        grid_d[dest[0],dest[1]]=piece
        for pawn in self.player.pawns:
            if pawn.name==piece:
                current_cord=pawn.cord
                grid_d[current_cord[0],current_cord[1]]=""
                pawn.cord=dest
        return self.grid



    


my_grid=Grid()
Black_player=Player('Black')
Red_player=Player('Red')
Black_actions=Action(Black_player,my_grid)
Red_actions=Action(Red_player,my_grid)

player_actions=Black_actions
player=Black_player

while Black_player.score<WinningScore and Red_player.score<WinningScore:
    current_grid=my_grid.get_grid()
    print(current_grid)
    Possible_actions=player_actions.get_all_possible_moves()
    print("\nChoose among the following moves:")
    move_list=[]
    move_no=0
    spawns=Possible_actions['spawns']
    for piece in spawns.keys():
        for i in spawns[piece]:
            print("{0}. Insert piece {1} at {2}".format(move_no,piece,i))
            move_no+=1
            move_list.append(('spawn',piece,i))
    diagonals=Possible_actions['diagonals']
    for piece in diagonals.keys():
        for i in diagonals[piece]:
            print("{0}. Move piece {1} to {2}".format(move_no,piece,i))
            move_no+=1
            if i=='Goal':
                i=(None,None)
            move_list.append(('diagonal',piece,i))

    jumps=Possible_actions['jumps']
    for piece in jumps.keys():
        for i in jumps[piece]:
            print("{0}. Jump with piece {1} to {2}".format(move_no,piece,i))
            move_no+=1
            if i=='Goal':
                i=(None,None)
            move_list.append(('jump',piece,i))
            
    
    attacks=Possible_actions['attacks']
    for piece in attacks.keys():
        for i in attacks[piece]:
            piece_to_attack=current_grid[i[0],i[1]]
            print("{0}. Attack piece {1} with {2}".format(move_no,piece_to_attack,piece))
            move_no+=1
            move_list.append(('attack',piece,piece_to_attack))

    InputAction= int(input("\nI choose action numnber:\n"))
    
    move= move_list[InputAction]
    move_type=move[0]
    move_piece=move[1]
    dest=move[2]
    
    player_interface=Client(my_grid,player)
    if move_type=='spawn':
        player_interface.insert(dest)
    elif move_type=='diagonal':
        player_interface.diagonal_move(move_piece,dest)
    elif move_type=='jump':
        player_interface.jump_move(move_piece,dest)
    elif move_type=='attack':
        player_interface.attack_move(move_piece,dest)

    if player.color=='Black':
        player_actions=Red_actions
        player=Red_player
    else:
        player_actions=Black_actions
        player=Black_player

    


    
    




 
