from hagia.defs import (
    HAGIA_LOCAL_VARS
)

from hagia.errata import (
    HAGIA_ASSERT
)

from functools import cached_property
from .graphicSYS import Color

class Cart(object):
    def __init__(
        self,
        cart_name:str = HAGIA_LOCAL_VARS.DEFAULT_CART_NAME.value,
        cart_config_file:str = HAGIA_LOCAL_VARS.DEFAULT_CONFIG_Value.value,
        cart_font:str = HAGIA_LOCAL_VARS.DEFAULT_FONT.value,
        data_directory:str = HAGIA_LOCAL_VARS.DEFAULT_DATA_DIRECTORY.value,
        cart_icon_img:str = None
    ):
        """HAGIA_ASSERT(cart_name is str,"Error: Cart name must be of type `str`")
        HAGIA_ASSERT(
            cart_config_file is str or
            cart_config_file is None,
            "Error: Config file must either be of type `str` or `None`"
        )
        HAGIA_ASSERT(
            cart_font is str,
            "Error: Cart font must be of type `str`"
        )
        HAGIA_ASSERT(
            data_directory is str,
            "Error: Cart data directory must be of type `str`"
        )"""
        self.c_name:str = str(cart_name)
        self.c_conf_file = cart_config_file
        self.c_font:str = str(cart_font)
        self.c_data_directory:str = str(data_directory)
        self.c_icon_img = cart_icon_img

    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    @property
    def gfx(self):
        return None

    @property
    def sfx(self):
        return []

    @property
    def music(self):
        return []

    @property
    def map(self):
        return None

    @property
    def flags(self):
        return None

    @cached_property
    def palette(self) -> tuple:
        return (
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
        )
