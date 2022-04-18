from dataclasses import dataclass
from .defs import HAGIA_SPECS

from os import path
import io

@dataclass
class FlagObj:
    flags:list

    def _set(
        self,
        f:int,v:int
    ) -> None:
        self.flags[f] = v

    def _set_all(
        self,v:int
    ) -> None:
        for flg in self.flags:
            flg = v

class FlagSystem(object):
    def __init__(self):
        pass

    def init_flags(self):
        default_flags:list = [
        #False,False,False,False,
        #False,False,False,False
        0,0,0,0,0,0,0,0
        ]
        self._flags = []
        for q in range(HAGIA_SPECS.MAX_SPRITES):
            self._flags.append(
                FlagObj(default_flags)
            )

        del default_flags

    async def load_flag_data(self):
        if type(self.cart.flags) is list:
            self.load_flags_list(self.cart.flags)
        elif type(self.cart.flags) is str:
            self.load_flags_path(self.cart.c_data_directory,self.cart.flags)

    def load_flags_list(self,_flg_d) -> None:
        for i,sublist in enumerate(_flg_d,start=0):
            self._flags[i].flags = sublist

    def load_flags_path(self,data_dir,_flg_p) -> None:
        data = io.open(path.join(data_dir,_flg_p), mode='r')
        rinsed_data:list = list(filter(None,data.read().split("\n")))
        data.close()
        del data

        for i, _flg_list in enumerate(rinsed_data,start=0):
            flags_override:list = [0,0,0,0,0,0,0,0]
            #for q in range(len(_flg_list)):
            #    flags_override[q] = bool(int(_flg_list[q]))
            for i2,_flg in enumerate(_flg_list,start=0):
                flags_override[i2] = int(_flg)
            self._flags[i].flags = flags_override
        del rinsed_data




    def fget(
        self,
        n:int,
        f:int=None
    ): # no specified return type as it could be a list or int
        if f is None:
            return self._flags[n].flags
        return self._flags[n].flags[f]

    def fset(
        self,
        n:int,
        f:int=None,
        v:bool=False
    ) -> None:
        if f is None:
            self._flags[n]._set_all(int(v))
        self._flags[n]._set(f,int(v))
