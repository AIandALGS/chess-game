from pygame import mixer

from src.utilities.utils import Utils


class EffectsManager:
    def __init__(self) -> None:
        self.__sound_path = "sound_fx/effects/"

    def play_sound(self, board, position):
        if Utils.is_empty_square(board, position):
            mixer.Channel(0).play(mixer.Sound(self.__sound_path + "move.wav"))
        else:
            mixer.Channel(1).play(mixer.Sound(
                self.__sound_path + "capture.wav"))

        # If it is en passant play capture
