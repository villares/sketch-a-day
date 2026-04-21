# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

"""
Press " " (space bar) to create many balls
Press "g" to create a soft grid

Press "w" to drag the mouse and create a static segment (wall)
Press "b" to drag the mouse and create a box
Press "k" to drag the mouse and create a kinematic box
Press "p" to drag the mouse and create a polygon
Press <delete> or <backspace> to remove objects under the mouse
Press "c" to remove dynamic objects
You can drag kinematic objects (and nudge a bit the dynamic ones)
You can use the mouse wheel to rotate some objects
"""

import py5
import shapely
import numpy as np
from pymunk_helpers import Simulation, SimObj, Constraint
from pymunk_helpers import Segment, Ball, Box, Poly
from pymunk_helpers import  PivotJoint, PinJoint, Spring
from villares.shapely_helpers import polys_from_text

ongoing_creation = None

def setup():
    py5.size(600, 600)
    global sim
    sim = Simulation(gravity=(0,900))
    Segment(50, 550, 550, 550, static=True)
    Segment(50, 50, 50, 550, static=True)
    Segment(550, 50, 550, 550, static=True)
    
    
def add_soft_grid(x, y, n, w, d):
    balls = {}
    precursors = ((1, 1), (0, 1), (1, 0))
    for i in range(n):
        for j in range(n):
            ball = balls[i, j] = Ball(x + i * w, y + j * w, d)
            for oi, oj in precursors:
                if  other := balls.get((i - oi, j - oj)):
                    s = Spring(ball, other, thickness=1)

    #p = Spring(star, star.static_body, (450, 300), (300, 10))
    #p.visible = False
    


def mouse_clicked():
    print(py5.mouse_x, py5.mouse_y)
    
def star_points(x, y, radius_a, radius_b, n_points, rot=0):
    if n_points < 3:
        raise TypeError("Number of points sould be at least 3.")
    pts = []
    step = py5.TWO_PI / n_points
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a
        sy = py5.sin(ang) * radius_a
        cx = py5.cos(ang + step / 2.) * radius_b
        cy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            pts.append((x + cx, y + cy))
        else:
            pts.extend(quadratic_points(anchor_x, anchor_y, x + sx, y + sy, x + cx, y + cy))
        anchor_x, anchor_y = x + cx, y + cy
    return pts


def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = 20 #int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(ax, ay, cx, cy)) // 10
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
    y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
    return np.column_stack((x, y))


def draw():
    py5.background(200)
    #print(len(sim.living_set))
    sim.draw_and_update()  # draw and clean up
    sim.step(1/180)
    sim.step(1/180)
    sim.step(1/180)
    # create many balls
    if py5.is_key_pressed and py5.key == " ":
        d = py5.random(5, 25)
        c = py5.color(128, d * 10, 255 - d * 10)
        b = Ball(py5.mouse_x + py5.random(-1, 1), py5.mouse_y, d, c)
        b.friction = 0.01
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
    global sim
    if py5.key in (py5.BACKSPACE, py5.DELETE):
        for obj in sim:
            if obj.under_mouse():
                obj.remove_from_sim()
    elif py5.key == "c":
        for obj in sim:
            if isinstance(obj, Constraint) or obj.body.body_type not in (sim.STATIC, sim.KINEMATIC):
                obj.remove_from_sim() 
    elif py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == 'g':
        add_soft_grid(py5.mouse_x, py5.mouse_y, 5, 25, 20)

def mouse_pressed():
    global ongoing_creation
    if py5.key == "k" and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, "k")
    elif py5.key == "b" and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, "c")
    elif py5.key == "W" and py5.is_key_pressed:
            ongoing_creation = (py5.mouse_x, py5.mouse_y, "W")
    elif py5.key == "w" and py5.is_key_pressed:
            ongoing_creation = (py5.mouse_x, py5.mouse_y, "w")
    elif py5.key == "p" and py5.is_key_pressed:
        ongoing_creation = ([], "p")

def mouse_released():
    global ongoing_creation
    mx, my = py5.mouse_x, py5.mouse_y
    match ongoing_creation:
        case sx, sy, "w":
            sim.add_kinematic_segment(sx, sy, mx, my)
        case sx, sy, "W":
            sim.add_segment(sx, sy, mx, my, radius=20)
        case sx, sy, box_type:
            w, h = abs(sx - mx), abs(sy - my)
            x, y = (sx + mx) / 2, (sy + my) / 2
            Box(x, y, w, h, kinematic=(box_type == "k"))
        case pts, "p":
            shapely_poly = shapely.Polygon(pts) if len(pts) >= 3 else shapely.Polygon()
            if shapely_poly.area > 100 and shapely_poly.is_simple:
                Poly(shapely_poly, fill_color=py5.color(128))
    ongoing_creation = None

def mouse_dragged():
    dx, dy = py5.mouse_x - py5.pmouse_x, py5.mouse_y - py5.pmouse_y
    if not py5.is_key_pressed:
        for obj in sim:
            if obj.under_mouse():
                if obj.type == sim.KINEMATIC:
                    obj.translate(dx, dy)
                if obj.type == sim.DYNAMIC:
                    obj.vel_update(dx, dy)
                    
def mouse_wheel(e):
    for obj in sim:
        if obj.under_mouse() and isinstance(obj, SimObj):
            obj.rotate(py5.radians(e.get_count()))

py5.run_sketch(block=False)
