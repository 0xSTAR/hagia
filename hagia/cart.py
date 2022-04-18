from hagia.defs import (
    HAGIA_LOCAL_VARS
)

from hagia.errata import (
    HAGIA_ASSERT
)

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
