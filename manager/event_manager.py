import pygame


class EventManager:
    """
    The event manager class keeps tracks of all pygame events.
    """

    def poll_events(self) -> bool:
        """
        Poll game events, i.e. check if the game is still running.

        Return a Boolean value based on whether the game is running or
        not.
        """

        game_running = True

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                game_running = False

        return game_running, events
