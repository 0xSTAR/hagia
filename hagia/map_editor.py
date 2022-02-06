import sys
import os
import math
from dataclasses import dataclass
from typing import overload
import time

from tkinter import Tk
from tkinter.filedialog import askopenfile

from font import font
from atlas import atlas

_stdout = sys.stdout
sys.stdout = open(os.devnull,'w')

import pygame
import pygame.freetype
from pygame.locals import *

sys.stdout = _stdout
del(_stdout)

DEBUG:bool = False

@dataclass
class tile:
    spr_index:int = 0

#class _map:
#    def __init__(self):
#        self.tiles = [
#
#        ]

"""class atlas_panel(pygame.Surface):
    def __init__(
        self,
        w:int,
        h:int
    ) -> None:
        self.w = w
        #super(atlas_panel, self).__init__((w,h))
        self.panel = pygame.Surface((w,h))"""

class editor(object):
    def __init__(self):
        # 128 wide, 64 tall,
        # 128 columns, 64 rows
        self.tiles = [
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
            tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),tile(0),
        ]

        if DEBUG: print(f' number of tiles: {len(self.tiles)}')

        self.print_ver_info()

        self.initialize()

    def export(self):
        data = ''
        tiles = [tile.spr_index for tile in self.tiles]
        for index, tile in enumerate(tiles,start=0):
            if index % 128 == 0 and not index==0:
                data += '\n'
            data+='{},'.format(tile)

        with open('map.data','w') as data_file:
            data_file.write(data)

    def importer(self):
        if os.path.isfile('map.data'):

            with open('map.data','r') as map_data:
                data = map_data.read().replace('\n','').split(',')
                new_data = list(filter(None,data))
                
                for index,d in enumerate(new_data,start=0):
                    self.tiles[index].spr_index = int(d)

            



    def main(self):
        self._init()

        main_loop:bool = True
        while main_loop:
            self.pump()
            self.cls()
            self.reg_events()
            self.main_loop_checks()
            self._update()
            self._draw()
            self.clr_events()
            self.flip()
            self.clock.tick(self.framerate)

    def main_loop_checks(self):
        if 0x100 in self.events:
            self.shutdown()

    def _init(self):
        self.imported:bool = False
        self.exported:int = 0
        self.selected_sprite:int = 0
        self.failed_import:int = 0

        self.global_offset_x:int = 0
        self.global_offset_y:int = 0

        self.importer()

        #self.atlas_panel = atlas_panel(146*self.scale_factor,512*self.scale_factor)
    
    def _update(self):
        if not self.imported:
            # pressed import button
            if self.btn(0):
                Tk().withdraw()
                try:
                    atlas_file = askopenfile().name
                except AttributeError:
                    return
                try:
                    atlas0 = atlas(atlas_file) if atlas_file != None else None
                except:
                    self.failed_import = 60
                    return
                del(atlas_file)
                self.gfx = atlas0.load(self.scale_factor*2) if not atlas0 == None else []
                del(atlas0)
                self.imported = not self.imported
            return

        if self.btn(1) and self.exported <= 0:
            self.export()
            self.exported = 45

        fake_m_x, fake_m_y = pygame.mouse.get_pos()
        m_x, m_y = fake_m_x - self.global_offset_x, fake_m_y - self.global_offset_y

        cell_wh = 8 *self.scale_factor
        
        if (
            m_x+self.global_offset_x > (self.base_wh[0] - 200) * self.scale_factor
        ):
            #print('k')
            minfo = pygame.mouse.get_pos()
            mx, my = minfo[0],minfo[1]
            if (
                self.mse(0) and mx > (self.base_wh[0] - 180) * self.scale_factor
            ):    # selecting a sprite
                #print('even better')
                #print(f'{mx} {my}')
                x = math.ceil( (mx - ((self.base_wh[0] - 180) * self.scale_factor) ) / self.scale_factor / 2 / 8) - 1
                y = math.floor( (my - ((self.base_wh[1] - 50) * self.scale_factor) ) / self.scale_factor / 2 / 8) + 26
                tile_n = (y * 11) + x

                if (
                    x >= 0 and x < 11 and
                    y >= 0 and y < 12 and # y < 12 used to be y < 11
                    tile_n > 0 and tile_n < 128
                ):
                    
                    self.selected_sprite = tile_n
                #y = math.floor( (my + ((self.base_wh[1] - 50) * self.scale_factor)) ) / self.scale_factor / 2)
                #x = math.floor((mx - (self.base_wh[0] - 180) * self.scale_factor) / self.scale_factor / 2 / 11)# (column)
                #y = math.floor((my - (self.base_wh[1] - 50) * self.scale_factor) / self.scale_factor / 2 / 11) # (row)
                #print(f'x: {x} y: {y}')

        elif (
                m_x < self.base_wh[0]*self.scale_factor*2 and m_x > 0 and
                m_y > 0 and m_y < self.base_wh[1]*self.scale_factor*2
        ):
            if self.mse(0): # left click (set)
                row = math.floor(m_y / self.scale_factor / 2 / 8) # y
                column = math.floor(m_x / self.scale_factor / 2 / 8) # x

                tile_n = (row * 128) + column
                self.tiles[tile_n].spr_index = self.selected_sprite

                if DEBUG: 
                    print(f'left  || x: {m_x} y: {m_y}')
                    print(f'y: {row}')
                    print(f'x: {column}')

            elif self.mse(2): # right click (remove)
                
                row = math.floor(m_y / self.scale_factor / 2 / 8) # y
                column = math.floor(m_x / self.scale_factor / 2 / 8) # x

                tile_n = (row * 128) + column
                self.tiles[tile_n].spr_index = 0

                if DEBUG: 
                    print(f'right || x: {m_x} y: {m_y}')

        cell_wh = 8 * self.scale_factor

        if self.btn(2): # up
            self.global_offset_y += cell_wh * self.scale_factor
            #print(self.global_offset_y)
            self.sleep(0.06)
        elif self.btn(3): # down
            self.global_offset_y -= (8 * self.scale_factor) * self.scale_factor
            self.sleep(0.06)
        elif self.btn(4): # left
            self.global_offset_x += (8 * self.scale_factor) * self.scale_factor
            self.sleep(0.06)
        elif self.btn(5): # right
            self.global_offset_x -= (8 * self.scale_factor) * self.scale_factor
            self.sleep(0.06)

    def _draw(self):
        if not self.imported:
            if self.failed_import > 0:
                self.print(' INVALID FILE TYPE -=- MUST BE 8-BIT BMP ',105,245,7,8,size=25)
                self.failed_import-=1
                return
            self.print(' No sprite atlas currently loaded ',170,220,7,5,size=25)
            self.print(' Press \'I\' to load an atlas ',225,256,7,5,size=25)
            return

        cell_wh = 8*self.scale_factor

        for row in range(64):
            # row means y-axis
            # draw row
            if DEBUG:print(f'row: {row}')
            self.line(
                0,
                row*cell_wh,
                128*cell_wh,
                row*cell_wh,
                7
            )

        for column in range(128):
            # column means x
            # draw column
            if DEBUG:print(f'column: {row}')

            _column = column*cell_wh
            self.line(
                _column,
                0,
                _column,
                64*cell_wh,
                7
            )

        # draw tiles . . .

        start_x = 0 - self.global_offset_x
        start_y = 0 - self.global_offset_y

        #on_screen = ((start_x + (self.base_wh[0])) / cell_wh) * ((start_y + (self.base_wh[1])) / cell_wh)
        on_scr_x = (start_x + self.base_wh[0]) / cell_wh  + 4
        on_scr_y = (start_y + self.base_wh[1]) / cell_wh  + 4

        for index, tile in enumerate(self.tiles,start=0):
            x = index % 128
            y = math.floor(index / 128)

            #create_x = x * self.scale_factor * cell_wh
            #create_y = y * self.scale_factor * cell_wh
            #if create_x < on_scr_x and create_y < on_scr_y:
            #    self.screen.blit(self.gfx[tile.spr_index],(x,y))
            if x < on_scr_x and y < on_scr_y:
                self.screen.blit(
                    self.gfx[tile.spr_index],
                    (
                        (x*self.scale_factor*cell_wh) - start_x,
                        (y*self.scale_factor*cell_wh) - start_y
                    )
                    #(0,0,cell_wh*self.scale_factor,cell_wh*self.scale_factor)
                )
            #print(f'x: {x} y: {y}')
            #self.screen.blit(self.gfx[tile.spr_index].convert(),(x,y))

        # draw atlas panel
        x0 = self.base_wh[0] - 180
        x1 = self.base_wh[0]
        y0 = 0
        y1 = self.base_wh[1]
        self.rectfill(x0-20,y0,x1,y1,1)
        #self.rectfill(True,x0,y0,x1,y1)#,5)
        rect = pygame.Rect(
                x0*self.scale_factor,
                y0*self.scale_factor,
                (x1 - x0) * self.scale_factor,
                (y1 - y0) * self.scale_factor
            )
        pygame.draw.rect(
            self.screen,
            pygame.Color(20,20,20,a=255),
            rect,
            width=0
        )

        selected_len = len(str(self.selected_sprite))
        prefix = ''
        for i in range(3-selected_len):
            prefix+='0'
        
        x = self.base_wh[0] - 170
        y = 5
        self.print('selected: {}'.format(prefix+str(self.selected_sprite)),x,y,7,0,size=15)

        sx = self.base_wh[0] - 180
        sy = 0 + 50

        sprite_wh = 8 * self.scale_factor

        # 11 per row ** correction: 12
        for row in range(16):
            for sprite in range(11):
                gfx_index = (row * 11) + sprite
                try:
                    self.screen.blit(
                        self.gfx[gfx_index],
                        (
                            ((sx * self.scale_factor) + (sprite * self.scale_factor * sprite_wh)),
                            ( (sy * self.scale_factor) + (row * self.scale_factor * sprite_wh) )
                        )
                    )
                except IndexError:
                    pass

                if gfx_index == self.selected_sprite:
                    rect = pygame.Rect(
                        ((sx * self.scale_factor) + (sprite * self.scale_factor * sprite_wh)),
                        ( (sy * self.scale_factor) + (row * self.scale_factor * sprite_wh) ),
                        8*self.scale_factor * 2,
                        8*self.scale_factor * 2
                    )

                    pygame.draw.rect(
                        self.screen,
                        self.colours[7],
                        rect,
                        width=2*self.scale_factor,
                        border_radius=3*self.scale_factor

                    )


        if self.exported > 0:
            self.print(' exported ',350,420,7,8,size=35)
            self.exported -= 1

    def initialize(self) -> None:
        try:
            pygame.init()
            pygame.display.init()
            pygame.freetype.init()
        except RuntimeError:
            self.shutdown('ERROR: pygame failed to initialize')

        self.init_display()
        self.init_colour()
        self.init_font()
        self.init_mouse()
        self.init_time()
        self.configure()
        
    def init_display(self) -> None:
        base_wh:tuple[int,int] = (1024,512)
        self.base_wh = base_wh

        display_inf = pygame.display.Info()
        c_w = display_inf.current_w
        c_h = display_inf.current_h

        self.scale_factor = math.ceil(c_h / base_wh[1]) - 1
        dimens = (base_wh[0] * self.scale_factor,base_wh[1] * self.scale_factor)

        pygame.display.set_caption('Map Editor 6243 ZX')
        try:
            icon = pygame.image.load('pyco8.png')
        except FileNotFoundError:
            icon = None
        pygame.display.set_icon(icon) if icon != None else None
        self.screen = pygame.display.set_mode(dimens,depth=8)

        del(base_wh)
        del(display_inf)
        del(c_w)
        del(c_h)
        del(dimens)
        del(icon)

    def init_colour(self) -> None:
        self.colours = [
            pygame.Color(0,0,0,a=255), # black / 0
            pygame.Color(29,43,83,a=255), # dark blue / 1
            pygame.Color(126,37,83,a=255), # dark purple / 2
            pygame.Color(0,135,81,a=255), # dark green / 3
            pygame.Color(171,82,54,a=255), # brown / 4
            pygame.Color(95,87,79,a=255), # dark-grey / 5
            pygame.Color(194,195,199,a=255), # light-grey / 6
            pygame.Color(255,241,232,a=255), # white / 7
            pygame.Color(255,0,77,a=255), # red / 8
            pygame.Color(255,163,0,a=255), # orange / 9
            pygame.Color(255,236,39,a=255), # yellow / 10
            pygame.Color(0,228,54,a=255), # green / 11
            pygame.Color(41,173,255,a=255), # blue / 12
            pygame.Color(131,118,156,a=255), # lavender / 13
            pygame.Color(255,119,168,a=255), # pink / 14
            pygame.Color(255,204,170,a=255) # light-peach / 15
        ]

    def init_font(self) -> None:
        self.font = font().load()

    def init_mouse(self) -> None:
        pygame.mouse.set_visible(True)

    def init_time(self) -> None:
        self.clock = pygame.time.Clock()
        self.framerate:int = 15

    def configure(self) -> None:
        """
        I - for importing a sprite atlas
        E - exporting map data
        LEFT_MOUSE_BUTTON - setting sprite on map
        RIGHT_MOUSE_BUTTON - deleting sprite (setting to sprite 0)
        """
        self.keys = [
            105, # i
            101, # e
            1073741906, # up arrow
            1073741905, # down arrow
            1073741904, # left arrow
            1073741903 # right arrow
        ]

    def shutdown(self,error_msg='Exited successfully.'):
        pygame.quit()
        sys.exit(error_msg)

    def print_ver_info(self) -> None:
        print('\nMap Editor 6243 ZX 0.1.0-alpha')
        SDL_ver = pygame.get_sdl_version()
        print(f'SDL {SDL_ver[0]}.{SDL_ver[1]}.{SDL_ver[2]}')
        py_impl:str = str(sys.implementation.name)
        py_cachetag:str = str(sys.implementation.cache_tag)
        py_ver_inf = sys.version_info
        print(py_impl+' '+str(py_ver_inf[0])+'.'+str(py_ver_inf[1])+'.'+str(py_ver_inf[2])+'-'+str(py_ver_inf[3])+' / '+py_cachetag+'\n')
        del(py_impl)
        del(py_cachetag)
        del(py_ver_inf)
        del(SDL_ver)

    def flip(self) -> None:
        pygame.display.flip()

    def pump(self) -> None:
        pygame.event.pump()

    def reg_events(self) -> None:
        self.events = [ev.type for ev in pygame.event.get()]
        self.mouse_events = pygame.mouse.get_pressed(num_buttons=3)
        self.key_events = pygame.key.get_pressed()

    def clr_events(self) -> None:
        pygame.event.clear()
        del(self.events)
        del(self.mouse_events)
        del(self.key_events)

    def cls(self,x:int=0) -> None:
        self.screen.fill(self.colours[x])

    def sleep(self,x) -> None:
        time.sleep(x)

    def btn(self,x) -> bool:
        return self.key_events[self.keys[x]]

    def mse(self,x) -> bool:
        return self.mouse_events[x]

    def print(
        self,
        text:str,
        x:int,
        y:int,
        fgcolor:int=0,
        bgcolor:int=0,
        #style=pygame.STYLE_DEFAULT,
        #rotation=0,
        size=4
    ):
        # make sure to remove global offset from print for this
        self.font.render_to(self.screen,((x*self.scale_factor)+0,(y*self.scale_factor)+0),text,fgcolor=self.colours[fgcolor],bgcolor=self.colours[bgcolor],
            #style=style,
            #rotation=rotation,
            size=size*self.scale_factor
        )

    def line(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0,
        width:int=1
    ) -> None:
        pygame.draw.line(
            self.screen,
            self.colours[col],
            ((x0*self.scale_factor)+self.global_offset_x,(y0*self.scale_factor)+self.global_offset_y),
            ((x1*self.scale_factor)+self.global_offset_x,(y1*self.scale_factor)+self.global_offset_y),
            width=width*self.scale_factor
        )

    def rect(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0,
        width:int=1
    ) -> None:
        rect = pygame.Rect(
            x0*self.scale_factor,
            y0*self.scale_factor,
            (x1 - x0) * self.scale_factor,
            (y1 - y0) * self.scale_factor
        )
        pygame.draw.rect(
            self.screen,
            self.colours[col],
            rect,
            width=width*self.scale_factor
        )

    """@overload
    def rectfill(
        self,
        nice:bool,
        x0,
        y0,
        x1,
        y1,
        col=pygame.Color(20,20,20,a=255)
    ) -> None:
        if type(nice) == bool:
            
            rect = pygame.Rect(
                x0*self.scale_factor,
                y0*self.scale_factor,
                (x1 - x0) * self.scale_factor,
                (y1 - y0) * self.scale_factor
            )
            pygame.draw.rect(
                self.screen,
                col,
                rect,
                width=0
            )"""

    def rectfill(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ) -> None:
        rect = pygame.Rect(
            x0*self.scale_factor,
            y0*self.scale_factor,
            (x1 - x0) * self.scale_factor,
            (y1 - y0) * self.scale_factor
        )
        pygame.draw.rect(
            self.screen,
            self.colours[col],
            rect,
            width=0
        )

def main():
    e = editor()
    e.main()

if __name__ == '__main__':
    main()


