# PY5 IMPORTED MODE CODE

import pickle
from glyphs import Glyph

ADD_MODE, MOVE_MODE, EDIT_MODE = modes = ("add", "move", "edit")
mode = ADD_MODE
current_glyph = None  # None or Glyph object
current_path = None   # None or index to path
current_vertex = None # index to vertex in path for EDIT_MODE or (px, py) for MOVE_MODE

keys_pressed = {}
grid_size = 20
OX, OY = 3, 10

# [ ] Arrows to circulate between glyphs
#    [ ] key to remove glyph
# [ ] Store coordinates around OX, OY
# [ ] Use glyphs in a free sample text


def mouse_pressed(mb):
    global current_glyph, current_path, current_vertex
    mx, my = grid_mouse()
    if current_glyph is None:
        current_glyph = Glyph('a')
            
    if mode == ADD_MODE:
        if current_glyph and current_path is None:
            current_glyph.paths.append([(mx, my, {})])
            current_path = -1
        elif mb == LEFT and current_path is not None:
            current_glyph.paths[current_path].append((mx, my, {}))
        else:
            current_path = None
    elif mode == MOVE_MODE:
        if current_glyph:
            for i, path in enumerate(current_glyph.paths):
                for j, (x, y, _) in enumerate(path):
                    if (mx, my) == (x, y):
                        current_path = i
                        current_vertex = (mx, my)
                        print(i, current_vertex)
                        return
    elif mode == EDIT_MODE:
        if current_glyph:
            for i, path in enumerate(current_glyph.paths):
                for j, (x, y, _) in enumerate(path):
                    if (mx, my) == (x, y):
                        current_path = i
                        current_vertex = j
                        return                        

def mouse_dragged(mb):
    global current_vertex
    mx, my = grid_mouse()
    if mode == EDIT_MODE and current_vertex is not None:
        cps = current_glyph.paths[current_path]
        x, y, d = cps[current_vertex]
        cps[current_vertex] = (mx, my, d)
    elif mode == MOVE_MODE and current_path is not None and current_vertex:
        cps = current_glyph.paths[current_path]
        px, py = current_vertex # position where mouse was pressed
        dx, dy = mx - px, my - py
        current_vertex = mx, my
        for i, (x, y, d) in enumerate(cps):
            cps[i] =  (x + dx, y + dy, d)
                
def mouse_released(mb):
    global current_vertex
    current_path = None                        
                                                              
def grid_mouse():
    gs = grid_size
    mx = round(mouse_x / gs) - OX
    my = round(mouse_y / gs) - OY
    return mx, my      
            

def draw_grid(cg):
    push_style()
    stroke(150)
    for oy in (OY - 9, OY - 6, OY, OY + 3):
        line(0, oy * grid_size, width, oy* grid_size)
    line(OX * grid_size, 0, OX * grid_size, height)
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            if dist(mouse_x, mouse_y, x, y) < grid_size / 2:
                stroke(255, 0, 0)
            else:
                stroke(255)
            stroke_weight(2)
            point(x, y)
    if cg:
        stroke(255, 0, 0)
        stroke_weight(3)
        point((OX + cg.width) * grid_size, OY * grid_size)
    pop_style()
    circle(OX * grid_size, OY * grid_size, 5)
    # print(check_keys(CONTROL))
 
def show_mode():
    fill(0)
    text_size(20)
    text(mode, width - grid_size * 5, grid_size)
    
             
def check_keys(*args, **kwargs):
    if kwargs.get('ANY'):
        return any(keys_pressed.get(k, False) for k in args)
    else:
        return all(keys_pressed.get(k, False) for k in args)

def set_current_glyph(k):
        global current_glyph, current_path
        glyphs_dict = Glyph.glyphs
        if k in glyphs_dict:
            current_glyph = glyphs_dict[k]
        else:
            current_glyph = Glyph(k)
        current_path = None

def key_released(k, kc):
    global current_path
    if (check_keys(BACKSPACE, DELETE, ANY=True) and 
               check_keys(ALT)):
        cps = current_glyph.paths if current_glyph else None
        if cps:
            cps[:] = [[]]
        current_path = None
    
    elif check_keys(ALT) and kc != ALT:
        set_current_glyph(k)
        keys_pressed.pop(ALT)
    elif k == 'm':
        global mode
        mode = modes[modes.index(mode) - 1]        
    elif k == 'M' and current_glyph:
        pass
        # converting from earlier coord system!
        # glyphs_dict = Glyph.glyphs
        # for g in glyphs_dict.keys():
        #     for path in glyphs_dict[g].paths:
        #         for i, (x, y, d) in enumerate(path):
        #             path[i] = (x - OX, y - OY, d)
            
    elif k == 's':
        Glyph.glyphs.pop(65535, None)
        Glyph.glyphs.pop(chr(27), None)
        with open("glyphs.pickle", "wb") as f:
            pickle.dump(Glyph.glyphs, f)
            print('glyphs saved')
    elif k == 'l':
        with open("glyphs.pickle", 'rb') as f:
            Glyph.glyphs = pickle.load(f)
            print('glyphs loaded')

    elif check_keys(BACKSPACE, DELETE, ANY=True) and current_path:
        cps = current_glyph.paths if current_glyph else None
        if cps and current_path is None:
                current_path = -1
        if cps is not None and cps[current_path]:
            cps[current_path].pop()
    elif u'{}'.format(k) in '123456789' and current_glyph: 
        current_glyph.width = int(k)

        
