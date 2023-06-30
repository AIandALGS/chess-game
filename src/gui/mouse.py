import pygame

from src.gui.hitbox import Hitbox
from src.utilities.utils import Utils
from src.chess_pieces.chess_piece_switch import ChessPieceSwitch


class Mouse:
    def __init__(self):
        self.__selected = False
        self.__moves = []
        self.__current_position = None

    def check_click_event(self, board, rect, position):
        return (
            rect.collidepoint(pygame.mouse.get_pos())
            and pygame.mouse.get_pressed()[0]
            and board[position] is not None
        )

    def update(self, board, rects):
        for rect in rects:
            position = Utils.get_local_position((rect.x, rect.y))

            if self.check_click_event(board, rect, position):
                self.__moves = ChessPieceSwitch.get_moves(
                    board, position, board[position]
                )

                self.__current_position = position

        for move in self.__moves:
            if (
                move.collidepoint(pygame.mouse.get_pos())
                and pygame.mouse.get_pressed()[0]
            ):
                new_position = Utils.get_local_position((move.x, move.y))
                board[new_position] = board[self.__current_position]
                board[self.__current_position] = None

    def render(self, screen, rects):
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()):
                Hitbox.add_hitbox(screen, rect)

        for move in self.__moves:
            Hitbox.add_circle(screen, move)
