import pygame

from manager.sound_manager import MusicManager


class EventManager:
    """
    The event manager class keeps tracks of all pygame events.
    """

    def __init__(self) -> None:
        self.__click = False
        self.__music_manager = MusicManager()

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

        # Comment this line out if you do not want music :(
        if not pygame.mixer.music.get_busy():
            self.__music_manager.play_music()

        return game_running, events

    def poll_click_events(self):
        return self.__click
