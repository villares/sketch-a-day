from enum import Enum

import py5

class Mode(Enum):
    BEZIER = 0
    QUADRATIC = 1
    OPEN_CMR = 2
    CLOSED_CMR = 3

    def is_active(self):
        return self == self.active

    @classmethod
    def switch(cls, mode=None):
        cls.active = mode or cls((cls.active.value + 1) % len(cls))

Mode.switch(Mode(0))

being_dragged = None

draw_line_funcs = {}
draw_curve_funcs = {}
draw_hendle_funcs = {}

pts = [
    (100, 50),   # 0 initial anchor
    (150, 100),  # 1
    (250, 100),  # 2
    (250, 200),  # 3
    (150, 200),  # 4
    (150, 150),  # 5
    (50, 200),   # 6
    ]

s = 2 # scale factor

def setup():
    py5.size(800, 800)
    f = py5.create_font('Inconsolata', 10)
    py5.text_font(f)

def draw():
    py5.scale(s)
    py5.background(100)
    # gray thin lines to control points
    py5.stroke_weight(1)
    py5.stroke(200)
    for i, (x, y) in enumerate(pts):
        if i != 0:
            if Mode.QUADRATIC.is_active() and i % 2 == 0:
                v0x, v0y = pts[i - 2]
                c1x, c1y = pts[i - 1]
                py5.line(v0x, v0y, c1x, c1y)
                py5.line(c1x, c1y, x, y)
            elif Mode.BEZIER.is_active() and i % 3 == 0:
                v0x, v0y = pts[i - 3]
                c1x, c1y = pts[i - 2]
                py5.line(v0x, v0y, c1x, c1y)
                c2x, c2y = pts[i - 1]
                py5.line(c2x, c2y, x, y)
    # the curves, thick and black
    py5.stroke_weight(3)
    py5.stroke(0)
    py5.no_fill()
    if Mode.QUADRATIC.is_active():
        with py5.begin_shape():
            py5.vertex(pts[0][0], pts[0][1])  # primeiro pt (índice 0)
            pairs = zip(pts[1::2], pts[2::2])
            for (px, py), (x, y) in pairs:  
               py5. quadratic_vertex(px, py, x, y)
    elif Mode.BEZIER.is_active():
        with py5.begin_shape():
            py5.vertex(pts[0][0], pts[0][1])  # primeiro pt (índice 0)
            triples = zip(pts[1::3], pts[2::3], pts[3::3])
            for (c1x, c1y), (c2x, c2y), (vx, vy) in triples:
                py5.bezier_vertex(c1x, c1y, c2x, c2y, vx, vy)
    elif Mode.OPEN_CMR.is_active():
        with py5.begin_shape():
            py5.curve_vertex(pts[0][0], pts[0][1])  # primeiro pt (índice 0)
            for x, y in pts:
                py5.curve_vertex( x, y)
            py5.curve_vertex(pts[-1][0], pts[-1][1])  # último ponto
    elif Mode.CLOSED_CMR.is_active():
        with py5.begin_closed_shape():
            py5.curve_vertex(pts[-1][0], pts[-1][1])  # primeiro pt (índice 0)
            for x, y in pts:
                py5.curve_vertex( x, y)
            py5.curve_vertex(pts[0][0], pts[0][1])  # último ponto
            py5.curve_vertex(pts[1][0], pts[1][1])  # último ponto
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
            f"{i}: {'vertex' if not i else 'control' if i % 3 else 'bezier'}",
            Mode.QUADRATIC:
            f"{i}: {'vertex' if not i else 'control' if i % 2 else 'quadratic'}",
            Mode.OPEN_CMR:
            f"{i}: {'curve_vertex 2x' if i == 0 or i == len(pts)-1 else 'curve_vertex'}",
            Mode.CLOSED_CMR:
            f"{i}: {'curve_vertex 2x' if i in (0,1) or i == len(pts)-1 else 'curve_vertex'}",
        }
    py5.text(templates[Mode.active], x + 5, y - 5)
    t = generate_code()
    py5.fill(255)
    py5.text_leading(10)
    py5.text(t, 20, 260)

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
    if py5.key == ' ':
       Mode.switch()
    elif  py5.key == 'p':
        py5.save_frame('####.png')
        print(generate_code())
        
def generate_code():
    (v0x, v0y) = pts[0]
    code = ''
    if Mode.QUADRATIC.is_active():
        code = '# Quadratic Bézier curve\n'
        code += f'with begin_shape():\n'
        code += f'    vertex({pts[0][0]}, {pts[0][1]})  # 0 \n'
        pairs = zip(pts[1::2], pts[2::2], range(1, len(pts), 2))
        for (cx, cy), (vx, vy), i in pairs:
            code += f'    quadratic_vertex({cx}, {cy}, {vx}, {vy})  # {i} {i+1}\n'
    elif Mode.BEZIER.is_active():
        code = '# Cubic Bézier curve\n'
        code += f'with begin_shape():\n'
        code += f'    vertex({pts[0][0]}, {pts[0][1]})  # 0 \n'
        triples = zip(pts[1::3], pts[2::3], pts[3::3], range(1, len(pts), 3))
        for (c1x, c1y), (c2x, c2y), (vx, vy), i in triples:
            code += f'    bezier_vertex({c1x}, {c1y}, {c2x}, {c2y}, {vx}, {vy})   # {i} {i+1} {i+2}\n'
    elif Mode.OPEN_CMR.is_active():
        code = '# Open Catmull-Rom curve\n'
        code += f'with begin_shape():\n'
        code += f'    curve_vertex({pts[0][0]}, {pts[0][1]})  # 0 \n'
        for i, (x, y) in enumerate(pts):
            code += f'    curve_vertex({x}, {y})  # {i}\n'
        code += f'    curve_vertex({pts[-1][0]}, {pts[-1][1]})  # {len(pts)-1}\n'
    elif Mode.CLOSED_CMR.is_active():
        code = '# Closed Catmull-Rom curve\n'
        code += f'with begin_shape():\n'
        code += f'    curve_vertex({pts[-1][0]}, {pts[-1][1]})  # {len(pts)-1}\n'
        for i, (x, y) in enumerate(pts):
            code += f'    curve_vertex({x}, {y})  # {i}\n'
        code += f'    curve_vertex({pts[0][0]}, {pts[0][1]})  # 0 \n'
        code += f'    curve_vertex({pts[1][0]}, {pts[1][1]})  # 1 \n'

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