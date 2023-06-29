import pygame

from src.utilities.utils import Utils

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

    def initialize_board(self):
        board = dict()

        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                position = (x, y)
                board[position] = None

        return board
    
    def initialize_rects(self):
        rects = dict()

        for position in self.__board:
            global_position = Utils.get_global_position(position)
            rect = pygame.Rect(*global_position, *SQUARE_SIZE)
            rects[position] = rect

        return rects
            

    def draw_board(self, screen):
        for position in self.__board:
            x = position[0]
            y = position[1]

            if (not(x % 2) and not(y % 2)) or (x % 2 and y % 2):
                pygame.draw.rect(screen, LIGHT_SQUARE, self.__rects[position])
            else:
                pygame.draw.rect(screen, DARK_SQUARE, self.__rects[position])





    