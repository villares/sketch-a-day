from __future__ import division
import pickle
import glyphs

ADD, SELECT, EDIT = ("add", "select", "edit")
mode = ADD
current_glyph = None
keys_pressed = {}
grid_size = 20

def mouse_pressed(mb):
    global current_glyph
    mx, my = grid_mouse()

    if current_glyph is None:
        current_glyph = glyphs.Glyph('a')
            
    if mode == ADD:
        cp = current_glyph.current_path
        if cp is None:
            current_glyph.paths.append([(mx, my, {})])
            current_glyph.current_path = -1
        elif mb == LEFT:
            current_glyph.paths[cp].append((mx, my, {}))
        else:
            current_glyph.current_path = None
    
def mouse_dragged(mb):
    pass

def mouse_released(mb):
    pass
                            
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
    global current_glyph
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
                                                                    
                                                                                                                                                                                                  
    # print(keys_pressed)
    elif mode == ADD and check_keys(CONTROL, '\x05'): # ctrl + e
        cps = current_glyph.paths if current_glyph else None
        if cps:
            cps[:] = [[]]

    elif mode == ADD and check_keys(BACKSPACE, DELETE, ANY=True):
        cps = current_glyph.paths if current_glyph else None
        cp =  current_glyph.current_path if cps else None 
        if cp is not None and cps[cp]:
            cps[cp].pop()
        
