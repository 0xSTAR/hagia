import sys
import os
from dataclasses import dataclass
import math
import time

from tkinter import Tk
from tkinter.filedialog import askopenfile, asksaveasfilename

from hagia.font import font

import pygame
import pygame.freetype
from pygame.locals import *

DEBUG = False

@dataclass
class pixel:
    num:int = 0

class sprite(object):
    def __init__(self):
        self.pixels = [
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),
            pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel(),pixel()
        ]

        # every sprite has 8 flags
        self.flags = [False, False, False, False, False, False, False, False]

    def draw_viewport(self,screen,colours,x,y,wh,multiplier):
        # draws to the viewport
        """row = 0
        _pixel_index = 0
        for pixel in self.pixels:
            if _pixel_index % 8 == 0:
                row+=1
            pygame.draw.rect(
                screen,
                colours[pixel.num],
                (
                    x+(math.floor(_pixel_index / 8)*multiplier*wh),
                    y+(row*multiplier*wh),
                    wh*multiplier,
                    wh*multiplier
                )
            )
            #pygame.
            _pixel_index+=1"""

        # draws pixels

        _pixel_index = 0
        for row in range(8):
            for pixel in range(8):
                pygame.draw.rect(
                    screen,
                    colours[self.pixels[_pixel_index].num],
                    (
                        x+(pixel*multiplier*wh),
                        y+(row*multiplier*wh),
                        wh*multiplier,
                        wh*multiplier
                    )
                )
                _pixel_index+=1



    def draw_menu(self):
        # draws in the down below area
        pass

class init_error(RuntimeError):
    def __init__(self,error_msg) -> None:
        super().__init__(error_msg)

        self.error_msg = error_msg

    def __repr__(self) -> str:
        return self.error_msg

