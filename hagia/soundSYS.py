import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import (
    mixer
)
from pygame.locals import *

sys.stdout = _stdout
del _stdout
del sys

from .errata import (
    BASE_HAGIA_ERROR,
    HAGIA_ASSERT
)

from os import path
from .utils import Thread
from .defs import HAGIA_SPECS

class SoundSystem(object):
    def __init__(self):
        pass

    def init_sound(self):
        try:
            mixer.pre_init(
                frequency=44100,
                size=-16,
                channels=2,
                buffer=512,
                devicename=None,
                allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE
            )
            mixer.init()
        except:
            raise BASE_HAGIA_ERROR("hagia.sound.SoundSystem failed to initialize")

        self.snd:list = []
        self.mus:list = []
        self.channels:list = []

        for chnl in range(HAGIA_SPECS.SOUND_CHANNELS):
            self.channels.append(
                mixer.Channel(chnl)
            )
            #self.channels[chnl].__currently_playing = -1

    async def load_sound_data(self):
        self.snd:list = []
        self.mus:list = []

        def ok_list_of_strs(_dataset:list) -> bool:
            for sndx in _dataset:
                print(_dataset)
                if not sndx is str:
                    return False
            return True

        def check_list_snd_mus(_attr:str,*args):
            if (
                getattr(self.cart,_attr) is list and
                len(getattr(self.cart,_attr)) > 0
            ):
                HAGIA_ASSERT(
                    ok_list_of_strs(getattr(self.cart,_attr)),
                    "Error: Must be a list of strings for SFX and MUSIC."
                )

        sfx_check = Thread(
            target=check_list_snd_mus,
            args=("sfx",)
        )
        mus_check = Thread(
            target=check_list_snd_mus,
            args=("music",) # comma otherwise breaks and
                            # pretends the string is a list
                            # :)
        )
        sfx_check.start()
        mus_check.start()

        #for sndx,musx in zip(self.cart.sfx,self.cart.music):
        #    self.snd.append(
        #        mixer.Sound(path.join(self.cart.c_data_directory,sndx))
        #    )
        #    self.mus.append(
        #        path.join(self.cart.c_data_directory,musx)
        #    )
        for sndx in self.cart.sfx:
            self.snd.append(
                mixer.Sound(path.join(self.cart.c_data_directory,sndx))
            )
        for musx in self.cart.music:
            self.mus.append(
                path.join(self.cart.c_data_directory,musx)
            )

        sfx_check.join()
        mus_check.join()
        del sfx_check
        del mus_check

    def sfx(
        self,
        n:int,
        channel:int=-1,
        fade_len:int=0
    ) -> None:
        # default) to automatically choose a channel that is not being used
        if channel < 0:
            for c in self.channels:
                if n==-1:c.stop();continue
                elif n==-2:c.fadeout(fade_len);continue
                if channel==-1 and not c.get_busy():
                    c.play(self.snd[n],fade_ms=fade_len)
                    return
                elif channel==-2 and c.get_sound() == self.snd[n]:
                    c.stop()
                    return
            return

        if n == -1:
            self.channels[channel].stop()
            return
        elif n==-2:
            self.channels[channel].fadeout(fade_len)
            return

        # normal
        self.channels[channel].play(self.snd[n],fade_ms=fade_len)

    def music(
        self,
        n:int,
        fade_len:int=0,
        #channel_mask:int=-1,
        loop:int=-1,
        offset:float=0.0
    ) -> None:
        if n==-1:
            mixer.music.stop()
            mixer.music.unload()
            return
        if not mixer.music.get_busy():
            mixer.music.stop()
            mixer.music.unload()
        mixer.music.load(self.mus[n])
        mixer.music.play(loops=loop,start=offset,fade_ms=fade_len)
