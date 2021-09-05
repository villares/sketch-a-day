from __future__ import division
import pickle
import glyphs

ADD, SELECT, EDIT = modes = ("add", "select", "edit")
mode = ADD
current_glyph = None
current_path = None
current_vertex = None

keys_pressed = {}
grid_size = 20

def mouse_pressed(mb):
    global current_glyph, current_path, current_vertex
    mx, my = grid_mouse()
    if current_glyph is None:
        current_glyph = glyphs.Glyph('a')
            
    if mode == ADD:
        if current_glyph and current_path is None:
            current_glyph.paths.append([(mx, my, {})])
            current_path = -1
        elif mb == LEFT and current_path is not None:
            current_glyph.paths[current_path].append((mx, my, {}))
        else:
            current_path = None
    elif mode == SELECT:
        if current_glyph:
            for i, path in enumerate(current_glyph.paths):
                for j (x, y, _) in enumerate(path):
                    if dist(mx * grid_size, my * grid_size,
                            x, y) < grid_size:
                        curent_path = i
                        return
    elif mode == EDIT:
        if current_glyph:
            for i, path in enumerate(current_glyph.paths):
                for j (x, y, _) in enumerate(path):
                    if dist(mx * grid_size, my * grid_size,
                            x, y) < grid_size:
                        current_path = i
                        current_vertex = j
                        return                        
def mouse_dragged(mb):
    mx, my = grid_mouse()

    if current_vertex is not None:
        cps = current_glyph.paths[current_path]
        x, y, d = cps[current_vertex]
        cps[current_vertex] = (mx, my, d)
            
            
            
def mouse_released(mb):
    global current_vertex
    current_vertex = None
                            
                                                              
def grid_mouse():
    gs = grid_size
    mx = round(mouseX / gs)
    my = round(mouseY / gs)
    return mx, my      
            

def draw_grid():
    push()
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            if dist(mouseX, mouseY, x, y) < grid_size / 2:
                stroke(255, 0, 0)
            else:
                stroke(255)
            strokeWeight(2)
            point(x, y)
    pop()
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
    global current_glyph, current_path
    if check_keys(ALT) and kc != ALT:
        glyphs_dict = glyphs.Glyph.glyphs
        if k in glyphs_dict:
            current_glyph = glyphs_dict[k]
        else:
            current_glyph = glyphs.Glyph(k)
        keys_pressed.pop(ALT)
        
    elif k == 's':
        with open("data.pickle", "w") as f:
            pickle.dump(glyphs.Glyph.glyphs, f)
            print('data saved')
    elif k == 'l':
        with open("data.pickle") as f:
            glyphs.Glyph.glyphs = pickle.load(f)
            print('data loaded')
    elif k == 'e':
        cps = current_glyph.paths if current_glyph else None
        if cps:
            cps[:] = [[]]
    elif k == 'm':
        global mode
        mode = modes[modes.index(mode) - 1]

    elif mode == ADD and check_keys(BACKSPACE, DELETE, ANY=True):
        cps = current_glyph.paths if current_glyph else None
        if cps and current_path is None:
                current_path = -1
        if cps is not None and cps[current_path]:
            cps[current_path].pop()
        
