from src.utilities.utils import Utils

from src.chess_pieces.pawn import Pawn
from src.chess_pieces.knight import Knight
from src.chess_pieces.bishop import Bishop
from src.chess_pieces.rook import Rook
from src.chess_pieces.queen import Queen
from src.chess_pieces.king import King

from src.constants import CHESS_PIECES


class Opponent:

    @staticmethod
    def get_pawn_moves(board, position, opponent):
        return Pawn.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_knight_moves(board, position, opponent):
        return Knight.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_bishop_moves(board, position, opponent):
        return Bishop.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_rook_moves(board, position, opponent):
        return Rook.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_queen_moves(board, position, opponent):
        return Queen.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_king_moves(board, position, opponent):
        return King.get_opponent_moves(board, position, opponent)

    @staticmethod
    def get_king_position(board, player):
        for position in board:
            if not Utils.is_empty_square(board, position):
                chess_piece_name = board[position].name.lower()

                if player in chess_piece_name and 'king' in chess_piece_name:
                    break

        return position

    @staticmethod
    def get_chess_moves(board, position, opponent):
        chess_piece_name = board[position].name.lower()

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_piece_name and opponent in chess_piece_name:
                return getattr(Opponent, "get_" + chess_piece + "_moves")

        return None
