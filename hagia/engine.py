from .system import System
from .cart import Cart

from .errata import HAGIA_ASSERT

#from typing import Callable

class Engine(System):
    def __init__(self):
        pass

    def load_cart(self,cartridge:Cart):
        HAGIA_ASSERT(
            hasattr(cartridge,"update"),
            "Cartridge must have `update` function"
        )
        HAGIA_ASSERT(
            hasattr(cartridge,"draw"),
            "Cartridge must have `draw` function"
        )

        HAGIA_ASSERT(
            hasattr(cartridge,"init"),
            "Cartridge must have `init` function"
        )

        # start to initialize the system
        super().__init_system__(cartridge)

        self.main_loop()
