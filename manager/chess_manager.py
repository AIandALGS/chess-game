import pygame

from src.chess_pieces.chess_type import ChessType
from src.utilities.utils import Utils

from src.constants import (
    CHESS_PIECE_SIZE
)

class ChessManager:

    @staticmethod
    def get_chess_txtr(chess_type):
        chess_path = chess_type.value
        chess_imge = pygame.image.load(chess_path).convert_alpha()
        chess_txtr = pygame.transform.scale(chess_imge, CHESS_PIECE_SIZE)

        return chess_txtr

    @staticmethod
    def get_chess_piece(board, position):
        chess_txtr = ChessManager.get_chess_txtr(board[position])
        global_position = Utils.get_global_position(position)
        chess_rect = pygame.Rect(*global_position, *CHESS_PIECE_SIZE)

        return chess_txtr, chess_rect

