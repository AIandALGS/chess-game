from src.utilities.utils import Utils


class Knight:
    @staticmethod
    def get_player_moves(board, position, player):
        x, y = position
        positions = []

        DX = [-2, -2, 2, 2, -1, 1, -1, 1]
        DY = [-1, 1, -1, 1, -2, -2, 2, 2]

        for dx, dy in zip(DX, DY):
            delta = (x + dx, y + dy)

            if Knight.valid_move(board, delta, player):
                positions.append(delta)

        return positions

    @staticmethod
    def get_opponent_moves(board, position, opponent):
        x, y = position
        positions = []

        DX = [-2, -2, 2, 2, -1, 1, -1, 1]
        DY = [-1, 1, -1, 1, -2, -2, 2, 2]

        for dx, dy in zip(DX, DY):
            delta = (x + dx, y + dy)

            if Utils.is_position_in_range(delta):
                positions.append(delta)

        return positions

    @staticmethod
    def valid_move(board, position, player):
        if not Utils.is_position_in_range(position):
            return False

        if not Utils.is_empty_square(board, position):
            if not Utils.is_opponent_position(board, position, player):
                return False

        return True
