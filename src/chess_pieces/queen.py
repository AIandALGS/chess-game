from src.chess_pieces.bishop import Bishop
from src.chess_pieces.rook import Rook


class Queen:
    @staticmethod
    def get_player_moves(board, position, player):
        positions = []

        positions.extend(Bishop.get_player_moves(board, position, player))
        positions.extend(Rook.get_player_moves(board, position, player))

        return positions

    @staticmethod
    def get_opponent_moves(board, position, opponent):
        return Queen.get_player_moves(board, position, opponent)
