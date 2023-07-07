import copy

from src.players.player import Player
from src.players.opponent import Opponent
from src.utilities.utils import Utils
from src.chess_pieces.king import King


class ChessMove:
    @staticmethod
    def get_legal_moves(board, player):
        player_king_position = Player.get_king_position(board, player)
        legal_moves = dict()

        for position in board:
            player_moves = []

            if Utils.is_player_piece(board, position, player):
                chess_move = Player.get_chess_moves(board, position, player)

                if chess_move is not None:
                    possible_moves = chess_move(board, position, player)

                    for possible_move in possible_moves:
                        copy_board = copy.copy(board)
                        copy_board[position] = None
                        copy_board[possible_move] = board[position]

                        opponent_moves = ChessMove.get_opponent_moves(
                            copy_board, player
                        )

                        if not King.is_check(player_king_position, opponent_moves):
                            player_moves.append(possible_move)

                        copy_board[position] = board[position]
                        copy_board[possible_move] = None

            legal_moves[position] = Utils.get_rect_list(player_moves)

        opponent_moves = ChessMove.get_opponent_moves(board, player)
        king_moves = King.get_player_moves(
            board, player_king_position, player, opponent_moves)

        for king_move in king_moves:
            copy_board = copy.copy(board)
            copy_board[player_king_position] = None
            copy_board[king_move] = board[player_king_position]

            opponent_moves = ChessMove.get_opponent_moves(copy_board, player)

            if King.is_check(king_move, opponent_moves):
                king_moves.remove(king_move)

            copy_board[player_king_position] = board[player_king_position]
            copy_board[king_move] = None

        legal_moves[player_king_position] = Utils.get_rect_list(king_moves)

        return legal_moves

    @staticmethod
    def get_opponent_moves(board, player):
        opponent = Utils.get_opponent(player)
        opponent_king_position = Opponent.get_king_position(board, opponent)
        opponent_moves = set()

        for position in board:
            if not Utils.is_empty_square(board, position):
                chess_move = Opponent.get_chess_moves(
                    board, position, opponent)

                if chess_move is not None:
                    opponent_moves |= set(
                        chess_move(board, position, opponent))

        opponent_moves |= set(
            Opponent.get_king_moves(board, opponent_king_position, opponent)
        )

        return opponent_moves

    @staticmethod
    def get_number_of_legal_moves(legal_moves):
        count = 0

        for player_moves in legal_moves.values():
            count += len(player_moves)

        return count

    @staticmethod
    def is_check(board, player):
        player_king_position = Player.get_king_position(board, player)
        opponent_moves = ChessMove.get_opponent_moves(board, player)

        if not King.is_check(player_king_position, opponent_moves):
            return False

        return True

    @staticmethod
    def is_checkmate(board, player, legal_moves):
        player_king_position = Player.get_king_position(board, player)
        opponent_moves = ChessMove.get_opponent_moves(board, player)

        if not King.is_check(player_king_position, opponent_moves):
            return False

        if ChessMove.get_number_of_legal_moves(legal_moves) > 0:
            return False

        return True
