import pygame

from manager.chess_manager import ChessManager

from src.utilities.utils import Utils
from src.gui.mouse import Mouse


from src.chess_pieces.chess_position_constants import (
    WHITE_INITIAL_POSITIONS,
    BLACK_INITIAL_POSITIONS,
)

from src.constants import (
    BOARD_SIZE,
    SQUARE_SIZE,
    LIGHT_SQUARE,
    DARK_SQUARE,
)


class Board:
    def __init__(self):
        self.__board = self.initialize_board()
        self.__rects = self.initialize_rects()
        self.__mouse = Mouse()

    def initialize_board(self):
        board = dict()

        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                position = (x, y)
                board[position] = None

        for white_position, white_type in WHITE_INITIAL_POSITIONS.items():
            board[white_position] = white_type

        for black_position, black_type in BLACK_INITIAL_POSITIONS.items():
            board[black_position] = black_type

        return board

    def initialize_rects(self):
        rects = dict()

        for position in self.__board:
            global_position = Utils.get_global_position(position)
            rect = pygame.Rect(*global_position, *SQUARE_SIZE)
            rects[position] = rect

        return rects

    def get_list_of_rects(self):
        return self.__rects.values()

    def update(self):
        self.__mouse.update(self.__board, self.get_list_of_rects())

    def draw_board(self, screen):
        for position in self.__board:
            x = position[0]
            y = position[1]

            if (not (x % 2) and not (y % 2)) or (x % 2 and y % 2):
                pygame.draw.rect(screen, LIGHT_SQUARE, self.__rects[position])
            else:
                pygame.draw.rect(screen, DARK_SQUARE, self.__rects[position])

    def render(self, screen):
        for position in self.__board:
            if self.__board[position] is not None:
                chess_txtr, chess_rect = ChessManager.get_chess_piece(
                    self.__board, position
                )
                screen.blit(chess_txtr, chess_rect)

        self.__mouse.render(screen, self.get_list_of_rects())
