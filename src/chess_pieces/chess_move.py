from src.players.player import Player
from src.players.opponent import Opponent

from src.utilities.utils import Utils

from src.constants import CHESS_PIECES, BOARD_SIZE


class ChessMove:
    @staticmethod
    def get_moves(board, position, player):
        chess_type = board[position]

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_type.name.lower():
                break

        chess_move = getattr(Player, "get_" +
                             chess_piece + "_moves")
        positions = chess_move(board, position, player)

        ChessMove.get_legal_moves(board, player)

        return Utils.get_rect_list(positions)

    @staticmethod
    def get_legal_moves(board, player):
        opponent = Utils.get_opponent(player)
        print(opponent)

        legal_moves = []
        opponent_moves = set()

        for position in board:
            if not Utils.is_empty_square(board, position):
                chess_move = Opponent.get_chess_moves(
                    board, position, opponent)

                if chess_move is not None:
                    opponent_moves |= set(
                        chess_move(board, position, opponent))
