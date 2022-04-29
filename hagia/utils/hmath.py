import random
import math
from dataclasses import dataclass
from functools import lru_cache
from numba import jit,int8,float32
from numba.experimental import jitclass

import sys
_stdout = sys.stdout
sys.stdout = None
import pygame.math
sys.stdout = _stdout
del _stdout
del sys

# min is apart of python
# max is apart of python

vec2ispec = [
    ('x',int8),
    ('y',int8)
]
@jitclass(vec2ispec)
#@dataclass
class Vec2i:
    #x:int
    #y:int
    def __init__(
        self,
        x:int8,
        y:int8
    ) -> None:
        self.x = x
        self.y = y

    def set_to(self,x:int8,y:int8) -> None:
        self.x = x
        self.y = y

vec2fspec = [
    ('x',float32),
    ('y',float32)
]
@jitclass(vec2fspec)
class Vec2f:
    def __init__(
        self,
        x:float32,
        y:float32
    ) -> None:
        self.x:float32 = x
        self.y:float32 = y

#vec2bspec = [
#    ("x",int8),
#    ("y",int8)
#]
#@jitclass(vec2bspec)
#class Vec2b:
#    def __init__(
#        self,
#        x:int8,
#        y:int8
#    ) -> None:
#        self.x = x
#        self.y = y
@dataclass
class Vec2b:
    x:bool
    y:bool

vec4ispec = [
    ("x",int8),
    ("y",int8),
    ("w",int8),
    ("h",int8)
]
@jitclass(vec4ispec)
class Vec4i:
    def __init__(
        self,
        x:int8,
        y:int8,
        w:int8,
        h:int8
    ) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

@lru_cache(maxsize=None)
@jit(nopython=True)
def mid(x,y,z):
    a = [x,y,z]
    a.sort()
    return a[1]

#flr = math.floor
#ceil = math.ceil
@jit(nopython=True,fastmath=True)
def flr(x):
    return math.floor(x)

@jit(nopython=True)
def ceil(x):
    return math.floor(y)

@jit(nopython=True,fastmath=True)
def xround(x) -> int:
    return flr(x+0.5)

#cos = math.cos
@jit(nopython=True,fastmath=True)
def cos(x):
    return math.cos(x)

@jit(nopython=True,fastmath=True)
def sin(x):
    return -1 * math.sin(x)

@jit(nopython=True)
def sgn(x):
    if x>=0:return 1
    return -1

def atan2(dx,dy) -> float:
    vec = pygame.math.Vector2((x,y))
    return vec.to_angle()

@jit(nopython=True,fastmath=True)
def sqrt(x):
    flr(math.sqrt(x))

# abs is apart of python

@jit(nopython=True,fastmath=True)
def rnd(x) -> int:
    return flr(random.random() * x)

@jit(nopython=True,fastmath=True)
def rndrng(x,y) -> int:
    # return flr(rnd(randrange(x,y)))
    return flr(random.randrange(x,y))

@jit(nopython=True)
def srand(x) -> None:
    random.seed(x)
