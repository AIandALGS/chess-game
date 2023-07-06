from src.utilities.utils import Utils
from src.constants import BOARD_SIZE


class Rook:
    @staticmethod
    def get_moves(board, position, player):
        x, y = position
        positions = []

        # Get left rook moves
        for dx in range(x - 1, -1, -1):
            delta = (dx, y)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

        # Get right rook moves
        for dx in range(x + 1, BOARD_SIZE):
            delta = (dx, y)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

        # Get upper rook moves
        for dy in range(y - 1, -1, -1):
            delta = (x, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

        # Get lower rook moves
        for y in range(y + 1, BOARD_SIZE):
            delta = (x, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

        return positions
