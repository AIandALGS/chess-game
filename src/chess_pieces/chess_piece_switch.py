from collections import defaultdict

from src.chess_pieces.chess_type import ChessType
from src.utilities.utils import Utils


class ChessPieceSwitch:
    @staticmethod
    def get_moves(board, position, chess_type):
        match chess_type:
            case ChessType.WHITE_PAWN:
                return ChessPieceSwitch.get_white_pawn_moves(board, position)

    @staticmethod
    def get_white_pawn_moves(board, position):
        positions = []

        if position[1] == 6:
            for height in range(2):
                x = position[0]
                y = position[1] - height - 1

                p = (x, y)

                if board[p] is None:
                    positions.append(p)
                else:
                    break

        return Utils.get_rect_list(positions)

    @staticmethod
    def get_rook_move(board, position, chess_type):
        ...

    @staticmethod
    def get_knight_move(board, position, chess_type):
        ...

    @staticmethod
    def get_bishop_move(board, position, chess_type):
        ...

    @staticmethod
    def get_queen_move(board, position, chess_type):
        ...

    @staticmethod
    def get_king_move(board, position, chess_type):
        ...
