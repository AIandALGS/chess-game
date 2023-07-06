from pygame import mixer


class EffectsManager:
    def __init__(self) -> None:
        self.__sound_path = "sound_fx/effects/"

    def play_sound(self, sound_effect):
        mixer.Channel(0).play(mixer.Sound(self.__sound_path + sound_effect + ".wav"))
