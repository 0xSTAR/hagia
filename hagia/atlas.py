import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import (
    image,
)

sys.stdout = _stdout
del _stdout
del sys

import io

class Atlas(object):
    def __init__(self):
        pass

    @staticmethod
    def load_(_path_to_atlas_data:str) -> list:
        _tmp = io.open(_path_to_atlas_data,mode='r')
        rinsed_tmp = list(
            filter(
                None,_tmp.read().replace("\n","").split(",")
            )
        )
        _tmp.close()
        rinsed_tmp = [int(r) for r  in rinsed_tmp]
        #print(rinsed_tmp)
        return rinsed_tmp
    #@staticmethod
    #def load(
    #    #self,
    #    _path_to_atlas_bmp:str
    #):
    #    _atlas = image.load_basic(_path_to_atlas_bmp)
    #    return _atlas
