import sys
import os
import configparser
import operator
from dataclasses import dataclass
from functools import singledispatch
from typing import overload, Type
import math
import random
import time

from hagia.cart import cart
from hagia.log import log
from hagia.atlas import atlas
from hagia.font import font
from hagia.error import hagia_init_error
from hagia.local_vars import (
    debug,
    version,
    default_font
)

import numpy

# shutting up pygame on import
_stdout = sys.stdout
sys.stdout = open(os.devnull,'w')

import pygame
import pygame.freetype
from pygame.locals import *

# allowing stdout to breath again
sys.stdout = _stdout
del(_stdout)

class hagia(object):
    def __init__(self):
        pass
    def cartridge(self,cart):
        #self.initialize()
        self.load_cart(cart)
        #self.boot()
        self.main()

    def load_cart(self,cart):
        self.original_cart_state = cart
        self.cart = cart

        self.initialize()

        try:
            self.load_gfx(self.cart.gfx)
        except AttributeError:
            pass

        try:
            self.load_sfx(self.cart.sfx)
        except AttributeError:pass

        try:
            self.load_music(self.cart.music)
        except AttributeError:
            pass

        try:self.load_font(self.cart.font)
        except AttributeError:
            self.load_font() # use default font then

        try:self.load_flags(self.cart.flags)
        except AttributeError:
            self.load_flags()

        try:self.load_map(self.cart.map)
        except AttributeError:
            self.load_map()

        #print(str(self.map_data))

        #self.parse_config()

    def load_gfx(self,atlas_data:str):
        atlas2 = atlas(atlas_data)#(getattr(self.cart,"gfx"))
        self.gfx_data = atlas2.load(self.multiplier)
        del(atlas2)

    def load_sfx(self,sfx:list):
        self.sfx_data = []
        if type(sfx[0])==bytes:
            for snd in sfx:
                self.sfx_data.append(pygame.mixer.Sound(buffer=snd))
        else:
            try:
                bytes.fromhex(sfx[0])
                for snd in sfx:
                    self.sfx_data.append(pygame.mixer.Sound(buffer=bytes.fromhex()))
            except ValueError:
                for snd in sfx:
                    self.sfx_data.append(pygame.mixer.Sound(buffer=open(snd,'rb').read()))

    def load_music(self,music:list):
        self.music_data = []
        for mus in music:
            assert not type(music[0])==bytes,sys.exit('Music cannot be bytes, must be file')
            self.music_data.append(mus)

    def load_font(self,font_file=None):
        if font == None:
            self.font = font().load()
            return
        else:
            self.font = font(font_file).load()

    @overload
    def load_flags(self):
        self.flags = [
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
            [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
        ]

    def load_flags(self,flag_data: Type[list]) -> None:
        self.flags = flag_data

    #@overload
    def load_flags(self,data_file: Type[str]) -> None:
        def check_flag(x) -> bool:
            return int(x)==True
        self.flags = []
        with open(data_file,'r') as flag_data_file:
            parsed = flag_data_file.read().split('\n')
            parsed2 = list(filter(None,parsed))
            del(parsed)
            for flag_group in parsed2:
                flags = []
                for i in range(8):
                    flags.append(check_flag(flag_group[i]))
                self.flags.append(flags)

    #@overload
    def load_map(self,data_file: Type[str]) -> None:
        map_data_path:str = data_file
        with open(map_data_path,'r') as map_data_file:
            raw_data = map_data_file.read().replace('\n','').split(',')
            filtered_data = list(filter(None,raw_data))

            self.map_data = [int(data) for data in filtered_data]

    #@overload
    #def load_map(self,data_list: list) -> None:
    #    self.map_data = data_list

    """@overload
    def load_map(self):
        self.map_data = [
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,

        ]"""

    def main(self):
        # if game has an _INIT function, call it first before the main loop
        self.cart._init()

        # if reset option, it will stop the main loop
        self.main_loop = True
        while self.main_loop:
            self.cls(0)
            self.pump()
            self.register_events()
            self.main_loop_checks()
            self.cart._update()
            self.cart._draw()
            #self.p8_print('Hello World',50,50,fgcolor=self.colours[7],size=50)
            self.clear_events()
            self.flip()
            self.game_clock.tick(self.framerate)

    def main_loop_checks(self):
        if debug:print('unpaused')
        for event in self.events:
            if event == pygame.QUIT:
                self.shutdown()

        if self.key_events[self.keys[6]]:
            self.pause()
            return

    def pause(self):
        self.rpal()
        paused:bool = True

        self.clear_events()

        # needs to sleep and blacken screen
        # or else instantly unpauses itself
        self.cls(0)

        # initial drawing - text
        self.print('continue',34,54,7,0,5)
        self.print('reset cart',34,63,7,0,5)
        self.print('exit',34,72,7,0,5)

        # initial drawing - box
        self.rect(24,48,128-28,128-48,7)

        self.flip()
        self.sleep(0.2)

        pygame.mixer.music.pause()
        pygame.mixer.pause()

        paused_clock = pygame.time.Clock()

        pointer:int = 0
        while paused:
            if debug:print('paused')
            self.cls(0)
            self.pump()
            self.register_events()

            for event in self.events:
                # 0x100 is the hex value of pygame.QUIT,
                # which is also the int value 256
                if event == 0x100:
                    self.shutdown()


            if self.key_events[self.keys[6]]: # esc
                paused = False
                if debug:print('unpausing')
            if self.key_events[self.keys[5]]: # button_1 (x)
                # for now it will unpause the game, but when menu depth is added .. .
                # it will instead decrease the menu depth
                # and there will be a check afterwards and if the menu depth is 0
                # then it will unpause / resume the game
                paused = False

            if self.key_events[self.keys[0]]: #up >> effects pointer
                pointer -= 1 if not pointer==0 else 0
            if self.key_events[self.keys[1]]: # down >> effects pointer
                pointer += 1 if not pointer==2 else 0

            if debug: print(pointer)

            if self.key_events[self.keys[4]]:
                if pointer==0: # resume
                    paused = False
                if pointer==1: # reset cart
                    self.reset()
                if pointer==2: # exit
                    self.shutdown()

            # draw menu

            # x start is 34 for options items
            # size is . . .
            # 9 in between each y value

            # text
            self.print('continue',34,54,7,0)
            self.print('reset cart',34,63,7,0)
            self.print('exit',34,72,7,0)

            # box
            self.rect(24,48,128-28,128-48,7)

            # pointer
            values = [
                (34-5,54),
                (34-5,63),
                (34-5,72)
            ]
            if pointer==0:
                self.polygon(values[0][0],values[0][1],7,[(0,0),(8,4),(0,8)])
            elif pointer==1:
                self.polygon(values[1][0],values[1][1],7,[(0,0),(8,4),(0,8)])
            elif pointer==2:
                self.polygon(values[2][0],values[2][1],7,[(0,0),(8,4),(0,8)])


            self.clear_events()
            self.flip()
            paused_clock.tick(self.framerate)

            # the events just register too fast
            self.sleep(0.08)
            pass

        del(paused)
        del(paused_clock)
        del(pointer)

        self.sleep(0.5)

        pygame.mixer.music.unpause()
        pygame.mixer.unpause()

        self.cls(0)
        self.pump()
        self.register_events()

    # reset cart to be exact **
    def reset(self):
        # reset screen
        self.cls(0)
        self.pump()
        self.flip()
        self.register_events()
        self.clear_events()

        # reset cart
        self.cart = self.original_cart_state

        # reloading assets
        try:
            self.load_gfx(self.cart.gfx)
        except AttributeError:
            pass

        try:
            self.load_sfx(self.cart.sfx)
        except AttributeError:pass

        try:
            self.load_music(self.cart.music)
        except AttributeError:
            pass

        try:self.load_font(self.cart.font)
        except AttributeError:
            self.load_font() # use default font then

        try:self.load_flags(self.cart.flags)
        except AttributeError:
            self.load_flags()

        try:self.load_map(self.cart.map)
        except AttributeError:
            self.load_map()

        self.init_colour()
        self.parse_config()
        self.init_camera()
        self.init_time()

        pygame.mixer.music.stop()
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()

        pygame.mixer.stop()

        # back to main loop which redoes the init and
        # begins the loop
        self.main()


    def get_ver_tuple(self) -> tuple:
        return version

    def get_ver(self) -> str:
        return (
            '{}.{}.{}'.format(version[0],version[1],version[2])
        )

    def print_info(self) -> None:
        sys.stdout.write('\nHagia Engine {}\nSDL {}\n{}\n'.format(
                self.get_ver(),
                str(pygame.get_sdl_version()[0])+'.'+str(pygame.get_sdl_version()[1])+'.'+str(+pygame.get_sdl_version()[2]),
                str(sys.implementation.name)+' '+str(sys.version_info[0])+'.'+str(sys.version_info[1])+'.'+str(sys.version_info[2])+'-'+str(sys.version_info[3])+' / '+str(sys.implementation.cache_tag),

            )
        )

    def initialize(self):
        self.print_info()
        self.init_log()

        try:
            pygame.init()
            pygame.mixer.init()
            pygame.display.init()
            pygame.freetype.init()
        except pygame.error as e:
            self.log.add(repr(pico8_init_error(e)))

        #self.init_defaults()

        self.init_colour()

        self.parse_config()
        self.init_display()
        self.load_font()
        self.init_camera()
        self.boot()
        self.init_time()

    def init_defaults(self):
        self.fullscreen = False
        self.framerate = 30

    def init_log(self) -> None:
        self.log = log()

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

    def parse_config(self) -> None:
        try:
            config_name = self.cart.config_name
        except AttributeError:
            config_name = 'config.ini'

        ini = configparser.ConfigParser()

        if not os.path.isfile(config_name):
            ini['DEFAULT'] = {
                'up':'1073741906',
                'down':'1073741905',
                'left':'1073741904',
                'right':'1073741903',
                'button_0':'122',
                'button_1':'120',
                'esc':'27',
                'fullscreen':'0', # 0 means False, else is True (aka 1)
                'framerate':'30'
            }

            with open(config_name,'w') as ini_file:
                ini.write(ini_file)

        ini.read(config_name)

        self.keys = [
            int(ini['DEFAULT']['up']),
            int(ini['DEFAULT']['down']),
            int(ini['DEFAULT']['left']),
            int(ini['DEFAULT']['right']),
            int(ini['DEFAULT']['button_0']),
            int(ini['DEFAULT']['button_1']),
            int(ini['DEFAULT']['esc']),
        ]
        self.fullscreen = False if int(ini['DEFAULT']['fullscreen'])==0 else True
        self.framerate = int(ini['DEFAULT']['framerate'])

        # checking overrides
        #ini.read(config_name)
        for override_section in ini.sections():
            try:self.keys[0] = int(ini[override_section]['up'])
            except KeyError:pass

            try:self.keys[1] = int(ini[override_section]['down'])
            except KeyError:pass

            try:self.keys[2] = int(ini[override_section]['left'])
            except KeyError:pass

            try:self.keys[3] = int(ini[override_section]['right'])
            except KeyError:pass

            try:self.keys[4] = int(ini[override_section]['button_0'])
            except KeyError:pass

            try:self.keys[5] = int(ini[override_section]['button_1'])
            except KeyError:pass

            try:self.keys[6] = int(ini[override_section]['esc'])
            except KeyError:pass

            try:self.fullscreen = False if int(ini[override_section]['fullscreen'])==0 else True
            except KeyError:pass

            try:self.framerate = int(ini[override_section]['framerate'])
            except KeyError:pass

    def init_display(self) -> None:

        try:
            pygame.display.set_caption(self.cart.cart_name)
        except AttributeError:
            pygame.display.set_caption('Untitled Hagia Cart')

        try:
            icon = pygame.image.load(self.cart.icon)
        except AttributeError:
            try:
                icon = pygame.image.load('hagia.png')
            except FileNotFoundError:
                icon = None

        pygame.display.set_icon(icon) if icon != None else None
        del(icon)

        height = pygame.display.Info().current_h
        if self.fullscreen:
            self.multiplier = math.floor(height / 128)

            width = pygame.display.Info().current_w

            self.global_offset_x = math.floor(width / 2) - math.floor((128 * self.multiplier) / 2)
            self.global_offset_y = math.floor(height / 2) - math.floor((128 * self.multiplier) / 2)

            self.dimensions = (width, height)
            flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF

            self.screen = pygame.display.set_mode(self.dimensions,flags)

            del(width)
        else:
            self.multiplier = math.floor(height / 128) - 1
            self.dimensions = (128 * self.multiplier, 128 * self.multiplier)
            self.global_offset_x = 0
            self.global_offset_y = 0

            #flags = pygame.NOFRAME

            self.screen = pygame.display.set_mode(self.dimensions)#,flags)

        del(height)

    def init_time(self):
        self.game_clock = pygame.time.Clock()

    def init_camera(self):
        self.camera_x:int = 0
        self.camera_y:int = 0

    def boot(self):
        # boot sequence

        frames:int = 70
        flicker = False
        boot_clock = pygame.time.Clock()

        boot_loop = True

        while boot_loop:
            self.cls(0)
            self.pump()
            self.register_events()

            # flicker
            if frames > 65:
                if flicker:
                    self.cls(6)
                flicker = not flicker
            elif frames < 63:
                self.print('untitled engine',8,8,7,0,size=6)#size=35)

            if frames < 60:
                self.print('booting . . .',8,18,6,0)

            if frames<=50:
                boot_loop = False

            frames-=1

            self.clear_events()
            self.flip()
            boot_clock.tick(15)

        del(frames)
        del(flicker)
        del(boot_clock)
        del(boot_loop)

    # old trash reset func that is totally wrong
    #def reset(self):
    #    self.boot()
    #    self.init_time()

    def shutdown(self):
        pygame.quit()
        self.log.export()
        sys.exit()

    def flip(self):
        pygame.display.flip()

    def sleep(self,x):
        time.sleep(x)

    def cls(self,col):
        self.screen.fill(self.colours[col])

    def pump(self):
        pygame.event.pump()

    def register_events(self):
        self.events = [event.type for event in pygame.event.get()]
        self.key_events = pygame.key.get_pressed()

    def clear_events(self):
        pygame.event.clear()
        del(self.events)
        del(self.key_events)

    #def __del__(self):
    #    self.shutdown()


    # graphics
    # ==========

    def clip(
        self,
        x,
        y,
        w,
        h,
        clip_previous:bool=False
    ):
        pass

    def pset(
        self,
        x,
        y,
        col:int=0
    ):
        pass

    def pget(self,x,y):
        pass

    def sget(self,x,y):
        pass

    def sset(self,x,y,col:int=0):
        pass

    def fget(self,n,f:int) -> bool:
        return self.flags[n][f]

    def fset(self,n,val:bool,f:int) -> None:
        self.gfx_data[n][f] = val

    def print(
        self,
        text,
        x,
        y,
        fgcolor=0,
        bgcolor=0,
        #style=pygame.STYLE_DEFAULT,
        #rotation=0,
        size=4
    ):
        self.font.render_to(self.screen,((x*self.multiplier)+self.global_offset_x+self.camera_x,(y*self.multiplier)+self.global_offset_y+self.camera_y),text,fgcolor=self.colours[fgcolor],bgcolor=self.colours[bgcolor],
            #style=style,
            #rotation=rotation,
            size=size*self.multiplier
        )


    def cursor(self,x,y,col:int=0):
        pass

    def color(self,col:int=0):
        pass

    def camera(self,x:int=0,y:int=0):
        self.camera_x = x
        self.camera_y = y

    def circ(
        self,
        x,
        y,
        r,
        col:int=0,
        width=1
    ):
        surf = pygame.Surface(((r*2)+1,(r*2)+1))
        surf.fill(self.colours[0])

        pygame.draw.circle(
            surf,
            self.colours[col],
            (
                0+r,
                0+r
            ),
            r,
            width=width*self.multiplier
        )

        surf.set_colorkey(self.colours[0])

        self.screen.blit(
            pygame.transform.scale(surf,(((r*2)+1)*self.multiplier,((r*2)+1)*self.multiplier)),
            #self.colours[col]
            (
                (x*self.multiplier)+self.global_offset_x+(self.camera_x * self.multiplier) - ((r+1) * self.multiplier),
                (y*self.multiplier)+self.global_offset_y+(self.camera_y * self.multiplier) - ((r+1) * self.multiplier)
            )
        )
        del(surf)

    def circfill(
        self,
        x,
        y,
        r,
        col:int=0
    ):
        surf = pygame.Surface(((r*2)+1,(r*2)+1))
        surf.fill(self.colours[0])

        pygame.draw.circle(
            surf,
            self.colours[col],
            (
                0+r,
                0+r
            ),
            r,
            width=0
        )

        surf.set_colorkey(self.colours[0])

        self.screen.blit(
            pygame.transform.scale(surf,(((r*2)+1)*self.multiplier,((r*2)+1)*self.multiplier)),
            #self.colours[col]
            (
                (x*self.multiplier)+self.global_offset_x+(self.camera_x * self.multiplier) - ((r+1) * self.multiplier),
                (y*self.multiplier)+self.global_offset_y+(self.camera_y * self.multiplier) - ((r+1) * self.multiplier)
            )
        )
        del(surf)

    def oval(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ):
        rect = pygame.Rect(
            (x0*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
            (y0*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier),
            (x1-x0*self.multiplier),
            (y1-y0*self.multiplier)
        )
        pygame.draw.ellipse(
            self.screen,
            self.colours[col],
            rect,
            width=0
        )

    def ovalfill(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0,
        width=1
    ):
        rect = pygame.Rect(
            (x0*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
            (y0*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier),
            (x1-x0*self.multiplier),
            (y1-y0*self.multiplier)
        )
        pygame.draw.ellipse(
            self.screen,
            self.colours[col],
            rect,
            width=width*self.multiplier
        )

    def line(
        self,
        x0,
        y0,
        x1=None,
        y1=None,
        col:int=0
    ):
        pygame.draw.line(
            self.screen,
            self.colours[col],
            ((x0*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),(y0*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier)),
            ((x1*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),(y1*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier)),
            width=1*self.multiplier
        )

    def rect(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ):
        rect = pygame.Rect(
            (x0*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
            (y0*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier),
            ((x1-x0)*self.multiplier),
            ((y1-y0)*self.multiplier)
        )
        pygame.draw.rect(self.screen,self.colours[col],rect,width=1*self.multiplier)

    def rectfill(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ):
        rect = pygame.Rect(
            (x0*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
            (y0*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier),
            ((x1-x0)*self.multiplier),
            ((y1-y0)*self.multiplier)
        )
        pygame.draw.rect(self.screen,self.colours[col],rect,width=0)

    def polygon(
        self,
        x,
        y,
        col:int=0,
        points=[]
    ):
        # will raise the error since default points only has nothing,
        # and requires 3 or more points to justify a polygon
        temp_surf = pygame.Surface((8+1,8+1)).convert()
        #temp_surf.set_colorkey = self.colours[0]
        pygame.draw.polygon(temp_surf,self.colours[col],points)
        scaled_temp_surf = pygame.transform.scale(temp_surf,(8*self.multiplier / 2,8*self.multiplier / 2))
        del(temp_surf)
        self.screen.blit(
            scaled_temp_surf,
            (
                (x*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
                (y*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier)
            )
        )
        del(scaled_temp_surf)

    #@pal.register

    #@overload
    #def pal(self,tbl:dict,p:int=0):
    #    raise NotImplementedError('Nobody uses this. gtfo.')

    #@overload
    def pal(self,
        c0:int,
        c1:int,
        p:int=0
    ):
        # p = 0 or 1 // 0 : Draw palette (the sprites) // 1 : Display palette (entire screen)
        if p == 0:
            colour_palette = self.colours
            colour_palette[c0] = self.colours[c1]
            for spr in self.gfx_data:
                #pal = self.colours
                #pal[c0] = pal[c1]
                spr.set_palette([colour for colour in colour_palette])
                spr.set_colorkey(self.colours[0])


        elif p == 1:
            palette = self.colours
            palette[c0] = self.colours[c1]
            self.screen.set_palette([colour for colour in palette])

            del(palette)

        else:
            raise NotImplementedError('p must be in this value range: 0 <= p <= 1')

    #@singledispatch
    #@overload
    def rpal(self):
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

        for spr in self.gfx_data:
            spr.set_colorkey(self.colours[0])

        #self.screen.set_palette([color for color in self.colours])
        #for spr in self.gfx_data:
        #    spr.set_palette([color for color in self.colours])

    def palt(self,c,t:bool=False):
        pass

    def spr(
        self,
        n,
        x,
        y,
        wh:tuple=(8,8),
        flip_x:bool=False,
        flip_y:bool=False
    ):
        #assert flip_y==False and len(self.gfx_data)==128, sys.exit('Sprites imported by atlas cannot be flipped on the y axis')
        self.screen.blit(
            pygame.transform.flip(self.gfx_data[int(n)],flip_x=flip_x,flip_y=flip_y),
            (
                (x*self.multiplier)+self.global_offset_x+(self.camera_x*self.multiplier),
                (y*self.multiplier)+self.global_offset_y+(self.camera_y*self.multiplier)
            ),
            (0,0,8*self.multiplier,8*self.multiplier)
        )

    def sspr(
        self,
        sx,
        sy,
        sw,
        sh,
        dx,
        dh,
        d_wh:tuple=(None,None),
        flip_x:bool=False,
        flip_y:bool=False
    ):
        pass

    def fillp(self,p):
        pass


    # math
    # =============

    def max(self,x,y):
        return max(x,y)

    def min(self,x,y):
        return min(x,y)

    def mid(self,x,y,z):
        raise NotImplementedError('mid is not implemented')

    def flr(self,x) -> int:
        return math.floor(x)

    def ceil(self,x) -> int:
        return math.ceil(x)

    def xround(self,x) -> int:
        return math.floor(x+0.5)

    def cos(self,x) -> int:
        return self.ceil(-1 * math.cos(x))

    def sin(self,x) -> int:
        return self.ceil(-1 * math.sin(x))
        #return self.ceil(math.sin(x))

    def atan2(self,dx,dy) -> float:
        vec = pygame.math.Vector2((x,y))
        return vec.to_angle()

    def sqrt(self,x) -> int:
        return math.ceil(math.sqrt(x))

    def abs(self,x):
        return abs(x)

    def rnd(self,x) -> int:
        return self.flr(random.random() * x)

    def srand(self,x) -> None:
        random.seed(x)


    # input
    # ==========

    def btn(self,x:int) -> bool:
        #if self.key_events[self.keys[x]]:
        #    return True
        #return False
        return self.key_events[self.keys[x]]

    def btnp(self,x) -> bool:
        pass

    # tables
    # ===========

    def add(self,tbl,val,index:int=-1) -> None:
        if not index>-1:tbl.append(val);return
        tbl[index]=val

    def delete(self,tbl,val) -> None:
        tbl.remove(val)

    def deli(self,tbl,i:int=-1) -> None:
        del(tbl[i])

    def count(self,tbl,val=None) -> int:
        if val==None:return len(tbl)
        amount = 0
        for value in tbl:
            if value==val:amount+=1
        return amount

    def all(self,tbl):
        return tbl

    def foreach(self,tbl,func) -> None:
        for element in tbl:
            func(element)

    def pairs(self,tbl): # for dictionaries
        pass

    # audio
    # ===========

    def sfx(
        self,
        n:int,
        fade_len:int=0,
        channel_mask:int=0
    ) -> None:
        if n <= -1:
            pygame.mixer.stop()
            return
        self.sfx_data[n].play()

    def music(
        self,
        n:int,
        start:float=0.0,
        fade_len:int=0,
        channel_mask:int=0
    ) -> None:
        if n <= -1:
            pygame.mixer.music.fadeout(fade_len)
            return

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
        pygame.mixer.music.load(self.music_data[n],"ogg")
        pygame.mixer.music.play(loops=-1,start=start,fade_ms=fade_len)

    # map
    # ========

    #@overload
    def map(
        self,
        cel_x,
        cel_y,
        sx=0,
        sy=0,
        cel_w=128,
        cel_h=64,
        layer=None
    ) -> None:
        cell_x = cel_x
        cell_y = cel_y
        x = (sx * self.multiplier) + (self.camera_x * self.multiplier)
        y = (sy * self.multiplier) + (self.camera_y * self.multiplier)
        cell_w = cel_w
        cell_h = cel_h

        if type(layer)==int:
            for w in range(cell_w):
                for h in range(cell_h):

                    mget = self.mget(
                        cell_x+w,
                        cell_y+h
                    )
                    #print(mget)
                    if self.fget(mget,layer):
                        self.spr(mget,(sx+w)*8,(sy+h)*8,flip_x=False,flip_y=False)
        elif layer == None:
            for w in range(cell_w):
                for h in range(cell_h):

                    mget = self.mget(
                        cell_x+w,
                        cell_y+h
                    )
                    #print(mget)
                    #if self.fget(mget,layer):
                    self.spr(mget,(sx * 8)+(w * 8),(sy * 8)+(h * 8),flip_x=False,flip_y=False)


    def mapdraw(
        self,
        cel_x,
        cel_y,
        sx,
        sy,
        cel_w,
        cel_h,
        layer=0
    ) -> None:
        pass

    def mget(self,x:int,y:int) -> int:
        return self.map_data[(y * 128) + x]

    def mset(self,x:int,y:int,v:int) -> None:
        self.map_data[(y * 128) + x] = v if type(v) == int else None


    # strings
    # ==========

    def sub(
        self,
        _str:str,
        _from:int,
        _to:int=None
    ) -> str:
        _to = _from + 1 if _to == None else _to
        return _str[_from:_to]

    def tostr(
        self,
        val,
        _hex:bool=False
    ) -> str:
        return str(val) if not _hex else str(hex(val))

    def tonum(
        self,
        _str:str
    ) -> float or int:
        try:
            return int(_str)
        except ValueError:
            return float(_str)
