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

        self.pal_mode = 0 # 16 would start at palette index 0

        self.__init_colour_palette__()

        self.previous_line_x1 = 0
        self.previous_line_y1 = 0

    async def load_graphics_data(self):
        if (
            hasattr(self.cart,"gfx") and
            self.cart.gfx != None and
            type(self.cart.gfx) is str
        ):
            self.atlas = Atlas.load(path.join(self.cart.c_data_directory,self.cart.gfx))
            self.atlas.convert(8)
            self.atlas.set_palette(self.default_colours)
            self.atlas.set_colorkey(self.default_colours[0])

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
        self.colours = self.default_colours
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
            self.colours[col]
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
            self.colours[col]
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
        _rect:Rect = Rect(
            (n%HAGIA_SPECS.ATLAS_SPR_COLUMNS)*HAGIA_SPECS.BASE_SPRITE_SIZE,
            (n//HAGIA_SPECS.ATLAS_SPR_COLUMNS)*HAGIA_SPECS.BASE_SPRITE_SIZE, # floor division
            w*HAGIA_SPECS.BASE_SPRITE_SIZE,
            h*HAGIA_SPECS.BASE_SPRITE_SIZE
        )

        _pos_xy:tuple = (x+self._camera.x,y+self._camera.y)

        if flip_x or flip_y:
            _surf:Surface = self.atlas.subsurface(
                _rect
            )
            self.scr.blit(
                transform.flip(
                    _surf,
                    flip_x,
                    flip_y
                ),
                _pos_xy
            )
            del _surf
            return

        self.scr.blit(
            self.atlas,
            _pos_xy,
            _rect
        )

        del _rect

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
        *args
    ) -> None:
        pass

    def dpal(
        self,
        *args
    ) -> None:
        pass

    def rpal(
        self,
        *args
    ) -> None:
        pass

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
            self.colours[int(col)],
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
            self.colours[int(col)],
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
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        draw.rect(
            self.scr,
            self.colours[int(col)],
            Rect(
                x0+self._camera.x,
                y0+self._camera.y,
                (x1-x0)+self._camera.x,
                (y1-y0)+self._camera.y
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
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        draw.rect(
            self.scr,
            self.colours[int(col)],
            Rect(
                x0+self._camera.x,
                y0+self._camera.y,
                (x1-x0)+self._camera.x,
                (y1-y0)+self._camera.y
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
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        draw.ellipse(
            self.scr,
            self.colours[col],
            Rect(
                x0,
                y0,
                (x1-x0)+self._camera.x,
                (y1-y0)+self._camera.y,
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
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        draw.ellipse(
            self.scr,
            self.colours[col],
            Rect(
                x0,
                y0,
                (x1-x0)+self._camera.x,
                (y1-y0)+self._camera.y,
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
            self.colours[col],
            (x0,y0),
            (x1,y1)
        )

    @cached_property
    def default_colours(self) -> list:
        return [
            Color(0, 0, 0, 255),
            Color(29, 43, 83, 255),
            Color(126, 37, 83, 255),
            Color(0, 135, 81, 255),
            Color(171, 82, 54, 255),
            Color(95, 87, 79, 255),
            Color(194, 195, 199, 255),
            Color(255, 241, 232, 255),
            Color(255, 0, 77, 255),
            Color(255, 163, 0, 255),
            Color(255, 236, 39, 255),
            Color(0, 228, 54, 255),
            Color(41, 173, 255, 255),
            Color(131, 118, 156, 255),
            Color(255, 119, 168, 255),
            Color(255, 204, 170, 255),
            Color(0, 146, 0, 255),
            Color(0, 146, 85, 255),
            Color(0, 146, 170, 255),
            Color(0, 146, 255, 255),
            Color(0, 182, 0, 255),
            Color(0, 182, 85, 255),
            Color(0, 182, 170, 255),
            Color(0, 182, 255, 255),
            Color(0, 219, 0, 255),
            Color(0, 219, 85, 255),
            Color(0, 219, 170, 255),
            Color(0, 219, 255, 255),
            Color(0, 255, 0, 255),
            Color(0, 255, 85, 255),
            Color(0, 255, 170, 255),
            Color(0, 255, 255, 255),
            Color(85, 0, 0, 255),
            Color(85, 0, 85, 255),
            Color(85, 0, 170, 255),
            Color(85, 0, 255, 255),
            Color(85, 36, 0, 255),
            Color(85, 36, 85, 255),
            Color(85, 36, 170, 255),
            Color(85, 36, 255, 255),
            Color(85, 73, 0, 255),
            Color(85, 73, 85, 255),
            Color(85, 73, 170, 255),
            Color(85, 73, 255, 255),
            Color(85, 109, 0, 255),
            Color(85, 109, 85, 255),
            Color(85, 109, 170, 255),
            Color(85, 109, 255, 255),
            Color(85, 146, 0, 255),
            Color(85, 146, 85, 255),
            Color(85, 146, 170, 255),
            Color(85, 146, 255, 255),
            Color(85, 182, 0, 255),
            Color(85, 182, 85, 255),
            Color(85, 182, 170, 255),
            Color(85, 182, 255, 255),
            Color(85, 219, 0, 255),
            Color(85, 219, 85, 255),
            Color(85, 219, 170, 255),
            Color(85, 219, 255, 255),
            Color(85, 255, 0, 255),
            Color(85, 255, 85, 255),
            Color(85, 255, 170, 255),
            Color(85, 255, 255, 255),
            Color(170, 0, 0, 255),
            Color(170, 0, 85, 255),
            Color(170, 0, 170, 255),
            Color(170, 0, 255, 255),
            Color(170, 36, 0, 255),
            Color(170, 36, 85, 255),
            Color(170, 36, 170, 255),
            Color(170, 36, 255, 255),
            Color(170, 73, 0, 255),
            Color(170, 73, 85, 255),
            Color(170, 73, 170, 255),
            Color(170, 73, 255, 255),
            Color(170, 109, 0, 255),
            Color(170, 109, 85, 255),
            Color(170, 109, 170, 255),
            Color(170, 109, 255, 255),
            Color(170, 146, 0, 255),
            Color(170, 146, 85, 255),
            Color(170, 146, 170, 255),
            Color(170, 146, 255, 255),
            Color(170, 182, 0, 255),
            Color(170, 182, 85, 255),
            Color(170, 182, 170, 255),
            Color(170, 182, 255, 255),
            Color(170, 219, 0, 255),
            Color(170, 219, 85, 255),
            Color(170, 219, 170, 255),
            Color(170, 219, 255, 255),
            Color(170, 255, 0, 255),
            Color(170, 255, 85, 255),
            Color(170, 255, 170, 255),
            Color(170, 255, 255, 255),
            Color(255, 0, 0, 255),
            Color(255, 0, 85, 255),
            Color(255, 0, 170, 255),
            Color(255, 0, 255, 255),
            Color(255, 36, 0, 255),
            Color(255, 36, 85, 255),
            Color(255, 36, 170, 255),
            Color(255, 36, 255, 255),
            Color(255, 73, 0, 255),
            Color(255, 73, 85, 255),
            Color(255, 73, 170, 255),
            Color(255, 73, 255, 255),
            Color(255, 109, 0, 255),
            Color(255, 109, 85, 255),
            Color(255, 109, 170, 255),
            Color(255, 109, 255, 255),
            Color(255, 146, 0, 255),
            Color(255, 146, 85, 255),
            Color(255, 146, 170, 255),
            Color(255, 146, 255, 255),
            Color(255, 182, 0, 255),
            Color(255, 182, 85, 255),
            Color(255, 182, 170, 255),
            Color(255, 182, 255, 255),
            Color(255, 219, 0, 255),
            Color(255, 219, 85, 255),
            Color(255, 219, 170, 255),
            Color(255, 219, 255, 255),
            Color(255, 255, 0, 255),
            Color(255, 255, 85, 255),
            Color(255, 255, 170, 255),
            Color(255, 255, 255, 255),
            Color(0, 0, 0, 255),
            Color(0, 0, 85, 255),
            Color(0, 0, 170, 255),
            Color(0, 0, 255, 255),
            Color(0, 36, 0, 255),
            Color(0, 36, 85, 255),
            Color(0, 36, 170, 255),
            Color(0, 36, 255, 255),
            Color(0, 73, 0, 255),
            Color(0, 73, 85, 255),
            Color(0, 73, 170, 255),
            Color(0, 73, 255, 255),
            Color(0, 109, 0, 255),
            Color(0, 109, 85, 255),
            Color(0, 109, 170, 255),
            Color(0, 109, 255, 255),
            Color(0, 146, 0, 255),
            Color(0, 146, 85, 255),
            Color(0, 146, 170, 255),
            Color(0, 146, 255, 255),
            Color(0, 182, 0, 255),
            Color(0, 182, 85, 255),
            Color(0, 182, 170, 255),
            Color(0, 182, 255, 255),
            Color(0, 219, 0, 255),
            Color(0, 219, 85, 255),
            Color(0, 219, 170, 255),
            Color(0, 219, 255, 255),
            Color(0, 255, 0, 255),
            Color(0, 255, 85, 255),
            Color(0, 255, 170, 255),
            Color(0, 255, 255, 255),
            Color(85, 0, 0, 255),
            Color(85, 0, 85, 255),
            Color(85, 0, 170, 255),
            Color(85, 0, 255, 255),
            Color(85, 36, 0, 255),
            Color(85, 36, 85, 255),
            Color(85, 36, 170, 255),
            Color(85, 36, 255, 255),
            Color(85, 73, 0, 255),
            Color(85, 73, 85, 255),
            Color(85, 73, 170, 255),
            Color(85, 73, 255, 255),
            Color(85, 109, 0, 255),
            Color(85, 109, 85, 255),
            Color(85, 109, 170, 255),
            Color(85, 109, 255, 255),
            Color(85, 146, 0, 255),
            Color(85, 146, 85, 255),
            Color(85, 146, 170, 255),
            Color(85, 146, 255, 255),
            Color(85, 182, 0, 255),
            Color(85, 182, 85, 255),
            Color(85, 182, 170, 255),
            Color(85, 182, 255, 255),
            Color(85, 219, 0, 255),
            Color(85, 219, 85, 255),
            Color(85, 219, 170, 255),
            Color(85, 219, 255, 255),
            Color(85, 255, 0, 255),
            Color(85, 255, 85, 255),
            Color(85, 255, 170, 255),
            Color(85, 255, 255, 255),
            Color(170, 0, 0, 255),
            Color(170, 0, 85, 255),
            Color(170, 0, 170, 255),
            Color(170, 0, 255, 255),
            Color(170, 36, 0, 255),
            Color(170, 36, 85, 255),
            Color(170, 36, 170, 255),
            Color(170, 36, 255, 255),
            Color(170, 73, 0, 255),
            Color(170, 73, 85, 255),
            Color(170, 73, 170, 255),
            Color(170, 73, 255, 255),
            Color(170, 109, 0, 255),
            Color(170, 109, 85, 255),
            Color(170, 109, 170, 255),
            Color(170, 109, 255, 255),
            Color(170, 146, 0, 255),
            Color(170, 146, 85, 255),
            Color(170, 146, 170, 255),
            Color(170, 146, 255, 255),
            Color(170, 182, 0, 255),
            Color(170, 182, 85, 255),
            Color(170, 182, 170, 255),
            Color(170, 182, 255, 255),
            Color(170, 219, 0, 255),
            Color(170, 219, 85, 255),
            Color(170, 219, 170, 255),
            Color(170, 219, 255, 255),
            Color(170, 255, 0, 255),
            Color(170, 255, 85, 255),
            Color(170, 255, 170, 255),
            Color(170, 255, 255, 255),
            Color(255, 0, 0, 255),
            Color(255, 0, 85, 255),
            Color(255, 0, 170, 255),
            Color(255, 0, 255, 255),
            Color(255, 36, 0, 255),
            Color(255, 36, 85, 255),
            Color(255, 36, 170, 255),
            Color(255, 36, 255, 255),
            Color(255, 73, 0, 255),
            Color(255, 73, 85, 255),
            Color(255, 73, 170, 255),
            Color(255, 73, 255, 255),
            Color(255, 109, 0, 255),
            Color(255, 109, 85, 255),
            Color(255, 109, 170, 255),
            Color(255, 109, 255, 255),
            Color(255, 146, 0, 255),
            Color(255, 146, 85, 255),
            Color(255, 146, 170, 255),
            Color(255, 146, 255, 255),
            Color(255, 182, 0, 255),
            Color(255, 182, 85, 255),
            Color(255, 182, 170, 255),
            Color(255, 182, 255, 255),
            Color(255, 219, 0, 255),
            Color(255, 219, 85, 255),
            Color(255, 219, 170, 255),
            Color(255, 219, 255, 255),
            Color(255, 255, 0, 255),
            Color(255, 255, 85, 255),
            Color(255, 255, 170, 255),
            Color(255, 255, 255, 255),
        ]
