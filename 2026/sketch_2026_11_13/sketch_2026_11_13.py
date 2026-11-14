import py5
from pathlib import Path
from shapely import Polygon, affinity, LineString, unary_union

rotate_shape = affinity.rotate
scale_shape = affinity.scale

shapes = []
starting_point = []
n = 6
W = 5
cap_style = 'square'

def setup():
    py5.size(600, 600)  # drawing size in pixels
    
def draw():
    global final_form
    py5.background(150, 150, 100)  # clear the canvas (red)
    forms = []  # used to merge all shapes
    middle = py5.width / 2, py5.height / 2
    for shp in shapes:  # going through all shapes      
        for i in range(n):   
            angle = i * 360 / n
            rshape = rotate_shape(
                    shp,
                    angle,
                    origin=middle
                )
            forms.append(rshape) # draw  the shape
            forms.append(scale_shape( # scale used to mirror 
                rshape,
                xfact=-1,
                origin=middle))
    final_form = unary_union(forms) # merged shapes
    py5.shape(final_form)
    if starting_point:
        ls = LineString([starting_point[0], (py5.mouse_x, py5.mouse_y)])        
        with py5.push_style():
            py5.no_fill()
            py5.shape(ls.buffer(W, cap_style=cap_style))
     
def mouse_pressed():  # when mouse is pressed
    starting_point.append((py5.mouse_x, py5.mouse_y))
    
def mouse_released():  # when mouse is released
    if starting_point:
        # print([starting_point[0], (mouse_x, mouse_y)])
        ls = LineString([starting_point[0], (py5.mouse_x, py5.mouse_y)])        
        shapes.append(Polygon(ls.buffer(W, cap_style=cap_style)))
    starting_point.clear()
    
def key_pressed():
    global n
    if py5.key == 'c':
        shapes.clear()
    elif py5.key == 'a':
        n = n + 1
    elif py5.key == 'z':
        n = n - 1
    elif py5.key == 's':
        svg = final_form.svg()
        Path('out.svg').write_text('<svg>' + svg + '</svg>')
        
py5.run_sketch()

