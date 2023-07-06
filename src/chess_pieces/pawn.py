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
        X = [-1,  1]
        Y = [-1, -1]

        for dx, dy in zip(X, Y):
            delta = (x+dx, y+dy)

            if Pawn.valid_diagonal_move(board, delta, player):
                positions.append(delta)

        # En Passant

        return positions

    @staticmethod
    def valid_forward_move(board, position):
        if Utils.is_position_in_range(position):
            if Utils.is_empty_square(board, position):
                return True

        return False

    @staticmethod
    def valid_diagonal_move(board, position, player):
        if Utils.is_position_in_range(position):
            if not Utils.is_empty_square(board, position):
                if Utils.is_opponent_position(board, position, player):
                    return True

        return False
