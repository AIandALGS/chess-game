from src.utilities.utils import Utils
from src.constants import (
    KING_POSITION,
    LEFT_KING_POSITION,
    RIGHT_KING_POSITION,
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

        king_not_moved = castling_rights[KING_POSITION]

        if king_not_moved and not King.is_check(KING_POSITION, opponent_moves):
            if King.check_castle_left(board, castling_rights):
                positions.append(LEFT_KING_POSITION)

            if King.check_castle_right(board, castling_rights):
                positions.append(RIGHT_KING_POSITION)

        return positions

    @staticmethod
    def check_castle_left(board, castling_rights):
        if not castling_rights[LEFT_ROOK_POSITION]:
            return False

        x, y = KING_POSITION

        for k in range(3):
            dx = x - k - 1
            dy = y
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                return False

        return True

    @staticmethod
    def check_castle_right(board, castling_rights):
        if not castling_rights[RIGHT_ROOK_POSITION]:
            return False

        x, y = KING_POSITION

        for k in range(2):
            dx = x + k + 1
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
