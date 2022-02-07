# HAGIA DOCS

Welcome to the Hagia Engine Documentation.
Let us proceed, shall we?

Hagia is a 2D Python game engine built on the Pygame Framework, and
heavily inspired by the PICO-8. Perhaps even an attempt at a recreation
of the PICO-8. As such, is bears many similarities, as well as differences
because it is, well, Python after all.

## COMPATIBILITY

Hagia is compatible with anything that can run Python, as well as Pygame.

Current known compatibility are as follows:

Windows
MacOS
Linux
Raspberry Pi

## PERFORMANCE

The Hagia Engine runs quite well.
Hagia's imposed limitations which limit the scope of a game serve to
maintain performance.

To put it plainly: performance should not be an issue.

## GETTING STARTED WITH HAGIA

Here is a general template for any game working with Hagia.

```
import hagia

h = hagia.engine()

class Game(hagia.game):
    def __init__(self):
        super().__init__()

    def _init(self):
        pass

    def _update(self):
        pass

    def _draw(self):
        pass

    @property
    def gfx(self):
        return

    @property
    def sfx(self):
        return

    @property
    def music(self):
        pass

    @property
    def flags(self):
        pass

    @property
    def map(self):
        pass

h.load_game(Game())
```

### Explaining The Template

In order to use Hagia, you must import it.
```
import hagia
```

After this, in order to effectively utilize Hagia, you must create an
instance of the engine.

```
h = hagia.engine()
```

The reason for this being that the engine loads all of your games
data and retains it. In order to access this data for the engine's functions,
there must be an instance of the engine.

Next, there must be a generic class (in this case "Game") which will inherit from `hagia.game`.

```
class Game(hagia.game):
    def __init__(self):
        super().__init__()

    ...
```

A class that inherits from the `hagia.game` class should call it's dunder init method using
`super().__init__()` with certain passed arguments. If you want to see more about
calling this method, see `Inheriting from the 'hagia.game' class`.

Next up, every game should have an `_init`,`_update`, and `_draw` method.
The `_init` method is called once when the game is ran or reset (via the pause menu), and it is called first.
The `_update` method is called 30 times a second by default. This can be changed by having a custom
`config file` for your game (see more about this in `Creating a Custom Config File`).
The `_draw` method is called 30 times a second by default. Like `_update`, this can also be changed
through means mentioned above.

It should be noted that the `_draw` method is called after the `_update` method.

Next, the properties of the game.
That is, the `gfx`, `sfx`, `music`, `flags`, and `map`

```
class Game(hagia.game):
    ...

    @property
    def gfx(self):
        return

    @property
    def sfx(self):
        return

    @property
    def music(self):
        return

    @property
    def flags(self):
        return

    @property
    def map(self):
        return

    ...
```

Meanings:

`gfx` - The graphics for the game. This property should return the path (type '`str`') to the sprite atlas for your game. This file should be a `.bmp` file, and 8-bit. This type of file is outputted from `Hagia's Sprite Editor`.

`sfx` - The sound effects for the game. This property should return a `list` of paths (type '`str`') to the sound effects files for your game. These files are preferably in the `.wav` format.

`music` - The music for the game. This property should return a `list` of paths (type '`str`') to the sound effects files for your game. These files are preferably in the `.ogg` format.

`flags` - The flags for every sprite in your game. This property should return the path (type '`str`') to the file that contains the flag data. This is outputted from `Hagia's Sprite Editor`.

`map` - The map data for your game. This property should return the path (type '`str`') to the file that contains all the map data. This is outputted by `Hagia's Map Editor`.


Finally, loading the game into Hagia.
To do this, Hagia's `load_game` function must be called.
This can be done with the Hagia instance from earlier.

```
h.load_game(Game())
```

Pass in an instance of your game, and Hagia will handle the rest.
_as well as spit out error messages when it is upset_

Note: _Do try not to let your Hagia instance fall out of scope_

## HAGIA REFERENCE

Hagia Engine Specs:

128x128 display
8x8 size tiles
128 tiles with 8 flags each
128 cells wide, 64 cells tall map data
16 Colors

