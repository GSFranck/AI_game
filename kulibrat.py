from kulibrat.game_setup import Player, Grid
from kulibrat.action import *
from agent import random_agent



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

def check_locked_state(actions=Action):
        count=0
        Possible_actions=actions.get_all_possible_moves()
        

        for key in Possible_actions.keys():
            for move_type in Possible_actions[key].values():
                
                count+=len(move_type)
        return count


WinningScore=5#int(input("Max score:"))

my_grid=Grid()
Black_player=Player('Black')
Red_player=Player('Red')
Black_actions=Action(Black_player,my_grid)
Red_actions=Action(Red_player,my_grid)

player_actions=Black_actions
player=Black_player

game_intro=("\nHow would you like to play?\n"
            "0. Human vs. Human\n"
            "1. Human vs. Random Agent")
print(game_intro)
game_mode=int(input())

if game_mode==1:
    human_color=int(input("\nWould you like to be the Black or Red player?\n"
                          "0. Black\n"
                          "1. Red\n"))
    if human_color==0:
        Black_player.player_type="Human"
        Red_player.player_type="Radom Agent"
    else:
        Black_player.player_type="Radom Agent"
        Red_player.player_type="Human"
else:
    Black_player.player_type="Human"
    Red_player.player_type="Human"



round_count=1

while Black_player.score<WinningScore and Red_player.score<WinningScore:

    if player.color=='Black':
        Black_move_count=check_locked_state(Black_actions)

        if Black_move_count==0:
            player_actions=Red_actions
            player=Red_player
    if player.color=='Red':
        Red_move_count=check_locked_state(Red_actions)

        if Red_move_count==0:
            player_actions=Black_actions
            player=Black_player

    print("********* ROUND {0} ********\n\n".format(round_count))
    print("Player turn: {0}".format(player.color))
    print("The score is:")
    print("Red: {0}".format(Red_player.score))
    print("Black: {0}".format(Black_player.score))
    current_grid=my_grid.get_grid()
    print_values=[]
    for i in range(0,4):
        for j in range(0,3):
            if current_grid[i,j]=='':
                print_values.append('  ')
            else:
                print_values.append(current_grid[i,j])
    print("+--+--+--+")
    print("|{0}|{1}|{2}|".format(print_values[0],print_values[1],print_values[2]))
    print("+--+--+--+")
    print("|{0}|{1}|{2}|".format(print_values[3],print_values[4],print_values[5]))
    print("+--+--+--+")
    print("|{0}|{1}|{2}|".format(print_values[6],print_values[7],print_values[8]))
    print("+--+--+--+")
    print("|{0}|{1}|{2}|".format(print_values[9],print_values[10],print_values[11]))
    print("+--+--+--+")

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
    if player.player_type=="Human":
        InputAction= int(input("\nI choose action number:\n"))
    else:
        InputAction=random_agent.random_action([i for i in range(0,len(move_list))])
    
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

    if player.score==WinningScore:
        print("{0} WINS THE GAME!!!!".format(player.color))

    Black_move_count=check_locked_state(Black_actions)
    Red_move_count=check_locked_state(Red_actions)
    Statelocked=Black_move_count+Red_move_count
    if Statelocked==0:
        if player.color=='Black':
            print("Red Player wins, due to the Black player locking the game")
            break
        elif player.color=='Red':
            print("Black Player wins, due to the Red player locking the game")
            break
    
    if player.color=='Black' and Black_move_count>0:
        player_actions=Red_actions
        player=Red_player
    elif player.color=='Red' and Red_move_count>0:
        player_actions=Black_actions
        player=Black_player
    
    round_count+=1

    