import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import (
    freetype,
    display,
    draw,
    image,
    Surface,
    Color,
    Rect,
    transform
)
from pygame.locals import *

sys.stdout = _stdout
del _stdout
del sys

from .defs import HAGIA_SPECS
from .atlas import Atlas
from .utils import *
from os import path
from functools import cached_property

#CURRENT_DRAWING_COLOUR = None

class GraphicSystem(object):
    def __init__(self):
        pass

    def init_graphics(self):

        display.init()
        freetype.init()

        self.__init_colour_palette__()

        self.__init_display_stuff__()

        #self.pal_mode = 0 # 16 would start at palette index 0

        self.previous_line_x1 = 0
        self.previous_line_y1 = 0

    def __init_display_stuff__(self):

        flgs = SCALED | FULLSCREEN # pygame.SCALED

        display.set_caption(self.cart.c_name)
        if not self.cart.c_icon_img is None:
            display.set_icon(image.load(
                    path.join(
                        self.cart.c_data_directory,
                        self.cart.c_icon_img
                    )
                )
            )

        # virtual screen
        self.vscr = display.set_mode(
            (HAGIA_SPECS.SCREEN_W,HAGIA_SPECS.SCREEN_H),
            flgs#,depth=8
        )
        # "real" screen
        self.scr = Surface(
            (HAGIA_SPECS.SCREEN_W,HAGIA_SPECS.SCREEN_H),
            #depth=HAGIA_SPECS.BIT_DEPTH
        )

        self.atlas = Surface(
            (HAGIA_SPECS.ATLAS_WIDTH, HAGIA_SPECS.ATLAS_HEIGHT),
            #depth=HAGIA_SPECS.BIT_DEPTH
        )
        self.atlas.set_colorkey(self.default_colours[0])

    async def load_graphics_data(self):
        if (
            hasattr(self.cart,"gfx") and
            self.cart.gfx != None and
            type(self.cart.gfx) is str
        ):
            self.atlas = Atlas.load_(path.join(self.cart.c_data_directory,self.cart.gfx))
            #self.atlas.convert(8)
            #self.atlas.set_palette(self.default_colours)
            #self.atlas.set_colorkey(self.default_colours[0])

        if (
            hasattr(self.cart,"palette")
        ):
            self._default_colours = list(self.cart.palette)
            self.colours = self.default_colours

    @cached_property
    def vscreen(self):
        return display.get_surface()

    def flip(self):
        display.flip()

    def cls(self,x):
        self.scr.fill(self.colours[x])

    def render(self):
        self.vscreen.fill(self.colours[0]) # reset virtual screen before
        # ----- testing atlas blit --------
        #self.scr.blit(self.atlas,(0,0))
        # ---------------------------------
        self.vscreen.blit(self.scr,(0,0))  # blitting new
        self.flip()
        self.scr.set_clip(None) # reset clipping region before
        #self.cls(0)             # clearing screen


    def __init_colour_palette__(self):
        self._default_colours:list = [
            Color(0,0,0,255),
            Color(29,43,83,255),
            Color(126,37,83,255),
            Color(0,135,81,255),
            Color(171,82,54,255),
            Color(95,87,79,255),
            Color(194,195,199,255),
            Color(255,241,232,255),
            Color(255,0,77,255),
            Color(255,163,0,255),
            Color(255,236,39,255),
            Color(0,228,54,255),
            Color(41,173,255,255),
            Color(131,118,156,255),
            Color(255,119,168,255),
            Color(255,204,170,255),
        ]
        self.colours = self.default_colours
        self.vcolours:dict = {
            0:0,
            1:1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            11:11,
            12:12,
            13:13,
            14:14,
            15:15
        }
        #self.scr.set_palette(self.colours)

    def clip(self,
        x:int,
        y:int,
        w:int,
        h:int,
        clip_previous:bool=False
    ) -> None:
        if not clip_previous:
            self.scr.set_clip(None)
        self.scr.set_clip(
            Rect( flr(x), flr(y), flr(w), flr(h) )
        )

    def pset(
        self,
        x:int,
        y:int,
        col:int=0
    ) -> None:
        self.scr.set_at(
            (flr(x),flr(y)),
            self.colours[self.vcolours[col]]
        )

    def pget(
        self,
        x:int,
        y:int,
    ) -> None:
        try:
            pix_at = self.scr.get_at((flr(x),flr(y)))
        except IndexError:
            print("Warning: Pixel grabbed is outside of the screen. Returning default 0.")
            return 0
        for i,c in enumerate(self.colours,start=0):
            if pix_at == c:
                return i

    def sget(
        self,
        x:int,
        y:int
    ) -> None:
        try:
            pix_at = self.atlas.get_at((flr(x),flr(y)))
        except IndexError:
            print("Warning: Pixel grabbed is outside of the screen. Returning default 0.")
            return 0
        for i,c in enumerate(self.colours,start=0):
            if pix_at == c: return i

    def sset(
        self,
        x:int,
        y:int,
        col:int=0
    ) -> None:
        self.atlas.set_at(
            (flr(x),flr(y)),
            self.colours[self.vcolours[col]]
        )

    def spr(
        self,
        n:int,
        x:int,
        y:int,
        w:int=1,
        h:int=1,
        flip_x:bool=False,
        flip_y:bool=False
    ) -> None:
    
        n = flr(n)
        _pos_xy:tuple = (x+self._camera.x,y+self._camera.y)

        surf = Surface((8,8))
        surf.set_colorkey(self.colours[self.vcolours[0]])
        data_sample = self.atlas[n*64:n*64+64]
        for i,d in enumerate(data_sample,start=0):
            x = i % 8
            y = flr(i/8)
            #if not d == 0:
            draw.rect(
                    surf,
                    self.colours[self.vcolours[d]],
                    Rect(x,y,1,1)
                )

        if flip_x or flip_y:
            self.scr.blit(
                transform.flip(
                    surf,
                    flip_x,
                    flip_y
                ),
                _pos_xy
            )
            return

        self.scr.blit(
            surf,
            _pos_xy
        )

    def sspr(
        self,
        sx:int,
        sy:int,
        sw:int,
        sh:int,
        dx:int,
        dy:int,
        dw:int=None,
        dh:int=None,
        flip_x:bool=False,
        flip_y:bool=False
    ) -> None:
        #if dw is None:
        #    dw:int = sw
        #if dh is None:
        #    dh:int = sh

        dw:int = sw if dw is None else dw
        dh:int = sh if dh is None else dh

        _rect:Rect = Rect(
            sx*HAGIA_SPECS.BASE_SPRITE_SIZE,
            sy*HAGIA_SPECS.BASE_SPRITE_SIZE,
            sw*HAGIA_SPECS.BASE_SPRITE_SIZE,
            sh*HAGIA_SPECS.BASE_SPRITE_SIZE
        )

        _pos_xy:tuple = (dx+self._camera.x,dy+self._camera.y)

        _surf:Surface = transform.scale(
            self.atlas.subsurface(_rect), # <-- returns a surface
            (dw*HAGIA_SPECS.BASE_SPRITE_SIZE,dh*HAGIA_SPECS.BASE_SPRITE_SIZE),
            dest_surface=None
        )

        self.scr.blit(
            transform.flip(
                _surf,
                flip_x,
                flip_y,
            ),
            _pos_xy
        )

    def pal(
        self,
        c0:int,
        c1:int,
        p:int=0
    ) -> None:
        if p == 0:
            self.dpal(int(c0),int(c1))
        elif p == 1:
            pass
        elif p == 2:
            pass

    def dpal(
        self,
        c0:int,
        c1:int
    ) -> None:
        #self.vcolours[c0] ^= self.vcolours[c1]
        #self.vcolours[c1] ^= self.vcolours[c0]
        #self.vcolours[c0] ^= self.vcolours[c1]
        self.vcolours[c0] = c1 #self.vcolours[c1]

    def rpal(
        self,
        *args
    ) -> None:
        self.vcolours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    def hprint(
        self,
        #_str:str
        *args,
        **kwargs
    ):
        pass

    def circ(
        self,
        x:int,
        y:int,
        r:int,
        col:int = 0
    ) -> None:
        draw.circle(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            (int(x)+self._camera.x,int(y)+self._camera.y),
            int(r),
            width=1
        )

    def circfill(
        self,
        x:int,
        y:int,
        r:int,
        col:int = 0
    ) -> None:
        draw.circle(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            (int(x)+self._camera.x,int(y)+self._camera.y),
            int(r)
        )

    def rect(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ) -> None:
        x0 = int(x0) + self._camera.x
        x1 = int(x1) + self._camera.x
        y0 = int(y0) + self._camera.y
        y1 = int(y1) + self._camera.y
        draw.rect(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            Rect(
                x0,
                y0,
                (x1-x0),
                (y1-y0)
            ),
            width=1
        )

    def rectfill(
        self,
        x0,
        y0,
        x1,
        y1,
        col:int=0
    ) -> None:
        x0 = int(x0) + self._camera.x
        x1 = int(x1) + self._camera.x
        y0 = int(y0) + self._camera.y
        y1 = int(y1) + self._camera.y
        draw.rect(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            Rect(
                x0,
                y0,
                (x1-x0),
                (y1-y0)
            )
        )

    def oval(
        self,
        x0:int,
        y0:int,
        x1:int,
        y1:int,
        col:int=0
    ) -> None:
        x0 = int(x0) + self._camera.x
        x1 = int(x1) + self._camera.x
        y0 = int(y0) + self._camera.y
        y1 = int(y1) + self._camera.y
        draw.ellipse(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            Rect(
                x0,
                y0,
                (x1-x0),
                (y1-y0),
            ),
            width=1
        )
    def ovalfill(
        self,
        x0:int,
        y0:int,
        x1:int,
        y1:int,
        col:int=0
    ) -> None:
        x0 = int(x0) + self._camera.x
        x1 = int(x1) + self._camera.x
        y0 = int(y0) + self._camera.y
        y1 = int(y1) + self._camera.y
        draw.ellipse(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            Rect(
                x0,
                y0,
                (x1-x0),
                (y1-y0),
            )
        )

    def line(
        self,
        x0:int,
        y0:int,
        x1:int=None,
        y1:int=None,
        col:int=0
    ) -> None:
        x0 = int(x0)
        y0 = int(y0)
        x1 = self.previous_line_x1 if x1 is None else int(x1)
        y1 = self.previous_line_y1 if y1 is None else int(y1)
        self.previous_line_x1 = x1 if not x1 is None else self.previous_line_x1
        self.previous_line_y1 = y1 if not y1 is None else self.previous_line_y1

        draw.line(
            self.scr,
            self.colours[self.vcolours[int(col)]],
            (x0+self._camera.x,y0+self._camera.y),
            (x1+self._camera.x,y1+self._camera.y)
        )

    @cached_property
    def default_colours(self) -> list:
        return self._default_colours
