from src.utilities.utils import Utils
from src.constants import (
    BOARD_SIZE,
    WHITE_KING_POSITION,
    WHITE_KING_LEFT_POSITION,
    WHITE_KING_RIGHT_POSITION,
    BLACK_KING_POSITION,
    BLACK_KING_LEFT_POSITION,
    BLACK_KING_RIGHT_POSITION,
    LEFT_ROOK_POSITION,
    RIGHT_ROOK_POSITION,
)


class King:
    @staticmethod
    def get_player_moves(board, position, player, opponent_moves, castling_rights):
        x, y = position
        positions = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                delta = (x + dx, y + dy)

                if not King.is_check(delta, opponent_moves):
                    if King.valid_move(board, delta, player):
                        positions.append(delta)

        king_position = WHITE_KING_POSITION if player == "white" else BLACK_KING_POSITION
        left_king_position = WHITE_KING_LEFT_POSITION if player == "white" else BLACK_KING_LEFT_POSITION
        right_king_position = WHITE_KING_RIGHT_POSITION if player == "white" else BLACK_KING_RIGHT_POSITION

        player_castling_rights = castling_rights[player]
        king_not_moved = player_castling_rights[king_position]

        if king_not_moved and not King.is_check(king_position, opponent_moves):
            if King.check_castle_left(board, king_position, player_castling_rights):
                positions.append(left_king_position)

            if King.check_castle_right(board, king_position, player_castling_rights):
                positions.append(right_king_position)

        return positions

    @staticmethod
    def check_castle_left(board, king_position, castling_rights):
        if not castling_rights[LEFT_ROOK_POSITION]:
            return False

        x, y = king_position

        for k in range(x - 1):
            dx = k + 1
            dy = y
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                return False

        return True

    @staticmethod
    def check_castle_right(board, king_position, castling_rights):
        if not castling_rights[RIGHT_ROOK_POSITION]:
            return False

        x, y = king_position

        for k in range(x, BOARD_SIZE - 2):
            dx = k + 1
            dy = y
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                return False

        return True

    @staticmethod
    def get_opponent_moves(board, position, opponent):
        x, y = position
        positions = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                delta = (x + dx, y + dy)

                if Utils.is_position_in_range(delta):
                    positions.append(delta)

        return positions

    @staticmethod
    def is_check(king_position, opponent_positions):
        return king_position in opponent_positions

    @staticmethod
    def valid_move(board, position, player):
        if not Utils.is_position_in_range(position):
            return False

        if not Utils.is_empty_square(board, position):
            if not Utils.is_opponent_position(board, position, player):
                return False

        return True
