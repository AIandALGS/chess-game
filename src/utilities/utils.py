import pygame

from src.constants import BOARD_SIZE, SQUARE_WIDTH, SQUARE_HEIGHT, SQUARE_SIZE


class Utils:
    @staticmethod
    def get_global_position(position):
        global_x = position[0] * SQUARE_WIDTH
        global_y = position[1] * SQUARE_HEIGHT

        return (global_x, global_y)

    @staticmethod
    def get_local_position(position):
        local_x = position[0] // SQUARE_WIDTH
        local_y = position[1] // SQUARE_HEIGHT

        return (local_x, local_y)

    @staticmethod
    def get_offset_position(position):
        offset_x = position[0] + (SQUARE_WIDTH // 2)
        offset_y = position[1] + (SQUARE_HEIGHT // 2)

        return (offset_x, offset_y)

    @staticmethod
    def get_global_positions(positions):
        global_positions = []

        for position in positions:
            global_position = Utils.get_global_position(position)
            global_positions.append(global_position)

        return global_positions

    @staticmethod
    def get_rect_list(positions):
        rects = []

        for position in positions:
            global_position = Utils.get_global_position(position)
            rect = pygame.Rect(*global_position, *SQUARE_SIZE)
            rects.append(rect)

        return rects

    @staticmethod
    def is_empty_square(board, position):
        return board[position] is None

    @staticmethod
    def is_position_in_range(position):
        return position[0] in range(BOARD_SIZE) and position[1] in range(BOARD_SIZE)

    @staticmethod
    def is_opponent_position(board, position, player):
        return player not in board[position].name.lower()
