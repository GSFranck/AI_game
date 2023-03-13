from kulibrat.action import Action

def score(board):
    # print(player.score)
    return board.black_score - board.red_score

def distance_from_start(board):
    return board.get_distance_from_start("Black") - board.get_distance_from_start("Red")

def number_of_pieces(board):
    return len(board.get_pieces_on_grid("Black")) - len(board.get_pieces_on_grid("Red"))
    
def number_of_pieces_on_goal(board):
    len(board.get_pieces_on_goal("Black")) - len(board.get_pieces_on_goal("Red"))

def number_of_moves(board):
    black_actions = Action("Black", board)
    red_actions = Action("Red", board)
    return count_moves(black_actions) - count_moves(red_actions)

# helper function
def count_moves(actions=Action):
    count=0
    Possible_actions=actions.get_all_possible_moves()
    #print(Possible_actions)
    for key in Possible_actions.keys():
        for move_type in Possible_actions[key].values():    
            count+=len(move_type)
    return count