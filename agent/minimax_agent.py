import sys
sys.path.append('..')
from copy import deepcopy

from kulibrat.board import Board
from kulibrat.client import Client
from kulibrat.action import Action

def minimax(board, depth, color, best_move=None):
    #print(board)
    if depth == 0 or board.winner() != None: # or win or lock
        return evaluate_result(board), best_move
    
    #print(player.color)
    if color == "Black":
        max_player = True
    else:
        max_player = False

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for result in get_all_results(board, color):
            evaluation = minimax(result[0], depth-1, "Red", best_move)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = result[1]
            
        return maxEval, best_move
    
    else:
        minEval = float('inf')
        best_move = None
        for result in get_all_results(board, color):
            evaluation = minimax(result[0], depth-1, "Black", best_move)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = result[1]
                    
        return minEval, best_move


def simulate_move(move, client):
    move_type=move[0]
    move_piece_name=move[1]
    dest=move[2]
    #print(move_type)
    #print(move_piece_name)
    #print(dest)
    if move_type=='spawn':
        return client.insert(move_piece_name, dest)
    elif move_type=='diagonal':
        return client.diagonal_move(move_piece_name,dest)
    elif move_type=='jump':
        return client.jump_move(move_piece_name,dest)
    elif move_type=='attack':
        return client.attack_move(move_piece_name,dest)

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
    
    #print(move_list)
    for move in move_list:
        temp_board = deepcopy(board)
        interface = Client(color, temp_board)
        #print(temp_grid.get_grid())
        result = simulate_move(move, interface)  
        #print(move)
        results.append((result, move))
    #print(move_list)
    #print(results[1].get_grid())
    return results

def evaluate_result(board):
    # print(player.score)
    return board.black_score - board.red_score



"""""

player_ = Player("Black")
opponent_ = Player("Red")
grid = Grid()
get_all_results(opponent_, player_, grid)
eval, best_move = minimax(grid, 8, player_, opponent_)
print(eval)
print(best_move)

"""""