Hagia will always believe that it's display is 128x128 pixels.
It scales things in order to fit the user's display.
So always base your input on the fact that the display is 128x128.
Anything else is considered off screen and will not be visible.

### GRAPHICS

This (graphics) references expects that you have an instance of the Hagia engine.
ex: `h = hagia.engine()`
This is considered the way of using the Hagia engine.
Do keep in mind that anywhere you see `hagia.engine`, simply think of
replacing this with the instance you created. In that example, `h`.

**hagia.engine.flip()**
Updates the display

**hagia.engine.cls()**
Clears the display
Note: Every single game step (every frame), the Hagia engine automatically clears
the screen.

**hagia.engine.fget(n,f)**
`n` = sprite (type `int` between 0,127)
`f` = flag (type `int` between 0,7)
Returns a boolean value (`True` or `False`) of whether the sprite specified has the specified flag or not.

**hagia.engine.fset(n,val,f)**
`n` = sprite (type `int` between 0,127)
`val` = `True` or `False` (type `bool`)
`f` = flag (type `int` between 0,7)
Sets the value of sprite `n`'s flag `f` to `val`

**hagia.engine.print(txt,x,y,fgc,bgc,s)**
`txt` = text (type `str`)
`x` = position x (type `int`)
`y` = position y (type `int`)
`fgc` = foreground color (color of the text) (type `int` between 0,15 or `NoneType`)
`bgc` = background color (color behind the text) (type `int` between 0,15 or `NoneType`)
`s` = size of text (type `int` or `float`)

`fgc` defaults to None
`bgc` defaults to None
`s` defaults to 4

Prints `txt` to the screen at (`x`,`y`) with the foreground color `fgc` and
background color `bgc` with the text being the size `s`

**hagia.engine.camera(x,y)**
`x` = camera offset x (type `int` or `float`)
`y` = camera offset y (type `int` or `float`)

`x` defaults to 0
`y` defaults to 0

Sets the Hagia Engine's camera position to (`x`,`y`)
Just calling `hagia.engine.camera()` without any arguments resets the camera.

**hagia.engine.circ(x,y,r,col,w)**
`x` = position x (type `int` or `float`)
`y` = position y (type `int` or `float`)
`r` = radius (type `int` or `float`)
`col` = color (type `int` between 0,15)
`w` = border width (type `int` or `float`)

`col` defaults to 0
`w` defaults to 1

Draws a circle at (`x`,`y`) with a radius of `r` colored `col` with a border
of width `w`

**hagia.engine.circfill(x,y,r,col)**
`x` = position x (type `int` or `float`)
`y` = position y (type `int` or `float`)
`r` = radius (type `int` or `float`)
`col` = color (type `int` between 0,15)

`col` defaults to 0

Draws a filled circle at (`x`,`y`) with a radius of `r` colored `col`

**hagia.engine.oval(x0,y0,x1,y1,col,w)**
`x0` = starting x position (type `int` or `float`)
`y0` = starting y position (type `int` or `float`)
`x1` = ending x position (type `int` or `float`)
`y1` = ending y position (type `int` or `float`)
`col` = color (type `int` between 0,15)
`w` = border width (type `int` or `float`)

`col` defaults to 0
`w` defaults to 1

Draws an oval from x position `x0` to `x1` and y position `y0` to `y1` colored
`col` with a border width of `w`

**hagia.engine.ovalfill(x0,y0,x1,y1,col)**
`x0` = starting x position (type `int` or `float`)
`y0` = starting y position (type `int` or `float`)
`x1` = ending x position (type `int` or `float`)
`y1` = ending y position (type `int` or `float`)
`col` = color (type `int` between 0,15)

`col` defaults to 0

Draws a filled oval from x postion `x0` to `x1` and y position `y0` to `y1` colored `col`

**hagia.engine.line(x0,y0,x1,y1,col,w)**
`x0` = starting x position (type `int` or `float`)
`y0` = starting y position (type `int` or `float`)
`x1` = ending x position (type `int` or `float`)
`y1` = ending y position (type `int` or `float`)
`col` = color (type `int` between 0,15)
`w` = line width (type `int` or `float`)