class editor(object):
    def _init(self):
        self.clicked:bool = False
        self.selected_sprite:int = 1 # 0 can never be selected; selected sprite
        self.selected_colour:int = 0
        self.selected_flag:int = 0
        self.page:int = 1 # sprite page starts at 1

        self.exported:int = 0
        self.flag_set_mode:bool = False

        self.save_file = None

        #self.import_save()

    def main(self) -> None:
        self._init()

        main_loop:bool = True
        while main_loop:
            self.pump()
            self.cls()
            self.register_events()
            self.main_loop_checks()
            self._update()
            self._draw()
            self.flip()
            #self.sleep(0.1)
            self.clear_events()
            self.clock.tick(self.framerate)

    def main_loop_checks(self) -> None:
        #for ev in self.events:
        #    if ev == 0x100: # alias for (int: 256, hex: 0x100)
        #        self.shutdown()
        if 0x100 in self.events:
            self.shutdown()

    def _update(self) -> None:
        # import save file
        if self.btn(7):
            self.import_save()
            self.sleep(0.1)
            return

        # save current save file
        if self.btn(8):
            self.save()
            self.sleep(0.1)
            return

        # save current file as . . .
        if self.btn(8) and self.btn(9):
            self.save_as()
            self.sleep(0.1)
            return

        if self.flag_set_mode:
            if self.btn(5):
                self.flag_set_mode = not self.flag_set_mode
                self.sleep(0.1)
                return

            elif self.btn(0):
                self.selected_flag -= 1 if self.selected_flag > 0 else 0
                self.sleep(0.1)
            elif self.btn(1):
                self.selected_flag += 1 if self.selected_flag < 7 else 0
                self.sleep(0.1)

            if self.mse(0) or self.btn(6):
                self.sprites[self.selected_sprite].flags[self.selected_flag] = not self.sprites[self.selected_sprite].flags[self.selected_flag]
                self.sleep(0.1)
            return

        # check button input
        # and update self.selected_sprite
        if self.btn(0):
            self.selected_sprite -= 1 if self.selected_sprite > 1 else 0
            self.sleep(0.1)
        elif self.btn(1):
            self.selected_sprite += 1 if self.selected_sprite < 127 else 0
            self.sleep(0.1)

        # check button input and update self.selected_colour
        elif self.btn(3):
            self.selected_colour += 1 if self.selected_colour < 15 else 0
            self.sleep(0.1)
        elif self.btn(2):
            self.selected_colour -= 1 if self.selected_colour > 0 else 0
            self.sleep(0.1)

        # check the button input for export button and set self.exported to 120
        elif self.btn(4) and self.exported == 0:
            self.export()
            self.exported = 120
            self.sleep(0.1)

        elif self.btn(5):
            self.flag_set_mode = not self.flag_set_mode
            self.sleep(0.1)

        # update mouse position
        self.m_x, self.m_y = math.floor(pygame.mouse.get_pos()[0] / self.multiplier), math.floor(pygame.mouse.get_pos()[1] / self.multiplier)

        # check if left click is pressed
        if self.mse(0):
            if DEBUG:print(f'x: {self.m_x}')
            if DEBUG:print(f'y: {self.m_y}')

            viewport_startx = 8
            viewport_starty = 8
            s_wh = 8
            viewport_endx = viewport_startx + (s_wh * 8)
            viewport_endy = viewport_starty + (s_wh * 8)

            # check for click in viewport area, if so, set that pixel of the sprite
            # to the selected colour
            if (
                self.m_x >= viewport_startx and
                self.m_x <= viewport_endx and
                self.m_y >= viewport_starty and
                self.m_y <= viewport_endy
            ):
                if DEBUG:print('clicked in the viewport')
                item = math.floor((self.m_x - viewport_startx) / s_wh)
                row = math.floor((self.m_y - viewport_starty) / s_wh)
                if DEBUG:print(f'item: {item} | row: {row}')

                sprite_pixel_index = row*8+item
                if DEBUG:print(f'pixel index: {sprite_pixel_index}')
                try:
                    self.sprites[self.selected_sprite].pixels[sprite_pixel_index].num = self.selected_colour
                except IndexError:
                    pass

            """start_x = 85
            start_y = 90
            radius = 2

            if (
                self.m_x >= start_x - radius and
                self.m_x <= (start_x + radius) + (radius*8*2) and
                self.m_y >= start_y - radius and
                self.m_y <= (start_y + radius) + (radius*2)
            ):
                mx = math.floor(self.m_x) - start_x# - radius)

                print(math.floor(mx / 4))

                #tapped = math.floor(mx / 4) #if mx >= 0 else 0

                #print(tapped)"""






    def _draw(self) -> None:
        self.screen.fill(pygame.Color(97,97,97,a=255))

        if self.flag_set_mode:
            start_x = 12
            start_y = 64
            radius = 3
            border = 1

            self.print('flags',50,32,7)
            self.print(f'selected : {self.selected_flag}',32,85,7)

            for index,flag in enumerate(self.sprites[self.selected_sprite].flags,start=0):
                colour = 1 if flag == False else 12
                pygame.draw.circle(
                    self.screen,
                    self.colours[colour],
                    (
                        start_x*self.multiplier,start_y*self.multiplier
                    ),
                    radius*self.multiplier
                )
                if index==self.selected_flag:
                    pygame.draw.circle(
                        self.screen,
                        self.colours[7],
                        (
                            start_x*self.multiplier,start_y*self.multiplier
                        ),
                        radius*self.multiplier,
                        width=border*self.multiplier
                    )
                start_x += radius*self.multiplier / 2
            return

        # viewport starts at x:32 y:32
        x = 8 * self.multiplier
        y = 8 * self.multiplier
        s_wh = 8 # sprite width and height
        # draw viewport square
        pygame.draw.rect(
            self.screen,
            self.colours[0],
            (x,y,s_wh*self.multiplier*8,s_wh*self.multiplier*8)
        )

        # width and height of sprites
        # width: height:
        self.sprites[self.selected_sprite].draw_viewport(
            self.screen,
            self.colours,
            x,
            y,
            s_wh,
            self.multiplier
        )

        # draws flags
        self.print('flags',93,80,7)
        start_x = 75
        start_y = 90
        radius = 1.4
        for flag in self.sprites[self.selected_sprite].flags:
            colour = 1 if flag == False else 12
            pygame.draw.circle(
                self.screen,
                self.colours[colour],
                (
                    start_x*self.multiplier,start_y*self.multiplier
                ),
                radius*self.multiplier
            )
            start_x += radius*self.multiplier/2
        del(start_x)
        del(start_y)
        del(radius)

        # draw selected sprite number
        self.print('sprite',20,80,7)
        length_of_string = len(str(self.selected_sprite))
        begin_of_string = ''
        while length_of_string < 3:
            begin_of_string+='0'
            length_of_string+=1
        selected_string = begin_of_string+str(self.selected_sprite)
        self.print(selected_string,20,90,7)
        del(length_of_string)
        del(begin_of_string)
        del(selected_string)


        # draw color palette, and square around selected color
        start_x = 85 * self.multiplier
        start_y = 16 * self.multiplier
        wh = 8

        pygame.draw.rect(
            self.screen,
            self.colours[0],
            (
                (start_x-10),
                (start_y-10),
                (wh*self.multiplier*4)+20,
                (wh*self.multiplier*4)+20
            )
        )

        color_index = 0
        row = 0
        for color in self.colours:
            item = color_index % 4

            pygame.draw.rect(
                self.screen,
                color,
                (
                    start_x+(item*self.multiplier*wh),
                    start_y+(row*self.multiplier*wh),
                    wh*self.multiplier,
                    wh*self.multiplier
                )
            )

            color_index+=1
            if color_index % 4 == 0:
                row+=1

        # draw selection box
        item = self.selected_colour % 4
        row = 0 if self.selected_colour < 4 else math.floor(self.selected_colour / 4)
        pygame.draw.rect(
            self.screen,
            self.colours[7],
            (
                start_x+(item*self.multiplier*wh),
                start_y+(row*self.multiplier*wh),
                wh*self.multiplier,
                wh*self.multiplier
            ),
            border_radius=1*self.multiplier,
            width=1*self.multiplier
        )


        # draw export button
        export_startx = 44
        export_starty = 115

        #export_button_text = ' export '
        if self.exported > 0:
            export_button_text='exported'
            self.print(export_button_text,export_startx,export_starty,7,8,size=6)
            self.exported-=1




    def __init__(self):
        # 128 x 64
        # every sprite is 8x8
        # so 16 sprites per row
        # 8 rows
        self.sprites = [
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
            sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),sprite(),
        ]

        self.print_ver_info()

        self.initialize()

    def print_ver_info(self) -> None:
        print('\nSprite Editor 8369 XZ 0.1.0-alpha')
        SDL_ver = pygame.get_sdl_version()
        print(f'SDL ver. {SDL_ver[0]}.{SDL_ver[1]}.{SDL_ver[2]}')
        py_impl:str = str(sys.implementation.name)
        py_cachetag:str = str(sys.implementation.cache_tag)
        py_ver_inf = sys.version_info
        print(py_impl+' '+str(py_ver_inf[0])+'.'+str(py_ver_inf[1])+'.'+str(py_ver_inf[2])+'-'+str(py_ver_inf[3])+' / '+py_cachetag+'\n')

    def get_flag_data_for_save(self) -> str:
        flags = []

        # 0 means False, 1 means True
        flags = []

        #atlas.fill(self.colours[0])
        if DEBUG:print(f'EXPORT:: Atlas bit size: {atlas.get_bitsize()}')

        for sprite_index,sprite in enumerate(self.sprites,start=0):
            for pixel_index,pix in enumerate(sprite.pixels,start=0):
                pass
            # append flags
            flags.append(sprite.flags)

        flag_data:str = ''
        for flgs in flags:
            for f in flgs:
                if f==True:
                    flag_data+=str(1)
                elif f==False:
                    flag_data+=str(0)
                #flag_data+=','
            flag_data+='\n'

        return flag_data

    def save_as(self):
        flag_data = self.get_flag_data_for_save()

        Tk().withdraw()
        save_file = asksaveasfilename(title="Save Project As...")
        #print(save_file)
        #print(save_file)
        if save_file != None:
            try:
                with open(save_file,'w') as save_file2:
                    save_data = ''
                    save_data+='flags\n'
                    save_data+=flag_data
                    save_data+='\nsprite_pixels\n'
                    for spr in self.sprites:
                        for pixl in spr.pixels:
                            save_data+=str(pixl.num)
                            save_data+=','
                        #save_data+=
                        save_data+='\n'
                    save_file2.write(save_data)
                self.save_file = save_file
            except FileNotFoundError:
                self.save_file=None
                del(save_file)

                return
            return
        self.save_file = None

        return

    def save(self):
        # getting flags for the save data file
        flag_data = self.get_flag_data_for_save()
        # now, the save data . . .
        if self.save_file != None:
            with open(self.save_file,'w') as save_file:
                save_data = ''
                save_data+='flags\n'
                save_data+=flag_data
                save_data+='\nsprite_pixels\n'
                for spr in self.sprites:
                    for pixl in spr.pixels:
                        save_data+=str(pixl.num)
                        save_data+=','
                    #save_data+=
                    save_data+='\n'
                save_file.write(save_data)
            return

        self.save_as()
        return



    def import_save(self):
        Tk().withdraw()
        try:
            proj_file = askopenfile(title="Open Project File (*.sep)").name
        except AttributeError:
            return
        #del(atlas_file)
        #self.gfx = atlas0.load(self.scale_factor*2) if not atlas0 == None else []
        #del(atlas0)
        #self.imported = not self.imported

        project_Data = list(filter(None,open(proj_file,'r').read().replace('flags','').replace('sprite_pixels','').split('\n'))) if proj_file != None and proj_file.endswith('.sep') else None
        self.save_file = proj_file if not proj_file==None else None
        if project_Data != None:
            # flags
            for index, flag_nums in enumerate(project_Data,start=0):
                #print(flag_nums)
                flags = []
                for i in range(8):
                    flags.append(True if int(flag_nums[i])==1 else False)
                self.sprites[index].flags = flags
                if index == 127:break

            # pixels
            for i in range(128,256):
                data = list(filter(None,project_Data[i].split(',')))
                for i2 in range(64):
                    self.sprites[i-128].pixels[i2].num = int(data[i2])

    def export(self) -> None:
        atlas = pygame.Surface((128,64),depth=8)
        #just keep it broken, lol. don't fix the palette
        atlas.set_palette(
            [colour for colour in self.colours]
        )

        # 0 means False, 1 means True
        flags = []

        #atlas.fill(self.colours[0])
        if DEBUG:print(f'EXPORT:: Atlas bit size: {atlas.get_bitsize()}')

        for sprite_index,sprite in enumerate(self.sprites,start=0):
            # define the item on which row of the atlas it is currently going to draw
            # to the atlas
            # by referencing the sprite_index variable
            atlas_item = 0 if sprite_index==0 else math.floor(sprite_index % 16)
            atlas_row = math.floor(sprite_index / 16)

            if DEBUG:print(f'EXPORT:: [ atlas item: {atlas_item} || atlas row: {atlas_row} ]')

            sprite_surface = pygame.Surface((8,8),depth=8)
            if DEBUG:print(f'EXPORT:: Sprite bit size: {sprite_surface.get_bitsize()}')

            for pixel_index,pix in enumerate(sprite.pixels,start=0):
                item = 0 if pixel_index==0 else math.floor(pixel_index % 8)
                row = math.floor(pixel_index / 8)

                if DEBUG:print(f'EXPORT:: pixel item: {item} || pixel row: {row}')

                pygame.draw.rect(
                    sprite_surface,
                    self.colours[pix.num],
                    (
                        item,
                        row,
                        1,
                        1
                    )
                )

            atlas.blit(
                sprite_surface,
                (atlas_item*8,atlas_row*8)
            )

            # append flags
            flags.append(sprite.flags)

        # finally, write it to a file
        pygame.image.save(atlas,'gfx.bmp')


        # now, save flags to a file . . .
        flag_data:str = ''
        for flgs in flags:
            for f in flgs:
                if f==True:
                    flag_data+=str(1)
                elif f==False:
                    flag_data+=str(0)
                #flag_data+=','
            flag_data+='\n'
        with open('flags.data','w') as flags_file:
            flags_file.write(flag_data)



    def shutdown(self) -> None:
        pygame.quit()
        sys.exit()

    def initialize(self) -> None:
        try:
            pygame.init()
            pygame.display.init()
            pygame.freetype.init()
        except RuntimeError as e:
            print(repr(init_error(e)))
            self.shutdown()

        self.init_display()
        self.init_colour()
        self.init_font()
        self.init_time()
        self.init_mouse()
        self.configure()

    def init_mouse(self):
        pygame.mouse.set_visible(True)

    def init_font(self) -> None:
        self.font = font().load()

    def configure(self) -> None:
        self.keys = [
            1073741904, # left arrow
            1073741903, # right arrow key
            1073741906, # up arrow key
            1073741905, # down arrow key
            101, # e key
            102, # f key
            99, # c key
            105, # i key
            115, # s key
            1073742049, # LSHIFT
        ]

    def init_display(self) -> None:
        pygame.display.set_caption('Hagia Sprite Editor')

        try:
            if pygame.image.get_extended():
                icon = pygame.image.load('hagia.png')
                pygame.display.set_icon(icon)
        except FileNotFoundError:
            pass # couldn't find hagia image icon :(

        height = pygame.display.Info().current_h
        self.multiplier = math.floor(height/128) - 1
        dimensions = (128 * self.multiplier, 128 * self.multiplier)
        self.screen = pygame.display.set_mode(dimensions)

    def init_colour(self) -> None:
        self.colours = [
            pygame.Color(0,0,0,a=255), # black / 0
            pygame.Color(29,43,83,a=255), # dark blue / 1
            pygame.Color(126,37,83,a=255), # dark purple / 2
            pygame.Color(0,135,81,a=255), # dark green / 3
            pygame.Color(171,82,54,a=255), # brown / 4
            pygame.Color(95,87,79,a=255), # dark-grey / 5
            pygame.Color(194,195,199,a=255), # light-grey / 6
            pygame.Color(255,241,232,a=255), # white / 7
            pygame.Color(255,0,77,a=255), # red / 8
            pygame.Color(255,163,0,a=255), # orange / 9
            pygame.Color(255,236,39,a=255), # yellow / 10
            pygame.Color(0,228,54,a=255), # green / 11
            pygame.Color(41,173,255,a=255), # blue / 12
            pygame.Color(131,118,156,a=255), # lavender / 13
            pygame.Color(255,119,168,a=255), # pink / 14
            pygame.Color(255,204,170,a=255) # light-peach / 15
        ]

    def init_time(self) -> None:
        self.clock = pygame.time.Clock()
        self.framerate:int = 30

    def flip(self) -> None:
        pygame.display.flip()

    def cls(self,x=0) -> None:
        self.screen.fill(self.colours[x])

    def pump(self) -> None:
        pygame.event.pump()

    def register_events(self) -> None:
        self.events = [event.type for event in pygame.event.get()]
        self.key_events = pygame.key.get_pressed()
        self.mouse_events = pygame.mouse.get_pressed(num_buttons=3)

    def clear_events(self) -> None:
        pygame.event.clear()
        del(self.events)
        del(self.key_events)
        del(self.mouse_events)

    def btn(self,x) -> bool:
        if self.key_events[self.keys[x]]:
            return True
        return False

    def mse(self,x) -> bool:
        if self.mouse_events[x]:
            return True
        return False

    def sleep(self,x) -> None:
        time.sleep(x)

    def print(
        self,
        text,
        x,
        y,
        fgcolor=0,
        bgcolor=0,
        #style=pygame.STYLE_DEFAULT,
        #rotation=0,
        size=4
    ):
        self.font.render_to(self.screen,(x*self.multiplier,y*self.multiplier),text,fgcolor=self.colours[fgcolor],bgcolor=self.colours[bgcolor],
            #style=style,
            #rotation=rotation,
            size=size*self.multiplier
        )

if __name__ == '__main__':
    e = editor()
    e.main()
