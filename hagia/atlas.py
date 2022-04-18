import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import (
    image,
)

sys.stdout = _stdout
del _stdout
del sys

class Atlas(object):
    def __init__(self):
        pass

    @staticmethod
    def load(
        #self,
        _path_to_atlas_bmp:str
    ):
        _atlas = image.load_basic(_path_to_atlas_bmp)
        return _atlas
