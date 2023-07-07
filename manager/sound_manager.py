from pygame import mixer

from src.utilities.utils import Utils


class EffectsManager:
    def __init__(self) -> None:
        self.__sound_path = "sound_fx/effects/"

    def play_sound(self, board, position):
        if Utils.is_empty_square(board, position):
            self.play_move_sound()
        else:
            self.play_capture_sound()

    def play_move_sound(self):
        mixer.Channel(0).play(mixer.Sound(self.__sound_path + "move.wav"))

    def play_capture_sound(self):
        mixer.Channel(1).play(mixer.Sound(self.__sound_path + "capture.wav"))

    def play_check_sound(self):
        mixer.Channel(2).play(mixer.Sound(self.__sound_path + "check.wav"))

    def play_checkmate_sound(self):
        mixer.Channel(3).play(mixer.Sound(self.__sound_path + "checkmate.wav"))