`col` defaults to 0
`w` defaults to 1

Draws a line from (`x0`,`y0`) to (`x1`,`y1`) colored `col` with a width of `w`

**hagia.engine.rect(x0,y0,x1,y1,col,w)**
`x0` = starting x position (type `int` or `float`)
`y0` = starting y position (type `int` or `float`)
`x1` = ending x position (type `int` or `float`)
`y1` = ending y position (type `int` or `float`)
`col` = color (type `int` between 0,15)
`w` = line width (type `int` or `float`)

`col` defaults to 0
`w` defaults to 1

Draws a rectangle from (`x0`,`y0`) to (`x1`,`y1`) colored `col` with a width of `w`

**hagia.engine.rectfill(x0,y0,x1,y1,col)**
`x0` = starting x position (type `int` or `float`)
`y0` = starting y position (type `int` or `float`)
`x1` = ending x position (type `int` or `float`)
`y1` = ending y position (type `int` or `float`)
`col` = color (type `int` between 0,15)

`col` defaults to 0

Draws a filled rectangle from (`x0`,`y0`) to (`x1`,`y1`) colored `col`

**hagia.engine.pal(c0,c1,p)**
`c0` = color to be swapped (type `int` between 0,15)
`c1` = color to swap with (type `int` between 0,15)
`p` = palette to effect (type `int` between 0,1)

`p` defaults to 0

if `p` is 0, it effects the draw palette (sprites, drawing shapes, etc)
if `p` is 1, it effects the display palette (the game screen)

Swaps the color at `c0` for `c1`

**hagia.engine.rpal()**
Resets all palettes

**hagia.engine.spr(n,x,y,w,h,flip_x,flip_y)**
`n` = sprite (type `int` between 0,127)
`x` = position x (type `int`)
`y` = position y (type `int`)
`w` = how many pixels of the sprite to draw wide (type `int`)
`h` = how many pixels of the sprite to draw tall (type `int`)
`flip_x` = flip the sprite on its x axis (type `bool`) (`True` or `False`)
`flip_y` = flip the sprite on its y axis (type `bool`) (`True` or `False`)

`w` defaults to 8
`h` defaults to 8
`flip_x` defaults to False
`flip_y` defaults to False

### MATH

**hagia.engine.max(x,y)**
Returns the maximum of `x` and `y`

**hagia.engine.min(x,y)**
Returns the minimum of `x` and `y`

**hagia.engine.flr(x)**
Returns (type `int`) the floored (rounded down) integer of `x`

**hagia.engine.ceil(x)**
Returns (type `int`) the ceiled (rounded up) integer of `x`

**hagia.engine.xround(x)**
General purpose rounding function
Returns (type `int`) the rounded integer of `x`

**hagia.engine.sin(x)**
Returns the sin of `x`
Note: The return value is automatically inverted (multiplied by -1) and floor'd

**hagia.engine.cos(x)**
Returns the cos of `x`
Note: The return value is automatically inverted (multiplied by -1) and floor'd

**hagia.engine.atan2(dx,dy)**
Returns an angle between 0,1 from `dx`,`dy`
Note: The return value is automatically inverted (multipled by -1)

**hagia.engine.sqrt(x)**
Returns the square root of `x`
Note: The return value is floor'd

**hagia.engine.abs(x)**
Returns the absolute value of `x`

**hagia.engine.rnd(x)**
Returns a random integer between 0,`x`

**hagia.engine.srand(x)**
Sets the random seed to `x`

### TIME

`! Sort of experimental !`

**hagia.engine.dt()**
Returns the time since last game step in seconds (delta time [change in time])

### INPUT

The Hagia Engine has 5 buttons of interest:

0 - The Up Key
1 - The Down Key
2 - The Left Key
3 - The Right Key
4 - Special Button 0
5 - Special Button 1

To find the default configurations for these, see `Configuration Files`.

**hagia.engine.btn(x)**
`x` = (type `int` between 0,5)

Returns a (type `bool`) whether `x` button is pressed or not

### TABLES

