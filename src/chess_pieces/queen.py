from src.chess_pieces.bishop import Bishop
from src.chess_pieces.rook import Rook


class Queen:

    @staticmethod
    def get_moves(board, position, player):
        positions = []

        positions.extend(Bishop.get_moves(board, position, player))
        positions.extend(Rook.get_moves(board, position, player))

        return positions
