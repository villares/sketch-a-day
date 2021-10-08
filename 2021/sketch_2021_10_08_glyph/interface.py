from __future__ import division
import pickle
from glyphs import Glyph

ADD, MOVE, EDIT = modes = ("add", "move", "edit")
mode = ADD
current_glyph = None  # None or Glyph object
current_path = None   # None or index to path
current_vertex = None # index to vertex in path for EDIT or (px, py) for MOVE

keys_pressed = {}
grid_size = 20
OX, OY = 3, 10

phrase = u''
                
def mouse_released(mb):
    global current_vertex
    current_path = None                        
                                                        
            

def draw_grid(cg=None):
    push()
    stroke(150)
    for oy in (OY - 9, OY - 6, OY, OY + 3):
        line(0, oy * grid_size, width, oy* grid_size)
    line(OX * grid_size, 0, OX * grid_size, height)
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            if dist(mouseX, mouseY, x, y) < grid_size / 2:
                stroke(255, 0, 0)
            else:
                stroke(255)
            strokeWeight(2)
            point(x, y)
    if cg:
        stroke(255, 0, 0)
        strokeWeight(3)
        point((OX + cg.width) * grid_size, OY * grid_size)
    pop()
    circle(OX * grid_size, OY * grid_size, 5)
    # print(check_keys(CONTROL))
 
def show_mode():
    fill(0)
    textSize(20)
    text(mode, width - grid_size * 5, grid_size)
    
             
def check_keys(*args, **kwargs):
    if kwargs.get('ANY'):
        return any(keys_pressed.get(k, False) for k in args)
    else:
        return all(keys_pressed.get(k, False) for k in args)


def key_released(k, kc):
    global current_path, phrase
    if check_keys(ALT):
        pass
    elif check_keys(BACKSPACE, DELETE, ANY=True):
        if phrase:
            phrase = phrase[:-1]
    elif u'{}'.format(k) in 'abcdefghijklmnopqrstuvwxyz ':
        phrase += k
    print(phrase)