**hagia.engine.add(tbl,val,index)**
`tbl` = table to add `val` to (type `list` or `dict`)
`val` = value to add to `tbl`
`index` = at which index to add `val` to `tbl`

`index` defaults to -1

Adds `val` to `tbl` at index `index`
Note: If `index` is <= -1, it will simply append the value to the `tbl`

**hagia.engine.del(tbl,val)**
`tbl` = table to reference when deleting `val` (type `list`)
`val` = value to remove from `tbl`

Removes the first occurence of `val` in `tbl`

**hagia.engine.deli(tbl,i)**
`tbl` = table to reference when deleting item at index `i` (type `list` or `dict`)
`i` = index of the item to remove (type `int`)

`i` defaults to -1, removing the last item of the `tbl`

Removes item from `tbl` at index `i`

**hagia.engine.count(tbl,val)**
`tbl` = table to reference (type `list` or `dict`)
`val` = value to count

`val` defaults to `None` (type `NoneType`)

Returns the amount of `val` in `tbl`
Note: When `val` is `None`, it simply returns the length of `tbl`

**hagia.engine.all(tbl)**
Returns `tbl`

**hagia.engine.foreach(tbl,func)**
`tbl` = table of items to perform `func` on (type `list` & type `dict`?)
`func` = function that gets performed on each item in `tbl`

Performs `func` for every item in `tbl`

Ex:
```
import hagia

h = hagia.engine()

table = [5,2,7,8]

def example_function(x):
    x*=2

h.foreach(table,example_function)
```

### AUDIO

**hagia.engine.sfx(n,fade_len)**
`n` = sound effect to be played (type `int`, starts from 0)
`fade_len` = time the sfx takes to fade out (type `int`)

`fade_len` defaults to 0

Plays sound effect `n` with a fade out of `fade_len`

Note: If `n` is <= -1, all sound will cease to play

**hagia.engine.music(n,start,fade_len)**
`n` = music to be played (type `int`, starts from 0)
`start` = where in the music to start (type `float`)
`fade_len` = time the sfx takes to fade out (type `int`)

`start` defaults to 0.0
`fade_len` defaults to 0

Plays music `n` starting at `start` with a fadeout of `fade_len`

Note: If `n` is <= -1, all music will cease to play with a fade out of `fade_len`

### MAP

The Hagia Engine's map is 128 cells wide, and 64 cells tall.
Every cell has data that refers to the ID of which sprite is drawn.
The flags of said sprite can be found by using the `fget` functionality.
Needless to say, this is very useful for collision detection.

**hagia.engine.map(cel_x,cel_y,sx,sy,cel_w,cel_h,layer)**
`cel_x` = starting map cell position x to draw from (type `int`)
`cel_y` starting map cell position y to draw from (type `int`)
`sx` = position x on screen to start drawing the map from (type `int`)
`sx` = position y on screen to start drawing the map from (type `int`)
`cel_w` = how many cells wide to draw from `cel_x` (type `int`)
`cel_h` = how many cells tall to draw from `cel_y` (type `int`)
`layer` = (type `int` between 0,7 which defines a flag) draws only sprites with this flag set True

`cel_w` defaults to 128
`cel_y` defaults to 128
`layer` defaults to None

Note: If `layer` is `None`, it will draw every sprite from the cell ranges specified.
If `layer` is a (type `int`) (must be between 0,7), it will draw only sprites with `layer`
flag set True.

**hagia.engine.mget(x,y)**
`x` (type `int`)
`y` type (`int`)

Returns the sprite ID of the tile at map cell `x` and `y`

**hagia.engine.set(x,y,v)**
`x` (type `int`)
`y` (type `int`)
`v` (type `int` between 0,127)

Sets the sprite ID of tile at map cell `x` and `y` to `v`

### STRINGS

**hagia.engine.sub(str,from,to)**
`str` = text (type `str`)
`from` (type `int`)
`to` (type `int`)

`to` defaults to None

Returns the part of the string `str` from `from` to `to`

**hagia.engine.tostr(val,hex)**
`val` = value to convert to a string (type `int` or `float` or `hex`)
`hex` = whether `val` is a hexadecimal or not (type `bool` - `True` or `False`)

