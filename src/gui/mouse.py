import pygame

from src.gui.hitbox import Hitbox
from src.utilities.utils import Utils
from src.utilities.matrix import Matrix
from src.chess_pieces.chess_piece_switch import ChessPieceSwitch
from src.constants import BOARD_SIZE, BOARD_FLIPS


class Mouse:
    def __init__(self):
        self.__moves = []
        self.__selected = False
        self.__current_position = None

    @staticmethod
    def get_position():
        return pygame.mouse.get_pos()

    @staticmethod
    def get_local_mouse_position():
        return Utils.get_local_position(Mouse.get_position())

    @staticmethod
    def get_mouse_click(events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

        return False

    def check_collision_and_clicked(self, mouse_clicked, rect):
        return mouse_clicked and rect.collidepoint(Mouse.get_position())

    def clear_moveset(self):
        self.__moves.clear()
        self.__selected = False
        self.__current_position = None

    def update_moves(self, board, mouse_clicked, position):
        for move in self.__moves:
            if self.check_collision_and_clicked(mouse_clicked, move):
                board[position] = board[self.__current_position]
                board[self.__current_position] = None
                self.clear_moveset()
                board = Matrix.rotate_board(board)

    def update(self, board, events):
        mouse_clicked = Mouse.get_mouse_click(events)
        position = Mouse.get_local_mouse_position()

        if mouse_clicked:
            if not self.__selected or self.__current_position != position:
                if board[position] is not None:
                    self.__moves = ChessPieceSwitch.get_moves(board, position)
                    self.__selected = True
                    self.__current_position = position
            else:
                self.clear_moveset()

        self.update_moves(board, mouse_clicked, position)

    def render(self, screen, rects):
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()):
                Hitbox.add_hitbox(screen, rect)

        for move in self.__moves:
            Hitbox.add_circle(screen, move)
