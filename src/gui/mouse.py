import pygame

from src.gui.hitbox import Hitbox
from src.utilities.utils import Utils
from src.utilities.matrix import Matrix
from src.chess_pieces.chess_piece_switch import ChessPiece


class Mouse:
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

    def render(self, screen, rects, moves):
        for rect in rects:
            if rect.collidepoint(pygame.mouse.get_pos()):
                Hitbox.add_hitbox(screen, rect)

        for move in moves:
            Hitbox.add_circle(screen, move)
