from kulibrat.action import Action
W1 = 5
W2 = 4
W3 = 3
W4 = 2
W5 = 1

class EvaluationFunctions:

    def score(self, board):
        return board.black_score - board.red_score

    def forward(self, board):
       return board.get_distance_from_start("Black") - board.get_distance_from_start("Red")

    def most_pieces(self, board):
        return len(board.get_pieces_on_grid("Black")) - len(board.get_pieces_on_grid("Red"))
    
    def block(self, board):
        return len(board.get_pieces_on_goal("Black")) - len(board.get_pieces_on_goal("Red"))

    def limit(self, board):
        black_actions = Action("Black", board)
        red_actions = Action("Red", board)
        return self._count_moves(black_actions) - self._count_moves(red_actions)

    def linear(self, board, color, locked_state):

        if board.winner(locked_state, color) == "Black":
            evaluation = 1000
        elif board.winner(locked_state, color) == "Red":
            evaluation = -1000
        else:
            evaluation = W5*self.most_pieces(board)+W4*self.forward(board)+W3*self.score(board)+W2*self.block(board)+W1*self.limit(board)
        return evaluation
    
    def non_linear(self, board, color, locked_state):
        if board.winner(locked_state, color) == "Black":
            evaluation = 1000
        elif board.winner(locked_state, color) == "Red":
            evaluation = -1000
        else:        
            if color == "Black":
                score = board.black_score+1
            else:
                score = board.black_score+1
            evaluation = W5*1/score*self.most_pieces(board)+W4*self.forward(board)+W3*self.score(board)+W2*1/score*self.block(board)+W1*1/score*self.limit(board)
        return evaluation
            
    # helper function
    def _count_moves(sefl, actions=Action):
        count=0
        Possible_actions=actions.get_all_possible_moves()
        for key in Possible_actions.keys():
            for move_type in Possible_actions[key].values():    
                count+=len(move_type)
        return count 


