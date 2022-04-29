import sys
_stdout = sys.stdout
sys.stdout = None

from pygame import init, event, quit, time

sys.stdout = _stdout
del _stdout

from .graphicSYS import GraphicSystem
from .soundSYS import SoundSystem
from .inputSYS import InputSystem
from .mapSYS import MapSystem
from .flagSYS import FlagSystem
from .utils import *
from .defs import HAGIA_SPECS


from typing import NoReturn
import asyncio


class System(
    GraphicSystem, SoundSystem, InputSystem,
    FlagSystem,MapSystem
):
    def __init__(self):
        pass
    # booting up the system with the cart
    def __init_system__(self,_cartridge) -> None:

        self._cart = _cartridge
        self.cart = self._cart

        init()
        self.init_flags()
        self.init_map()
        self.init_graphics()
        self.init_sound()
        self.init_input()

        # init time stuff
        self.init_time()
        self.init_camera()

        asyncio.run(self.load_cart_data())

    async def load_cart_data(self) -> None:
        # all of these functions will assume a self.cart exists in them
        # despite them not existing in the class whatsoever
        # which may cause confusion for maintenance, but whatever
        t2 = asyncio.create_task(self.load_sound_data())
        t3 = asyncio.create_task(self.load_map_data())
        t4 = asyncio.create_task(self.load_flag_data())
        t1 = asyncio.create_task(self.load_graphics_data())

        await t1
        await t2
        await t3
        await t4
        del t1
        del t2
        del t3
        del t4

    def main_loop(self) -> None:
        self.cart.init()
        self._main_loop:bool = True
        while self._main_loop:
            self.pump()
            self.reg_evs()
            self.cart.update()
            self.cart.draw()
            self.render()
            #self.cls(0)
            self.check_evs()
            self.tick()
        self.main_loop()

    def reg_evs(self) -> None:
        self.evs = [ev.type for ev in event.get()]
        self.reg_kevs()
        event.clear()

    def check_evs(self) -> None:
        # if WINDOW_X_BUTTON button was pressed
        # or if HAGIA_CONTROLS.EXIT button was pressed
        if (
            0x100 in self.evs or
            self.btn(8)
        ):
            self.SHUTDOWN()

        if (
            self.btn(6)
        ):
            self.RESET()

        if (
            self.btn(7)
        ):
            self.PAUSE()

    def pump(self) -> None:
        event.pump()

    def init_time(self) -> None:
        self.fr = HAGIA_SPECS.FRAMERATE
        self.clock = time.Clock()

    def tick(self) -> None:
        self.clock.tick(self.fr)

    # delta-time
    def dt(self) -> float:
        return self.clock.get_time() / 1000

    def init_camera(self) -> None:
        self._camera = Vec2i(0,0)

    def camera(self,x:int=0,y:int=0) -> None:
        self._camera.set_to( flr(-x), flr( -y) )

    def PAUSE(self) -> None:
        pass

    def RESET(self) -> None:
        self.cart = self._cart
        asyncio.run(self.load_cart_data())
        self._main_loop:bool = False

    def SHUTDOWN(self) -> NoReturn:
        quit()
        sys.exit("Shutting down Hagia...")
