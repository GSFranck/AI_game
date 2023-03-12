from kulibrat.player import Player
from kulibrat.board import Board
from kulibrat.action import Action
from kulibrat.client import Client
from agent import random_agent
#from agent import minimax_agent

def check_locked_state(actions=Action):
    count=0
    Possible_actions=actions.get_all_possible_moves()
    #print(Possible_actions)
    for key in Possible_actions.keys():
        for move_type in Possible_actions[key].values():    
            count+=len(move_type)
    return count

WinningScore=5#int(input("Max score:"))

game_board=Board()
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
            "2. Human vs Minimax Agent\n")
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
else:
    Black_player.player_type="Human"
    Red_player.player_type="Human"



round_count=1
evaluation = 0

while game_board.winner() == None:
    player_interface=Client(player.color, game_board)

    if player.color=='Black':
        Black_move_count=check_locked_state(Black_actions)

        if Black_move_count==0:
            player_actions=Red_actions
            player=Red_player
            opppent=Black_player
    if player.color=='Red':
        Red_move_count=check_locked_state(Red_actions)

        if Red_move_count==0:
            player_actions=Black_actions
            player=Black_player
            opppent=Red_player

    print("********* ROUND {0} ********\n\n".format(round_count))
    print("Player turn: {0}".format(player.color))
    print("The score is:")
    print("Red: {0}".format(game_board.red_score))
    print("Black: {0}".format(game_board.black_score))
    game_board.draw_grid()

    #print("\nMinimax eval = ", evaluation)

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
    
    """
    if player.player_type == "Minimax Agent":
        evaluation, move = minimax_agent.minimax(my_grid, 3, player, opponent)
        move_type=move[0]
        move_piece=move[1]
        dest=move[2]
    """

    #else:
    if player.player_type=="Human":
        InputAction= int(input("\nI choose action number:\n"))
    else:
        InputAction=random_agent.random_action([i for i in range(0,len(move_list))])
    
    move= move_list[InputAction]
    move_type=move[0]
    move_piece=move[1]
    dest=move[2]
    
    if move_type=='spawn':
        player_interface.insert(move_piece, dest)
    elif move_type=='diagonal':
        player_interface.diagonal_move(move_piece,dest)
    elif move_type=='jump':
        player_interface.jump_move(move_piece,dest)
    elif move_type=='attack':
        print(dest)
        player_interface.attack_move(move_piece,dest)

    if game_board.winner() != None:
        print("{0} WINS THE GAME!!!!".format(game_board.winner()))

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
        opppent=Black_player
    elif player.color=='Red' and Red_move_count>0:
        player_actions=Black_actions
        player=Black_player
        opppent=Red_player
    
    round_count+=1

    