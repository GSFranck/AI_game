from kulibrat.game_setup import Grid
from kulibrat.game_setup import Player

Black_start_row =[(0,0),(0,1),(0,2)]
Red_start_row = [(3,0),(3,1),(3,2)]

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
                    elif current_position[1]==0:
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