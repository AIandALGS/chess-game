import pygame

from manager.chess_manager import ChessManager
from manager.sound_manager import EffectsManager

from src.chess_pieces.chess_piece_factory import ChessPieceFactory
from src.utilities.matrix import Matrix
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
        self.__current_player = "white"
        self.__board = self.initialize_board()
        self.__rects = self.initialize_rects()
        self.__effects_manager = EffectsManager()
        self.__mouse = Mouse()
        self.__moves = []
        self.__selected = False
        self.__current_position = None

    @staticmethod
    def get_empty_square(board, position):
        return board[position] is None

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

    def check_collision_and_clicked(self, mouse_clicked, rect):
        return mouse_clicked and rect.collidepoint(Mouse.get_position())

    def clear_moveset(self):
        self.__moves.clear()
        self.__selected = False
        self.__current_position = None

    def end_turn(self, position, chess_type):
        if chess_type is not None:
            if self.__current_player in chess_type.name.lower():
                self.__moves = ChessPieceFactory.get_moves(
                    self.__board, position, self.__current_player
                )
                self.__selected = True
                self.__current_position = position

    def change_player(self):
        if self.__current_player == "white":
            self.__current_player = "black"
        else:
            self.__current_player = "white"

        # play sound
        self.__effects_manager.play_sound("move")

    def update_moves(self, mouse_clicked, position):
        for move in self.__moves:
            if self.check_collision_and_clicked(mouse_clicked, move):
                self.__board[position] = self.__board[self.__current_position]
                self.__board[self.__current_position] = None
                self.__board = Matrix.rotate_board(self.__board)

                self.clear_moveset()
                self.change_player()

    def update(self, events):
        mouse_clicked = Mouse.get_mouse_click(events)
        position = Mouse.get_local_mouse_position()

        if mouse_clicked:
            if not self.__selected or self.__current_position != position:
                chess_type = self.__board[position]
                self.end_turn(position, chess_type)
            else:
                self.clear_moveset()

        self.update_moves(mouse_clicked, position)

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

        self.__mouse.render(screen, self.get_list_of_rects(), self.__moves)
