from kulibrat.player import Player
from kulibrat.board import Board
from kulibrat.action import Action
from kulibrat.client import Client
from agent import random_agent
from agent import minimax_agent

def is_actions(actions=Action):
    count=0
    Possible_actions=actions.get_all_possible_moves()
    #print(Possible_actions)
    for key in Possible_actions.keys():
        for move_type in Possible_actions[key].values():    
            count+=len(move_type)
    #print(count)
    if count == 0:
        return False
    else:
        return True

number_of_rounds = 100
black_wins = 0
red_wins = 0
is_legal_moves = True

for _ in range(number_of_rounds):
    game_board=Board()
    Black_player=Player("Black")
    Black_actions=Action(Black_player.color,game_board)
    Black_player.player_type="Minimax Agent"
    
    Red_player=Player("Red")
    Red_actions=Action(Red_player.color,game_board)
    Red_player.player_type="Random Agent"
    
    player_actions=Black_actions
    player=Black_player
    while game_board.winner() == None:
        player_interface=Client(player.color, game_board)
        Possible_actions=player_actions.get_all_possible_moves()
        move_list=[]
        move_no=0
        spawns=Possible_actions['spawns']
        for piece in spawns.keys():
            for dest in spawns[piece]:
                move_no+=1
                move_list.append(('spawn',piece,dest))

        diagonals=Possible_actions['diagonals']
        for piece in diagonals.keys():
            for dest in diagonals[piece]:
                move_no+=1
                if dest=='Goal':
                    dest=(None,None)
                move_list.append(('diagonal',piece,dest))
    
        jumps=Possible_actions['jumps']
        for piece in jumps.keys():
            for dest in jumps[piece]:
                move_no+=1
                if dest=='Goal':
                    dest=(None,None)
                move_list.append(('jump',piece,dest))
                
        attacks=Possible_actions['attacks']
        for piece in attacks.keys():
            for dest in attacks[piece]:
                piece_to_attack=game_board.get_piece_by_pos(dest[0],dest[1]).name
                move_no+=1
                move_list.append(('attack',piece,piece_to_attack))
        
        
        if player.player_type == "Minimax Agent":
            evaluation, move = minimax_agent.minimax(game_board, 3, player.color)
            if move == None:
                is_legal_moves = False
            move_type=move[0]
            move_piece=move[1]
            dest=move[2]
        
        else:
            if len(move_list) == 0:
                is_legal_moves = False
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
            #Red_posssible_actions = Red_actions.get_all_possible_moves()
            # Check if board is locked
            if not is_actions(player_actions) and not is_actions(Red_actions):
                game_board.is_locked(player.color, True)
            # Check if the other player has any moves if not dont change turn
            elif not is_actions(Red_actions):
                pass
            # change turn
            else:
                player_actions=Red_actions
                player = Red_player
    
        if color == "Red":
            #Black_posssible_actions = Black_actions.get_all_possible_moves()
            if not is_actions(player_actions) and not is_actions(Black_actions):
                game_board.is_locked(player.color, True)
            elif not is_actions(Black_actions):
                pass
            else:
                player = Black_player
                player_actions=Black_actions
    

    print("Black score:", game_board.black_score)
    print("Red score:", game_board.red_score)

    if game_board.winner() == "Black":
        black_wins +=1
    if game_board.winner() == "Red":
        red_wins +=1

print("Black wins: ", black_wins)
print("Red wins: ", red_wins)
