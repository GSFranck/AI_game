import sys
sys.path.append('..')
from copy import deepcopy

from kulibrat.board import Board
from kulibrat.client import Client
from kulibrat.action import Action

def minimax_alpha_beta(board, depth, color, eval_func, alpha, beta, best_move=None, locked_state = False):
    if len(get_all_results(board, "Black")) + len(get_all_results(board, "Red")) == 0:
        locked_state = True
    if depth == 0 or board.winner(locked_state, color) != None: 
        return eval_func(board, color, locked_state), best_move

    if color == "Black":
        max_player = True
    else:
        max_player = False

    if max_player:
        
        if len(get_all_results(board, color)) == 0:
            maxEval = eval_func(board, color, locked_state)
            best_move = None
        else:
            maxEval = float('-inf')
            best_move = None
            for result in get_all_results(board, color):
                evaluation = minimax_alpha_beta(result[0], depth-1, "Red", eval_func, alpha, beta, best_move)[0]
                maxEval = max(maxEval, evaluation)
                alpha = max(alpha, evaluation)
                if maxEval == evaluation:
                    best_move = result[1]
                if beta <= alpha:
                    break

        return maxEval, best_move
    
    else:
        if len(get_all_results(board, color)) == 0:
            minEval = eval_func(board, color, locked_state)
            best_move = None

        else:
            minEval = float('inf')
            best_move = None
            for result in get_all_results(board, color):
                evaluation = minimax_alpha_beta(result[0], depth-1, "Black", eval_func, alpha, beta, best_move)[0]
                minEval = min(minEval, evaluation)
                beta = min(beta, evaluation)
                if minEval == evaluation:
                    best_move = result[1]
                if beta <= alpha:
                    break
                    
        return minEval, best_move


def simulate_move(move, client):
    move_type=move[0]
    move_piece_name=move[1]
    dest=move[2]
    if move_type=='jump':
        return client.jump_move(move_piece_name, dest)
    elif move_type=='diagonal':
        return client.diagonal_move(move_piece_name,dest)
    elif move_type=='attack':
        return client.attack_move(move_piece_name,dest)
    elif move_type=='spawn':
        return client.insert(move_piece_name,dest)

def get_all_results(board, color):
    results = []
    Possible_actions = Action(color, board).get_all_possible_moves()
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
            piece_to_attack=board.get_piece_by_pos(dest[0],dest[1]).name
            move_no+=1
            move_list.append(('attack',piece,piece_to_attack))
    
    for move in move_list:
        temp_board = deepcopy(board)
        interface = Client(color, temp_board)
        result = simulate_move(move, interface)
        results.append((result, move))
    return results




