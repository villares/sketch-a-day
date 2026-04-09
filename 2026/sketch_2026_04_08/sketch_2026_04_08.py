# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

"""
Press " " (space bar) to create many balls
Press "w" to drag the mouse and create a static segment (wall)
Press "b" to drag the mouse and create a box
Press "k" to drag the mouse and create a kinematic box
Press "p" to drag the mouse and create a polygon
Press <delete> or <backspace> to remove objects under the mouse
Press "c" to remove dynamic and kinematic objects
You can drag kinematic objects (and nudge a bit the dynamic ones)
You can use the mouse wheel to rotate some objects
"""

import py5
import shapely
from pymunk_helpers import Simulation, Segment, Ball, Box, Poly

ongoing_creation = None

def setup():
    py5.size(600, 600)
    global sim
    sim = Simulation()
    sim.add_segment(50, 500, 550, 500) # could be just Segment(...)

def draw():
    py5.background(200)
    sim.draw_and_update(step=1/60)  # draw and clean up
    # create many balls
    if py5.is_key_pressed and py5.key == " ":
        d = py5.random(10, 50)
        c = py5.color(d * 5, 0, 255 - d * 5)
        Ball(py5.mouse_x + py5.random(-1, 1), py5.mouse_y, d, c)
    # preview & object creation
    py5.no_fill()
    py5.stroke_weight(2)
    py5.stroke(255)
    x, y = py5.mouse_x, py5.mouse_y
    match ongoing_creation:
        case pts, "p":
            # poly creation ongoing!
            with py5.begin_shape():
                py5.vertices(pts)
                py5.vertex(x, y)
            if (len(pts) == 0) or py5.dist(x, y, *pts[-1]) > 20:
                pts.append((x, y))
        case sx, sy, "w":
            with py5.push_style(), py5.begin_shape():
                py5.line(sx, sy, x, y)
        case sx, sy, "b" | "k":
            py5.rect_mode(py5.CORNERS)
            py5.rect(sx, sy, x, y)

def key_pressed():
    if py5.key in (py5.BACKSPACE, py5.DELETE):
        for obj in sim:
            if obj.under_mouse():
                obj.remove_from_sim()
    elif py5.key == "c":
        for obj in sim:
            if obj.body is not obj.space.static_body:
                obj.remove_from_sim() 

def mouse_pressed():
    global ongoing_creation
    if py5.key == "k" and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, "k")
    elif py5.key == "b" and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, "c")
    elif py5.key == "w" and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, "w")
    elif py5.key == "p" and py5.is_key_pressed:
        ongoing_creation = ([], "p")

def mouse_released():
    global ongoing_creation
    mx, my = py5.mouse_x, py5.mouse_y
    match ongoing_creation:
        case sx, sy, "w":
            Segment(sx, sy, mx, my)
        case sx, sy, box_type:
            w, h = abs(sx - mx), abs(sy - my)
            x, y = (sx + mx) / 2, (sy + my) / 2
            Box(x, y, w, h, kinematic=(box_type == "k"))
        case pts, "p":
            shapely_poly = shapely.Polygon(pts) if len(pts) >= 3 else shapely.Polygon()
            if shapely_poly.area > 100 and shapely_poly.is_simple:
                Poly(shapely_poly, fill_color=py5.color(255))
    ongoing_creation = None

def mouse_dragged():
    if not py5.is_key_pressed:
        for obj in sim:
            if obj.under_mouse():
                obj.translate(py5.mouse_x - py5.pmouse_x, py5.mouse_y - py5.pmouse_y)

def mouse_wheel(e):
    for obj in sim:
        if obj.under_mouse():
            obj.rotate(py5.radians(e.get_count()))

py5.run_sketch(block=False)
