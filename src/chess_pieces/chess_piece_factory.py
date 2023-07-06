from src.utilities.utils import Utils
from src.chess_pieces.pawn import Pawn
from src.chess_pieces.knight import Knight
from src.chess_pieces.bishop import Bishop
from src.chess_pieces.rook import Rook
from src.chess_pieces.queen import Queen


from src.constants import CHESS_PIECES


class ChessPieceFactory:
    @staticmethod
    def get_moves(board, position, player):
        chess_type = board[position]

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_type.name.lower():
                break

        chess_move = getattr(ChessPieceFactory, "get_" + chess_piece + "_moves")
        positions = chess_move(board, position, player)

        return Utils.get_rect_list(positions)

    @staticmethod
    def get_pawn_moves(board, position, player):
        return Pawn.get_moves(board, position, player)

    @staticmethod
    def get_knight_moves(board, position, player):
        return Knight.get_moves(board, position, player)

    @staticmethod
    def get_bishop_moves(board, position, player):
        return Bishop.get_moves(board, position, player)

    @staticmethod
    def get_rook_moves(board, position, player):
        return Rook.get_moves(board, position, player)

    @staticmethod
    def get_queen_moves(board, position, player):
        return Queen.get_moves(board, position, player)

    @staticmethod
    def get_king_moves(board, position, player):
        ...
