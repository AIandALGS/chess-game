from src.utilities.utils import Utils
from src.chess_pieces.pawn import Pawn
from src.chess_pieces.rook import Rook


from src.constants import CHESS_PIECES, BOARD_SIZE


class ChessPiece:

    @staticmethod
    def get_moves(board, position, player):
        chess_type = board[position]

        for chess_piece in CHESS_PIECES:
            if chess_piece in chess_type.name.lower():
                break

        chess_move = getattr(ChessPiece, "get_" + chess_piece + "_moves")
        positions = chess_move(board, position, player)

        return Utils.get_rect_list(positions)

    @staticmethod
    def get_pawn_moves(board, position, player):
        return Pawn.get_moves(board, position, player)

    @staticmethod
    def get_rook_moves(board, position, player):
        return Rook.get_moves(board, position, player)

    @staticmethod
    def get_knight_moves(board, position, player):
        positions = []

        # Check upper direction
        y = position[1] - 2
        x = position[0] - 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        x = position[0] + 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        # Check lower direction
        y = position[1] + 2
        x = position[0] - 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        x = position[0] + 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        # Check left direction
        x = position[0] - 2
        y = position[1] - 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        y = position[1] + 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        # Check right direction
        x = position[0] + 2
        y = position[1] - 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        y = position[1] + 1
        p = (x, y)
        if ChessPiece.check_valid_position_knight(board, p, player):
            positions.append(p)

        return positions

    @staticmethod
    def get_bishop_moves(board, position, player):
        positions = []

        # Get left upper diagonal
        x, y = position[0] - 1, position[1] - 1
        while x >= 0 and y >= 0:
            p = (x, y)
            chess_piece = board[p]

            if chess_piece is not None:
                if player in chess_piece.name.lower():
                    break
                else:
                    positions.append(p)
                    break

            positions.append(p)

            x -= 1
            y -= 1

        # Get right upper diagonal
        x, y = position[0] + 1, position[1] - 1
        while x < BOARD_SIZE and y >= 0:
            p = (x, y)
            chess_piece = board[p]

            if chess_piece is not None:
                if player in chess_piece.name.lower():
                    break
                else:
                    positions.append(p)
                    break

            positions.append(p)

            x += 1
            y -= 1

        # Get left lower diagonal
        x, y = position[0] - 1, position[1] + 1
        while x >= 0 and y < BOARD_SIZE:
            p = (x, y)
            chess_piece = board[p]

            if chess_piece is not None:
                if player in chess_piece.name.lower():
                    break
                else:
                    positions.append(p)
                    break

            positions.append(p)

            x -= 1
            y += 1

        # Get right lower diagonal
        x, y = position[0] + 1, position[1] + 1
        while x < BOARD_SIZE and y < BOARD_SIZE:
            p = (x, y)
            chess_piece = board[p]

            if chess_piece is not None:
                if player in chess_piece.name.lower():
                    break
                else:
                    positions.append(p)
                    break

            positions.append(p)

            x += 1
            y += 1

        return positions

    @staticmethod
    def get_queen_moves(board, position, player):
        positions = []

        positions.extend(ChessPiece.get_rook_moves(board, position, player))
        positions.extend(ChessPiece.get_bishop_moves(board, position, player))

        return positions

    @staticmethod
    def get_king_moves(board, position):
        ...

    @staticmethod
    def check_valid_position_pawn(board, position, player):
        if position[0] in range(BOARD_SIZE) and position[1] in range(BOARD_SIZE):
            if board[position] is not None:
                if player not in board[position].name.lower():
                    return True

        return False

    @staticmethod
    def check_valid_position_knight(board, position, player):
        if position[0] in range(BOARD_SIZE) and position[1] in range(BOARD_SIZE):
            if board[position] is not None:
                if player not in board[position].name.lower():
                    return True
            else:
                return True

        return False
