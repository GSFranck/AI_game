import numpy as np

from kulibrat.player import Player
from kulibrat.board import Board
from kulibrat.action import Action
from kulibrat.client import Client
from agent import random_agent
from agent import alpha_beta_agent
from agent.evaluation_functions import EvaluationFunctions

def is_actions(actions=Action):
    count=0
    Possible_actions=actions.get_all_possible_moves()
    for key in Possible_actions.keys():
        for move_type in Possible_actions[key].values():    
            count+=len(move_type)
    if count == 0:
        return False
    else:
        return True
WinningScore = 5 #int(input("Max score:"))
depth = 5 # minimax search depth
locked_state = False
is_legal_moves = True
round_count=1

eval_funcs = EvaluationFunctions()
game_board=Board(WinningScore)
Black_player=Player("Black")
Red_player=Player("Red")
Black_actions=Action(Black_player.color,game_board)
PosMoves = Black_actions.get_all_possible_moves()
Red_actions=Action(Red_player.color,game_board)

player_actions=Black_actions
player=Black_player
game_intro=("\nHow would you like to play?\n"
            "0. Human vs. Human\n"
            "1. Human vs. Random Agent\n"
            "2. Human vs Minimax Agent\n"
            "3. Minimax Agent vs Random Agent\n")
print(game_intro)
game_mode=int(input())

if game_mode==1 or game_mode==2:
    human_color=int(input("\nWould you like to be the Black or Red player?\n"
                          "0. Black\n"
                          "1. Red\n"))
    if human_color==0 and game_mode==1:
        Black_player.player_type="Human"
        Red_player.player_type="Radom Agent"
    elif human_color==1 and game_mode==1:
        Black_player.player_type="Radom Agent"
        Red_player.player_type="Human"
    elif human_color==1 and game_mode==2:
        Black_player.player_type="Minimax Agent"
        Red_player.player_type="Human"
    elif human_color==0 and game_mode==2:
        Black_player.player_type="Human"
        Red_player.player_type="Minimax Agent"
elif game_mode == 0:
    Black_player.player_type="Human"
    Red_player.player_type="Human"
else:
    Black_player.player_type="Random Agent"
    Red_player.player_type="Minimax Agent"

while game_board.winner(locked_state, player.color) == None:
    player_interface=Client(player.color, game_board)

    print("********* ROUND {0} ********\n\n".format(round_count))
    print("Player turn: {0}".format(player.color))
    print("The score is:")
    print("Red: {0}".format(game_board.red_score))
    print("Black: {0}".format(game_board.black_score))
    game_board.draw_grid()

    Possible_actions=player_actions.get_all_possible_moves()
    print("\nChoose among the following moves:")
    move_list=[]
    move_no=0
    spawns=Possible_actions['spawns']
    for piece in spawns.keys():
        for dest in spawns[piece]:
            print("{0}. Insert piece {1} at {2}".format(move_no,piece,dest))
            move_no+=1
            move_list.append(('spawn',piece,dest))
    diagonals=Possible_actions['diagonals']
    for piece in diagonals.keys():
        for dest in diagonals[piece]:
            print("{0}. Move piece {1} to {2}".format(move_no,piece,dest))
            move_no+=1
            if dest=='Goal':
                dest=(None,None)
            move_list.append(('diagonal',piece,dest))

    jumps=Possible_actions['jumps']
    for piece in jumps.keys():
        for dest in jumps[piece]:
            print("{0}. Jump with piece {1} to {2}".format(move_no,piece,dest))
            move_no+=1
            if dest=='Goal':
                dest=(None,None)
            move_list.append(('jump',piece,dest))
            
    attacks=Possible_actions['attacks']
    for piece in attacks.keys():
        for dest in attacks[piece]:
            piece_to_attack=game_board.get_piece_by_pos(dest[0],dest[1]).name
            print("{0}. Attack piece {1} with {2}".format(move_no,piece_to_attack,piece))
            move_no+=1
            move_list.append(('attack',piece,piece_to_attack))
    
    
    if player.player_type == "Minimax Agent":
        evaluation, move = alpha_beta_agent.minimax_alpha_beta(game_board, depth, player.color, eval_funcs.linear, float('-inf'), float('inf'))
        if move == None:
            is_legal_moves = False
        else:
            move_type=move[0]
            move_piece=move[1]
            dest=move[2]
    
    else:
        if player.player_type=="Human":
            InputAction= int(input("\nI choose action number:\n"))
        else:
            InputAction=random_agent.random_action([i for i in range(0,len(move_list))])

        move= move_list[InputAction]
        move_type=move[0]
        move_piece=move[1]
        dest=move[2]
    
    if is_legal_moves:
        if move_type=='spawn':
            player_interface.insert(move_piece, dest)
        elif move_type=='diagonal':
            player_interface.diagonal_move(move_piece,dest)
        elif move_type=='jump':
            player_interface.jump_move(move_piece,dest)
        elif move_type=='attack':
            player_interface.attack_move(move_piece,dest)
    
    # Change player turn
    color = player.color
    if color == "Black":
        # Check if board is locked
        if not is_actions(player_actions) and not is_actions(Red_actions):
            locked_state = True
            player = Red_player
        # Check if the other player has any moves if not dont change turn
        elif not is_actions(Red_actions):
            pass
        # change turn
        else:
            player_actions=Red_actions
            player = Red_player

    if color == "Red":
        if not is_actions(player_actions) and not is_actions(Black_actions):
            locked_state = True
            player = Black_player
        elif not is_actions(Black_actions):
            pass
        else:
            player = Black_player
            player_actions=Black_actions
                                       
    if game_board.winner(locked_state, player.color) != None:
            game_board.draw_grid()
            print("The score is:")
            print("Red: {0}".format(game_board.red_score))
            print("Black: {0}".format(game_board.black_score))
            print("{0} WINS THE GAME!!!!".format(game_board.winner(locked_state, player.color)))

    round_count+=1

    