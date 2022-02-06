from hagia.error import atlas_error

import sys
import os

_stdout = sys.stdout
sys.stdout = open(os.devnull,'w')

import pygame

sys.stdout = _stdout
del(_stdout)
del(sys)
del(os)

class atlas2:
    def __init__(self, atlas:str):
        #super().__init()
        try:
            self._atlas = pygame.image.load_basic(atlas)
            #self._atlas = pygame.image.fromstring(bytes.fromhex(atlas),(128,64),"P").convert()
        except ValueError as e:
            print(repr(e))
        except pygame.error as e:
            print(repr(atlas_error(e)))
    @property
    def atlas(self):
        return self._atlas

    @atlas.setter
    def atlas(self, val):
        self._atlas = val

    @atlas.deleter
    def atlas(self):
        del(self._atlas)

    def load(
        self,
        multiplier:int,
        colorkey=(0,0,0,255)
    ):
        """sprites = []
        flags = pygame.RLEACCEL
        for row in range(8):
            for item in range(16):
                spr = pygame.Surface((8,8),depth=8)
                spr.blit(self.atlas,(0,0),(item*8,row*8,8,8))
                spr_scaled = pygame.transform.scale(spr,(8*multiplier,8*multiplier))
                spr_scaled.convert(8)
                spr_scaled.set_colorkey(colorkey,flags)
                sprites.append(spr_scaled)
                del(spr)
                del(spr_scaled)
                #del(spr_size)
        return [sprites[index] for index,spr in enumerate(sprites,start=0)]"""
        flags = pygame.RLEACCEL
        scaled_atlas = pygame.transform.scale(self.atlas,(128*multiplier,64*multiplier))
        scaled_atlas.convert(8)
        scaled_atlas.set_colorkey(colorkey,flags)
        return scaled_atlas

class atlas:
    def __init__(self, atlas:str):
        #super().__init()
        try:
            self._atlas = pygame.image.load_basic(atlas)
            #self._atlas = pygame.image.fromstring(bytes.fromhex(atlas),(128,64),"P").convert()
        except ValueError as e:
            print(repr(e))
        except pygame.error as e:
            print(repr(atlas_error(e)))
    @property
    def atlas(self):
        return self._atlas

    @atlas.setter
    def atlas(self, val):
        self._atlas = val

    @atlas.deleter
    def atlas(self):
        del(self._atlas)

    def load(
        self,
        multiplier:int,
        colorkey=(0,0,0,255)
    ):
        sprites = []
        flags = pygame.RLEACCEL
        for row in range(8):
            for item in range(16):
                spr = pygame.Surface((8,8),depth=8)
                spr.blit(self.atlas,(0,0),(item*8,row*8,8,8))
                spr_scaled = pygame.transform.scale(spr,(8*multiplier,8*multiplier))
                spr_scaled.convert(8)
                spr_scaled.set_colorkey(colorkey,flags)
                sprites.append(spr_scaled)
                del(spr)
                del(spr_scaled)
                #del(spr_size)
        return [sprites[index] for index,spr in enumerate(sprites,start=0)]

"""class atlas(object):
    def __init__(self,atlas):
        self.sprites:list = []

        # can take a path, or bytes / buffer / etc.
        self._atlas = atlas

    @property
    def atlas(self):
        return self._atlas

    @atlas.setter
    def atlas(self,value) -> None:
        self._atlas = value

    @atlas.deleter
    def atlas(self):
        del(self._atlas)

    def load_atlas(self):
        if type(self.atlas)==bytes:
            # format is P which means 8 bit. unfortunately pygame
            # won't do 4 bit which is the truth of the pico8
            img = pygame.image.frombuffer(self.atlas,(128,64),"P")
        elif type(self.atlas)==str:
            try:
                img = pygame.image.fromstring(bytes.fromhex(self.atlas))
            except TypeError:
                img = pygame.image.load_basic(self.atlas)
        else:
            #raise atlas_error(f"""#Unable to load data type {str(type(self.atlas))}.
            #                    Must be either file path (string) or bytes.""")

        # loop through every image in the atlas
        # -- the atlas is automatically assumed to be 128x64 --
        #for row in range(8):
        #    for sprite in range(16):
        #        pass



    #@property
    #def gfx(self):
    #    return self.sprites

    #@gfx.setter
    #def gfx(self,value):
    #    self.sprites = value

    #@gfx.deleter
    #def gfx(self):
    #    del(self.sprites)

    #def kill(self):
    #    del(self)"""
