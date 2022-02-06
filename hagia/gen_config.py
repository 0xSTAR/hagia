import sys
import os
import configparser

import pygame
from pygame.locals import *

# make sure to make this the name of the config file for the game as well
conf_file_name:str = 'config.ini'
conf_section_name = 'override'

# or if using command line args . . .
for arg in sys.argv:
    if arg.startswith('name='):
        #conf_file_name = arg.split('=')[1] if not arg.split('=')[1].endswith(arg.split('='[1].split('.')[1])) else arg.split
        conf_file_name = arg.lower().split('=')[1].split('.')[0]+'.ini'
        conf_section_name = arg.lower().split('=')[1]+'_control_override'
        #conf_section_name = arg.split('')

# edit these vars
#
#      -- NOTE --
# If you do not wish to change the default 
# value of the key, set it to None.
# Any None values means it will be left
# at the default value as determined
# by the engine.
# --------------------------------------------

# Example:
"""
up:int = None
down:int = None
left:int = None
right:int = None
button_0:int = K_c
button_1:int = K_x
esc:int = None
fullscreen:int = 0
framerate:int = 30
"""

up = None
down = None
left = None
right = None
button_0 = K_c
button_1 = K_x
esc = None
fullscreen = 0
framerate = 30

# --------------------------------------------

def main():
    conf = configparser.ConfigParser(
    defaults={
        'up':str(K_UP),
        'down':str(K_DOWN),
        'left':str(K_LEFT),
        'right':str(K_RIGHT),
        'button_0':str(K_z),
        'button_1':str(K_x),
        'esc':str(K_ESCAPE),
        'fullscreen':str(0),
        'framerate':str(30)
        }
    )

    conf[conf_section_name.upper()] = {}

    new_section = conf[conf_section_name.upper()]

    if not up == None:
        new_section['up'] = str(up)

    if not down == None:
        new_section['down'] = str(down)
    
    if not left == None:
        new_section['left'] = str(left)
    
    if not right == None:
        new_section['right'] = str(right)

    if not button_0 == None:
        new_section['button_0'] = str(button_0)
    
    if button_1 != None:
        new_section['button_1'] = str(button_1)

    if not esc == None:
        new_section['esc'] = str(esc)

    if fullscreen != None:
        new_section['fullscreen'] = str(fullscreen)

    if framerate != None:
        new_section['framerate'] = str(framerate)

    #conf[conf_section_name.upper()] = {
    #    'up':str(up),
    #    'down':str(down),
    #    'left':str(left),
    #    'right':str(right),
    #    'button_0':str(button_0),
    #    'button_1':str(button_1),
    #    'esc':str(esc),
    #    'fullscreen':str(fullscreen),
    #    'framerate':str(framerate)
    #}
    #conf[conf_section_name.lower()]['up'] = str(up)
    #conf[conf_section_name.lower()]['down'] = str(down)
    #conf[conf_section_name.lower()]['left'] = str(left)
    #conf[conf_section_name.lower()]['right'] = str(right)
    #conf[conf_section_name.lower()]['button_0'] = str(button_0)
    #conf[conf_section_name.lower()]['button_1'] = str(button_1)
    #conf[conf_section_name.lower()]['esc'] = str(esc)
    #conf[conf_section_name.lower()]['fullscreen'] = str(fullscreen)
    #conf[conf_section_name.lower()]['framerate'] = str(framerate)

    with open(conf_file_name,'w') as conf_file:
        conf.write(conf_file)

    pygame.quit()

if __name__ == '__main__':
    main()

