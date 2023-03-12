from kulibrat.board import Board
from kulibrat.action import *

class Client:
    def __init__(self, color=str, board=Board):
        self.color=color
        self.board=board

    # Note: here piece
    def insert(self,piece_name, dest):
        piece = self.board.get_piece_by_name(piece_name)
        self.board.move_piece(piece, dest[0], dest[1])

        return self.board

    def diagonal_move(self,piece_name,dest):
        piece = self.board.get_piece_by_name(piece_name)
        if dest==(None,None):
            self.board.move_piece(piece, dest[0], dest[1])
            self.board.update_score(self.color)
            return self.board

        self.board.move_piece(piece, dest[0], dest[1])
        return self.board

    def attack_move(self,piece_name,piece_to_attack_name):
        piece = self.board.get_piece_by_name(piece_name)
        if type(piece_to_attack_name) == str:
            piece_to_attack = self.board.get_piece_by_name(piece_to_attack_name)
        else:
            piece_to_attack = self.board.get_piece_by_pos(piece_to_attack_name)
        row, col = piece_to_attack.row, piece_to_attack.col
        self.board.remove_piece(piece_to_attack)
        self.board.move_piece(piece, row, col)
        return self.board
    
    def jump_move(self,piece_name,dest):
        piece = self.board.get_piece_by_name(piece_name)
        if dest==(None,None):
            self.board.move_piece(piece, dest[0], dest[1])
            self.board.update_score(self.color)
            return self.board
        
        self.board.move_piece(piece, dest[0], dest[1])
        return self.board
