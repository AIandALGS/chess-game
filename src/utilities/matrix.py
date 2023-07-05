from src.constants import BOARD_FLIPS, BOARD_SIZE


class Matrix:
    @staticmethod
    def get_initial_matrix(board):
        return [[board[(x, y)] for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

    @staticmethod
    def rotate_board(board):
        mat = Matrix.get_initial_matrix(board)

        for _ in range(BOARD_FLIPS):
            mat = list(zip(*mat))[::-1]

            for y in range(BOARD_SIZE):
                for x in range(BOARD_SIZE):
                    position = (x, y)
                    board[position] = mat[y][x]

        return board
