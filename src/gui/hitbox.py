import pygame

from pygame import gfxdraw

from src.utilities.utils import Utils
from src.constants import SQUARE_SIZE, BLACK, GREEN_CIRCLE, CIRCLE_RADIUS


class Hitbox:
    texture = pygame.Surface(SQUARE_SIZE, pygame.SRCALPHA)

    @staticmethod
    def add_hitbox(screen, rect):
        pygame.draw.rect(Hitbox.texture, BLACK, Hitbox.texture.get_rect(), 4)
        screen.blit(Hitbox.texture, rect)

    @staticmethod
    def add_circle(screen, rect):
        offset_position = Utils.get_offset_position((rect.x, rect.y))
        gfxdraw.aacircle(screen, *offset_position, CIRCLE_RADIUS, GREEN_CIRCLE)
        gfxdraw.filled_circle(screen, *offset_position, CIRCLE_RADIUS, GREEN_CIRCLE)
