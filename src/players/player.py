from src.utilities.utils import Utils

from src.chess_pieces.pawn import Pawn
from src.chess_pieces.knight import Knight
from src.chess_pieces.bishop import Bishop
from src.chess_pieces.rook import Rook
from src.chess_pieces.queen import Queen
from src.chess_pieces.king import King

from src.constants import CHESS_PIECES


class Player:
    @staticmethod
    def get_pawn_moves(board, position, player):
        return Pawn.get_player_moves(board, position, player)

    @staticmethod
    def get_knight_moves(board, position, player):
        return Knight.get_player_moves(board, position, player)

    @staticmethod
    def get_bishop_moves(board, position, player):
        return Bishop.get_player_moves(board, position, player)

    @staticmethod
    def get_rook_moves(board, position, player):
        return Rook.get_player_moves(board, position, player)

    @staticmethod
    def get_queen_moves(board, position, player):
        return Queen.get_player_moves(board, position, player)

    @staticmethod
    def get_king_moves(board, position, player):
        return King.get_player_moves(board, position, player)

    @staticmethod
    def get_king_position(board, player):
        for position in board:
            if not Utils.is_empty_square(board, position):
                chess_piece_name = board[position].name.lower()

                if player in chess_piece_name and "king" in chess_piece_name:
                    break

        return position

    @staticmethod
    def get_chess_moves(board, position, player):
        chess_piece_name = board[position].name.lower()

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_piece_name and player in chess_piece_name:
                return getattr(Player, "get_" + chess_piece + "_moves")

        return None
