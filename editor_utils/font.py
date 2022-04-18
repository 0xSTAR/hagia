import sys
import os

_stdout = sys.stdout
sys.stdout = open(os.devnull,'w')

import pygame.freetype

sys.stdout = _stdout
del(_stdout)
del(sys)
del(os)

from editor_utils.local_vars import (
    default_font
)

class font(object):
    def __init__(self,font:str=None) -> None:
        self.font = font if not font==None else default_font

    def load(self):# returns a font
        return pygame.freetype.Font(self.font)
