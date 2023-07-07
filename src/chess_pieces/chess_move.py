from copy import deepcopy
from src.chess_pieces.king import King

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
        player_king_position = Player.get_king_position(board, player)
        legal_moves = dict()

        for position in board:
            player_moves = []

            if not Utils.is_empty_square(board, position):
                chess_move = Player.get_chess_moves(
                    board, position, player)

                if chess_move is not None:
                    possible_moves = chess_move(board, position, player)

                    for possible_move in possible_moves:
                        copy_board = deepcopy(board)
                        copy_board[possible_move] = board[position]
                        opponent_moves = ChessMove.get_opponent_moves(
                            copy_board, player)

                        if not King.is_check(player_king_position, opponent_moves):
                            player_moves.append(possible_move)

                        copy_board[position] = board[position]

            legal_moves[position] = Utils.get_rect_list(player_moves)

        legal_moves[player_king_position] = Utils.get_rect_list(
            King.get_player_moves(board, player_king_position, player, opponent_moves))

        return legal_moves

    @staticmethod
    def get_opponent_moves(board, player):
        opponent = Utils.get_opponent(player)
        opponent_moves = set()

        for position in board:
            if not Utils.is_empty_square(board, position):
                chess_move = Opponent.get_chess_moves(
                    board, position, opponent)

                if chess_move is not None:
                    opponent_moves |= set(
                        chess_move(board, position, opponent))

        return opponent_moves
