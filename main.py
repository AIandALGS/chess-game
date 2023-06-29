import pygame

from manager.event_manager import EventManager
from src.chess_board.board import Board

def main(event_manager: EventManager, screen: pygame.Surface, clock: pygame.time.Clock):
    game_running = True

    while game_running:
        screen.fill(BLACK)

        game_running = event_manager.poll_events()

        board.draw_board(screen)

        pygame.display.update()
        clock.tick(FRAME_RATE)

if __name__ == "__main__":
    import os

    from src.constants import (
        WINDOW_DISPLAY_WIDTH,
        WINDOW_DISPLAY_HEIGHT,
        BLACK,
        FRAME_RATE
    )

    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT), 16)
    
    event_manager = EventManager()

    board = Board()

    main(event_manager, screen, pygame.time.Clock())

    pygame.quit()