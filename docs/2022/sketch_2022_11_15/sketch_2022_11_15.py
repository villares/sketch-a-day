from random import randint, choice
from pyodide import create_proxy
from math import pi, sin, cos

svgNS = 'http://www.w3.org/2000/svg'

def setup():
    canvas = create_canvas(900, 900)
    add_listener(canvas, 'mousedown', mouse_pressed)
    mouse_pressed() # generate the first one

def create_canvas(w, h):
    global width, height, canvas # global canvas is usefull for drawing elements
    width, height = w, h
    canvas = document.createElementNS(svgNS, 'svg')  # document is pyscript "magic"
    set_attribute(canvas, 'width', f'{w}px')
    set_attribute(canvas, 'height', f'{h}px')
    append_by_id('ContainerBox', canvas)
    return canvas

def add_listener(element, event, func):
    element.addEventListener(event, create_proxy(func))
  
def set_attribute(element, attr, value):
    element.setAttributeNS(None, attr, value)
    
def append_by_id(html_id, element):
    document.getElementById(html_id).append(element)
  
def circle(x, y, d, **kwargs):
    c = document.createElementNS(svgNS, 'circle')
    c.setAttributeNS(None, 'cx', x)
    c.setAttributeNS(None, 'cy', y)
    c.setAttributeNS(None, 'r', d / 2)
    apply_kwargs(c, kwargs)
    add_to_canvas(c)
    return c

def rect(x, y, w, h, **kwargs):
    r = document.createElementNS(svgNS, 'rect')
    r.setAttributeNS(None, 'x', x)
    r.setAttributeNS(None, 'y', y)
    r.setAttributeNS(None, 'width', w)
    r.setAttributeNS(None, 'height', h)
    apply_kwargs(r, kwargs)
    add_to_canvas(r)
    return r

def line(x1, y1, x2, y2, **kwargs):
    li = document.createElementNS(svgNS, 'line')
    li.setAttributeNS(None, 'x1', x1)
    li.setAttributeNS(None, 'y1', y1)
    li.setAttributeNS(None, 'x2', x2)
    li.setAttributeNS(None, 'y2', y2)
    apply_kwargs(li, kwargs)
    add_to_canvas(li)
    return li

def text(x, y, text, size=5, **kwargs):
    t = document.createElementNS(svgNS, 'text')
    t.setAttributeNS(None, 'x', x)
    t.setAttributeNS(None, 'y', y)
    t.style.fill = kwargs.pop('fill', 'black')
    t.style.fontSize = str(size)
    t.style.fontFamily = kwargs.pop('family', 'monospace')
    t.style.textAnchor = kwargs.pop('anchor', 'middle')
    t.innerHTML = text
    apply_kwargs(t, kwargs)
    add_to_canvas(t)
    return t
    
def poly(points, **kwargs):
    pts = ' '.join(f'{x},{y}' for x, y in points)
    p = document.createElementNS(svgNS, 'polygon')
    p.setAttributeNS(None, 'points', pts)
    apply_kwargs(p, kwargs)
    add_to_canvas(p)
    return p

def apply_kwargs(element, kwargs):
    if 'stroke' not in kwargs and element != 'text':
        kwargs['stroke'] = 'black'
    if 'fill' not in kwargs and element not in ('line', 'text'):
        kwargs['fill'] = 'white'
    for kw, value in kwargs.items():
        if kw:
            attr = kw.replace('_', '-')
            set_attribute(element, attr, value)

def add_to_canvas(element):
     canvas.appendChild(element)

def rgb_to_hex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def mouse_pressed(e=None):
    #if e.button == 0:   # left mouse button e.offsetX, e.offsetY
    draw_and_replace_canvas_contents()
 
def draw_and_replace_canvas_contents():
    canvas.innerHTML = ''
    rect(0, 0, width, height, fill='rgb(0, 0, 100)')
    for _ in range(3):
        for x in range(100, width, 100):
            for y in range(100, height, 100):
                r, g, b = randint(128, 255), randint(0, 128), randint(0, 255)
                f = rgb_to_hex(r, g, b)
                m = randint(1, 6)
                if m == 1:
                    star(x, y,
                        randint(5, 30),
                        randint(35, 50),
                        1 + randint(1, 4) * 2,
                        stroke='black',
                        stroke_width=2,
                        fill=f,
                        fill_opacity=0.25,
                        )
                elif 1 < m < 4:
                    rect(x - randint(0, 1) * 50, y - randint(0, 1) * 50,
                             50, 50, fill=f, fill_opacity=0.5, stroke='white')
                elif 4 <= m < 6:
                    rect(x - 50, y - 50, 100, 100, fill_opacity=0.25, stroke='white')
                else:
                    circle(x, y, randint(1, 2) * 25, fill=f, stroke='white', fill_opacity=0.25)

def star(cx, cy, ra, rb, n, **kwargs):
    passo = pi * 2 / n
    pts = []
    for i in range(n):  # enquanto o ângulo for menor que 2 * PI:
        ang = passo * i
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        bx = cx + cos(ang + passo / 2.) * rb
        by = cy + sin(ang + passo / 2.) * rb
        pts.append((ax, ay))
        pts.append((bx, by))
        li = line(ax, ay, bx, by, **kwargs)
        set_attribute(li, 'stroke', 'white')
        set_attribute(li, 'stroke-width', 6)
    poly(pts, **kwargs)    

setup()


