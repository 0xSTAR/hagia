from enum import (
    IntEnum,
    Enum,
    unique,
    auto
)

@unique
class HAGIA_LOCAL_VARS(Enum):
    DEFAULT_DATA_DIRECTORY = "hagia_data"
    DEFAULT_FONT = "mono_upper.ttf"
    DEFAULT_CART_NAME = "Untitled Hagia Cart"
    DEFAULT_CONFIG_Value = None

@unique
class HAGIA_EVENTS(IntEnum):
    QUIT = 0x100

@unique
class HAGIA_TYPES(Enum):
    true:bool = True
    false:bool = False
    nil = None#:NoneType = None

#@unique
class HAGIA_SPECS(IntEnum):
    SCREEN_W = 128
    SCREEN_H = 128
    BIT_DEPTH = 8

    BASE_SPRITE_SIZE = 8
    BASE_TILE_SIZE = 8
    MAX_SPRITES = 128
    ATLAS_WIDTH = 128
    ATLAS_HEIGHT = 64
    ATLAS_SPR_COLUMNS = 128 // 8
    ATLAS_SPR_ROWS = 64 // 8

    MAX_MAP_DATA = 8192
    MAP_WIDTH = 128
    MAP_HEIGHT = 64

    SOUND_CHANNELS = 8

    FRAMERATE = 30

@unique
class HAGIA_CONTROLS(IntEnum):
    BTN_0 = 1073741906 # up
    BTN_1 = 1073741905 # down
    BTN_2 = 1073741904 # left
    BTN_3 = 1073741903 # right
    BTN_4 = 99         # C
    BTN_5 = 120        # X
    RESET = 8          # BACKSPACE
    PAUSE = 27         # ESCAPE
    EXIT  = 1073742053 # RSHIFT


@unique
class HAGIA_MEMORY(IntEnum):
    SPRITE_MEMORY_START = 0x0000
    SPRITE_MEMORY_END = 0x0000 + (128 * 8)
