from src.utilities.utils import Utils


class King:
    @staticmethod
    def get_player_moves(board, position, player, opponent_moves):
        x, y = position
        positions = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                delta = (x + dx, y + dy)

                if not King.is_check(delta, opponent_moves):
                    if King.valid_move(board, delta, player):
                        positions.append(delta)

        return positions

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
