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
