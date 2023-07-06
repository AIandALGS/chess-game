from src.utilities.utils import Utils


class Pawn:

    @staticmethod
    def get_moves(board, position, player):
        x, y = position
        positions = []

        # Starting pawn move
        if y == 6:
            for k in range(2):
                delta = (x, y-k-1)

                if Utils.is_empty_square(board, delta):
                    positions.append(delta)
                else:
                    break

        # Single forward pawn move
        else:
            delta = (x, y-1)

            if Pawn.valid_forward_move(board, delta):
                positions.append(delta)

        # Diagonal pawn capture moves
        DX = [-1,  1]
        DY = [-1, -1]

        for dx, dy in zip(DX, DY):
            delta = (x+dx, y+dy)

            if Pawn.valid_diagonal_move(board, delta, player):
                positions.append(delta)

        # En Passant

        return positions

    @staticmethod
    def valid_forward_move(board, position):
        if not Utils.is_position_in_range(position):
            return False

        if not Utils.is_empty_square(board, position):
            return False

        return True

    @staticmethod
    def valid_diagonal_move(board, position, player):
        if not Utils.is_position_in_range(position):
            return False

        if Utils.is_empty_square(board, position):
            return False

        if not Utils.is_opponent_position(board, position, player):
            return False

        return True
