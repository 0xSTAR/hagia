import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import (
    key
)
from pygame.locals import *

sys.stdout = _stdout
del _stdout
del sys

from hagia.defs import HAGIA_CONTROLS

class InputSystem(object):
    def __init__(self):
        pass

    def init_input(self):
        self.kevs:list = []
        self.ks:list = [
            HAGIA_CONTROLS.BTN_0, # 0
            HAGIA_CONTROLS.BTN_1, # 1
            HAGIA_CONTROLS.BTN_2, # 2
            HAGIA_CONTROLS.BTN_3, # 3
            HAGIA_CONTROLS.BTN_4, # 4
            HAGIA_CONTROLS.BTN_5, # 5
            HAGIA_CONTROLS.RESET, # 6
            HAGIA_CONTROLS.PAUSE, # 7
            HAGIA_CONTROLS.EXIT   # 8
        ]

    def reg_kevs(self):
        self.kevs = key.get_pressed()

    def btn(self,x:int) -> bool:
        return self.kevs[self.ks[x]]