`hex` defaults to False

Returns a string of `val`
Note: If `val` is a hexadecimal value, make sure that `hex` is True

**hagia.engine.tonum(str)**
`str` = string to be converted to a number (type `str`)

Returns a (type `int` or `float`) of `str`

## Inheriting from the 'hagia.game' Class

Inheriting from the `hagia.game` class will give your game some properties.

There are three:

- Name
- Config File Name/Path
- Custom Font/Path

To take advantage of these properties, in the class of your game, define an `__init__` method.
Inside of this method, call `hagia.game`'s `__init__` method with these properties as
the arguments. Any arguments not supplied will stay as their defaults.

Defaults being:

- Name = `Untitled Hagia Game`
- Config File Name/Path = `config.ini`
- Custom Font = (the default engine font)

Here is an example of doing this:

```
import hagia

class Lucky(hagia.game):
    def __init__(self):
        super().__init__('Lucky','lucky.ini','Data/lucky.ttf')
```

This sets the game's title as `Lucky`, the config file and path to `lucky.ini` and the font and path to the font as `Data/lucky.ttf`

These changes are reflected in the fact that the name of the window will be `Lucky`, it will take configuration from the `lucky.ini` file, and it will use the font supplied.

For more on `configuration files` and using `custom fonts`, read more.

## Configuration Files

A configuration file is where Hagia gets some default settings from.

Here is what a default configuration file looks like:

```
[DEFAULT]
up = 1073741906
down = 1073741905
left = 1073741904
right = 1073741903
button_0 = 122
button_1 = 120
esc = 27
fullscreen = 0
framerate = 30
```

Explanation:

By default, the...

`up` key is set to the up arrow key on a keyboard
`down` key is set to the down arrow key on a keyboard
`left` key is set to the left arrow key on a keyboard
`right` key is set to the right arrow key on a keyboard
`button_0` is set to the Z key on a keyboard
`button_1` is set to the X key on a keyboard
`esc` is set to the ESCAPE key on a keyboard
`fullscreen` is set to 0, which makes it false
`framerate` is set to 30

To learn how to create a custom configuration file, I, the writer of this documentation,
have decided it would best be explained by a video.

When the video is posted, I will have a link to it here.

`! Currently, setting fullscreen to anything but 0 is considered experimental !`

## Custom Fonts

Custom fonts should be in the TrueType format (`*.ttf`).
Read the `Inheriting from the hagia.game Class` to find out how to load in your own custom font!

## Appendix

Hagia has a pause menu. By default this can be accessed by pressing the ESCAPE key.

To navigate the pause menu, by default use the arrow keys UP and DOWN.
By default, menu items can be selected by pressing the (button 0) Z key.

### Hagia's Sprite Editor

... CONTROLS ...

LEFT ARROW KEY - goes to the previous sprite or flag depending on the menu
RIGHT ARROW KEY - goes to the next sprite or flag depending on the menu
UP ARROW KEY - goes to the previous color
DOWN ARROW KEY - goes to the next color

LEFT MOUSE BUTTON - fills a color in based on the selected color
                    when pressed inside the viewport

E KEY - exports all the sprites into an atlas,
        along with the flags data
        into 2 files called 'gfx.bmp' and
        'flags.data' when in the normal menu

F KEY - opens/closes the flags editing menu

C KEY - flips the switch of the currently selected flag
        when the flag menu is open

S KEY - Save the current project

I KEY - Import from a saved project

There will be a video on this. Coming soon...

### Hagia's Map Editor

... CONTROLS ...

UP ARROW KEY - Pan up on the map
DOWN ARROW KEY - Pan down on the map
LEFT ARROW KEY - Pan to the left on the map
RIGHT ARROW KEY - Pan to the right on the map

LEFT CLICK - Place sprite on map / Select sprite from selection panel

RIGHT CLICK - Remove tile from the map

I - Import sprite atlas from sprite editor (`*.gfx` file exported)

Notes: Automatically loads a `map.data` file if detected in current working directory.
This allows to keep the progress of making the map. This will be changed to a project file
soon enough.

There will be a video on this. Coming soon...
