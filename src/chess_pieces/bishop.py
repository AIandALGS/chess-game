from src.utilities.utils import Utils
from src.constants import BOARD_SIZE


class Bishop:

    @staticmethod
    def get_moves(board, position, player):
        x, y = position
        positions = []

        # Get left upper bishop diagonal
        dx, dy = x-1, y-1
        while dx >= 0 and dy >= 0:
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

            dx -= 1
            dy -= 1

        # Get right upper bishop diagonal
        dx, dy = x+1, y-1
        while dx < BOARD_SIZE and dy >= 0:
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

            dx += 1
            dy -= 1

        # Get left lower bishop diagonal
        dx, dy = x-1, y+1
        while dx >= 0 and dy < BOARD_SIZE:
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

            dx -= 1
            dy += 1

        # Get right lower bishop diagonal
        dx, dy = x+1, y+1
        while dx < BOARD_SIZE and dy < BOARD_SIZE:
            delta = (dx, dy)

            if not Utils.is_empty_square(board, delta):
                if Utils.is_opponent_position(board, delta, player):
                    positions.append(delta)
                    break
                else:
                    break

            positions.append(delta)

            dx += 1
            dy += 1

        return positions
