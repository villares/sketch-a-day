import py5
import numpy as np

drag = None
pts = [
    (100, 100),
    (500, 100),
    (500, 500),
    (100, 500),
    (150, 150),
    (450, 150),
    (450, 450),
    (150, 450),    
    ]


def setup():
    py5.size(600, 600)

        
def draw():
    global num_points
    py5.background(200)
    py5.no_stroke()
    py5.fill(255)
    for i, (x, y) in enumerate(pts): 
        py5.circle(x, y, 15 if i < 4 else 10)        
    py5.stroke(200, 0, 0)
    py5.stroke_weight(2)
    
    for (xa, ya), (xb, yb) in zip(
            get_qpts(pts[4:]),
            get_qpts(pts[:4])):
        py5.line(xa, ya, xb, yb)
    
    
def get_qpts(pts):
    new_pts = []
    for i, (x, y) in enumerate(pts):
        px, py = pts[i - 1]
        new_pts.append(((px + x) / 2, (py + y) / 2))
        new_pts.append((x, y))    
    qpts = []
    lnp = len(new_pts)
    for i, p in enumerate(new_pts):
        if i % 2 == 0:
            xa, ya = p
            xb, yb = new_pts[(i + 1) % lnp]
            xc, yc = new_pts[(i + 2) % lnp]
            qpts.extend(quadratic_points(xa, ya, xb, yb, xc, yc,
                                         num_points=50))
    return qpts

def quadratic_points(ax, ay, bx, by, cx, cy, num_points=None, first_point=False):
    if num_points is None:
        num_points = int(py5.dist(ax, ay, bx, by) + py5.dist(bx, by, cx, cy) + py5.dist(ax, ay, cx, cy)) // 10
    if num_points <= 2:
        return [(ax, ay), (cx, cy)] if first_point else [(cx, cy)]
    t = np.arange(0 if first_point else 1, num_points + 1) / num_points
    x = (1 - t) * (1 - t) * ax + 2 * (1 - t) * t * bx + t * t * cx
    y = (1 - t) * (1 - t) * ay + 2 * (1 - t) * t * by + t * t * cy
    return np.column_stack((x, y))
           
def mouse_pressed():
    global drag
    for i, (x, y) in enumerate(pts):
        if py5.dist(py5.mouse_x, py5.mouse_y, x, y) < 10:
            drag = i
            break

def mouse_dragged():
    if drag is not None:
        pts[drag] = (py5.mouse_x, py5.mouse_y)

def mouse_released():
    global drag
    drag = None
    
py5.run_sketch()