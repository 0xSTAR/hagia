import io
from os import path
from .defs import HAGIA_SPECS
from .utils import *
from numba import jit

class MapSystem(object):
    def __init__(self):
        pass

    def init_map(self):
        self._map:list = []
        for q in range(HAGIA_SPECS.MAX_MAP_DATA):
            self._map.append(0)

    async def load_map_data(self) -> None:
        if type(self.cart.map) is str:
            self.load_map_str(self.cart.c_data_directory,self.cart.map)
        elif type(self.cart.map) is list:
            self.load_map_list(self.cart.map)

    def load_map_list(self,_mdata:list) -> None:
        for i,m in enumerate(_mdata,start=0):
            self._map[i] = m

    def load_map_str(self,data_dir:str,_mdata) -> None:
        data = io.open(path.join(data_dir,_mdata),mode='r')
        rinsed_data = list(
            filter(
                None,data.read().replace("\n","").split(",")
            )
        )
        data.close()
        #del data
        self._map = [int(d) for d in rinsed_data]
        #for i,_md in enumerate(rinsed_data,start=0):
        #    # preserve map data that isn't filled potentially
        #    self._map[i] = int(_md)
        #del rinsed_data


    # the funcs

    def mget(self,x:int,y:int) -> int:
        return self._map[
            (HAGIA_SPECS.MAP_WIDTH * y) + x
        ]

    def mset(self,x:int,y:int,v:int) -> None or int:
        if (
            x < 0 or y < 0 or
            x >= HAGIA_SPECS.MAP_WIDTH or
            y >= HAGIA_SPECS.MAP_HEIGHT
        ):
            return 0
        self._map[(HAGIA_SPECS.MAP_WIDTH * y) + x] = v

    def mapdraw(
        self,
        cell_x :int,
        cell_y :int = 0,
        sx :int=0,
        sy :int=0,
        cell_w :int = 128,
        cell_h :int = 32,
        layers :int = None,
        secret_flip_x = False,
        secret_flip_y = False
    ) -> None:
        #if type(layer) is int:
        if not layers is None:
            for w in range(cell_w):
                for h in range(cell_h):
                    _spr_to_draw = self.mget(cell_x+w,cell_y+h)
                    if self.fget(
                        _spr_to_draw,
                        layers
                    ):
                        self.spr(
                            _spr_to_draw,
                            (sx+w)*HAGIA_SPECS.BASE_TILE_SIZE,
                            (sy+h)*HAGIA_SPECS.BASE_TILE_SIZE,
                            flip_x=secret_flip_x,
                            flip_y=secret_flip_y
                        )


        elif layers is None:
            pass
