from src.chess_pieces.chess_type import ChessType
from src.utilities.utils import Utils
from src.constants import CHESS_PIECES


class ChessPiece:

    @staticmethod
    def get_moves(board, position):
        chess_type = board[position]

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_type.name.lower():
                break

        chess_move = getattr(ChessPiece, 'get_' + chess_piece + '_moves')

        return chess_move(board, position)

    @staticmethod
    def get_pawn_moves(board, position):
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

        else:
            x = position[0]
            y = position[1] - 1

            p = (x, y)

            if board[p] is None:
                positions.append(p)

        return Utils.get_rect_list(positions)

    @staticmethod
    def get_rook_moves(board, position):
        ...

    @staticmethod
    def get_knight_moves(board, position):
        ...

    @staticmethod
    def get_bishop_moves(board, position):
        ...

    @staticmethod
    def get_queen_moves(board, position):
        ...

    @staticmethod
    def get_king_moves(board, position):
        ...
