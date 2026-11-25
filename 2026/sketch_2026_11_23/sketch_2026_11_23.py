"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>
"""

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
mirror = True

save_svg = False

def setup():
    py5.size(600, 600)  # drawing size in pixels
    
def draw():
    global final_form, save_svg
    py5.background(255, 255, 240)
    if save_svg:
        py5.begin_record(py5.SVG, '####.svg')
    
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
            if mirror:
                forms.append(scale_shape( # scale used to mirror 
                    rshape,
                    xfact=-1,
                    origin=middle))
    final_form = unary_union(forms) # merged shapes
    # pontes
    gaps = []
    ls = LineString([middle, (py5.width / 2, -py5.height)])        
    gap = Polygon(ls.buffer(W, cap_style=cap_style))
    for i in range(n):   
        angle = i * 360 / n
        rgap = rotate_shape(
                gap,
                angle,
                origin=middle
            )
        gaps.append(rgap)
    final_form -= unary_union(gaps) # merged gaps

    py5.fill(0)
    py5.shape(unary_union(final_form))
    
    if save_svg:
        save_svg = False
        py5.end_record()

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
    global n, save_svg, mirror
    if py5.key == 'c':
        shapes.clear()
    elif py5.key == 'a':
        n = n + 1
    elif py5.key == 'z':
        n = n - 1
    elif py5.key == 'd' and shapes:
        shapes.pop()
    elif py5.key == 'm':
        mirror = not mirror
    elif py5.key == 'p':
        py5.save_frame('####.png')
    elif py5.key == 's':
        save_svg = True
                
py5.run_sketch()

