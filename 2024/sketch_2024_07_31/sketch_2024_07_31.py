from enum import Enum

import py5

class Mode(Enum):
    BEZIER = 0
    QUADRATIC = 1
#     OPEN_CMR = 2
#     CLOSED_CMR = 3

active_mode = Mode(0)
being_dragged = None

draw_line_funcs = {}
draw_curve_funcs = {}
draw_hendle_funcs = {}

pts = [
    (100, 50),   # 0: vertex() initial anchor
    (150, 100),  # 1: ?
    (250, 100),  # 2: ?
    (250, 200),  # 3: ?
    (150, 200),  # 4: ?
    (150, 100),  # 4: ?
    (50, 200),   # 5: ?
#     (50, 150),   # 6: ?
#     (50, 100),   # 6: ?
#     (50, 50),   # 6: ?
    ]

s = 2 # scale factor

def setup():
    py5.size(800, 800)
    f = py5.create_font('Inconsolata', 12)
    py5.text_font(f)

def draw():
    py5.scale(s)
    py5.background(100)
    
    
    # gray thin lines to control points
    py5.stroke_weight(1)
    py5.stroke(200)
    for i, (x, y) in enumerate(pts):
        if i != 0:
            if active_mode == Mode.QUADRATIC and i % 2 == 0:
                v0x, v0y = pts[i - 2]
                c1x, c1y = pts[i - 1]
                py5.line(v0x, v0y, c1x, c1y)
                py5.line(c1x, c1y, x, y)
            if active_mode == Mode.BEZIER and i % 3 == 0:
                v0x, v0y = pts[i - 3]
                c1x, c1y = pts[i - 2]
                py5.line(v0x, v0y, c1x, c1y)
                c2x, c2y = pts[i - 1]
                py5.line(c2x, c2y, x, y)
    # the curves, thick and black
    py5.stroke_weight(3)
    py5.stroke(0)
    py5.no_fill()
    if active_mode == Mode.QUADRATIC:
        with py5.begin_shape():
            x0, y0 = pts[0]
            py5.vertex(x0, y0)  # primeiro pt (índice 0)
            for (px, py), (x, y) in zip(pts[1::2], pts[2::2]):  
               py5. quadratic_vertex(px, py, x, y)
    if active_mode == Mode.BEZIER:
        with py5.begin_shape():
            x0, y0 = pts[0]
            py5.vertex(x0, y0)  # primeiro pt (índice 0)
            for (c1x, c1y), (c2x, c2y), (vx, vy) in zip(pts[1::3],
                                                        pts[2::3],
                                                        pts[3::3] ):
                py5.bezier_vertex(c1x, c1y, c2x, c2y, vx, vy)

    # the handles
    py5.stroke_weight(1)
    for i, pt in enumerate(pts):
        x, y = pt
        if i == being_dragged:
            py5.fill(200, 0, 0)
        elif py5.dist(py5.mouse_x,
                      py5.mouse_y, x, y) < 10:
            py5.fill(255, 255, 0)
        else:
            py5.fill(255)
        py5.circle(x, y, 5)
        templates = {
            Mode.BEZIER:
            f"{'vertex' if not i else 'control' if i % 3 else 'bezier'}",
            Mode.QUADRATIC:
            f"{'vertex' if not i else 'control' if i % 2 else 'quadratic'}",
        }
        py5.text(f'{i}: {templates[active_mode]}', x + 5, y - 5)
        t = generate_code()
        py5.fill(255)
        py5.text(t, 20, 300)

def mouse_pressed():
    global being_dragged
    for i, pt in enumerate(pts):
        x, y = pt
        if py5.dist(py5.mouse_x / s,
                    py5.mouse_y / s, x, y) < 10:
            being_dragged = i
            break 

def mouse_released():
    global being_dragged
    being_dragged = None
    

def key_pressed():
    global active_mode
    if py5.key == ' ':
        active_mode = Mode((active_mode.value + 1) % len(Mode))
    elif  py5.key == 'p':
        py5.save_frame('####.png')
        print(generate_code())
        
def generate_code():
    (v0x, v0y) = pts[0]
    if active_mode == Mode.QUADRATIC:
        code = '# Quadratic Bézier curve\n'
        code += f'with begin_shape():\n    vertex({v0x}, {v0y})\n'
        for (cx, cy), (vx, vy) in zip(pts[1::2],
                                      pts[2::2]):
            code += f'    quadratic_vertex({cx}, {cy}, {vx}, {vy})\n'
    if active_mode == Mode.BEZIER:
        code = '# Cubic Bézier curve\n'
        code += f'with begin_shape():\n    vertex({v0x}, {v0y})\n'
        for (c1x, c1y), (c2x, c2y), (vx, vy) in zip(pts[1::3],
                                                    pts[2::3],
                                                    pts[3::3] ):
            code += f'    bezier_vertex({c1x}, {c1y}, {c2x}, {c2y}, {vx}, {vy})\n'
    return code


def mouse_dragged():
    global pts
    global being_dragged
    if being_dragged is not None:
        x, y = pts[being_dragged]
        x += (py5.mouse_x - py5.pmouse_x) / s
        y += (py5.mouse_y - py5.pmouse_y) / s
        pts[being_dragged] = x, y
        
        
py5.run_sketch(block=False)