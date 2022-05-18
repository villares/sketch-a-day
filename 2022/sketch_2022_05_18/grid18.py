from random import randint, choice
from pyodide import create_proxy
from math import pi, sin, cos

def size(w, h):
    global width, height, canvas, svgNS
    width, height = w, h
    svgNS = 'http://www.w3.org/2000/svg'
    canvas = document.createElementNS(svgNS, 'svg')
    canvas.setAttributeNS(None, 'width', f'{w}px')
    canvas.setAttributeNS(None, 'height', f'{h}px')
    document.getElementById('ContainerBox').append(canvas)
    on_click = create_proxy(mouse_pressed)
    canvas.addEventListener('mousedown', on_click)
    global current_stroke, current_fill, current_opacity
    current_stroke = 'black'
    current_fill = 'white'
    current_opacity =  1


def circle(x, y, d, stroke='current', fill='current'):
    if stroke == 'current':
        stroke = current_stroke
    if fill == 'current':
        fill = current_fill
    c = document.createElementNS(svgNS, 'circle')
    c.setAttributeNS(None, 'cx', x)
    c.setAttributeNS(None, 'cy', y)
    c.setAttributeNS(None, 'r', d / 2)
    if fill is not None:
        c.setAttributeNS(None, 'fill', fill)
    if stroke is not None:
        c.setAttributeNS(None, 'stroke', stroke)
    return c


def rect(x, y, w, h, stroke='current', fill='current'):
    if stroke == 'current':
        stroke = current_stroke
    if fill == 'current':
        fill = current_fill
    r = document.createElementNS(svgNS, 'rect')
    r.setAttributeNS(None, 'x', x)
    r.setAttributeNS(None, 'y', y)
    r.setAttributeNS(None, 'width', w)
    r.setAttributeNS(None, 'height', h)
    if fill is not None:
        r.setAttributeNS(None, 'fill', fill)
    if stroke is not None:
        r.setAttributeNS(None, 'stroke', stroke)
    return r


def text(x, y, text, size=5, fill='black'):
    t = document.createElementNS(svgNS, 'text')
    t.setAttributeNS(None, 'x', x)
    t.setAttributeNS(None, 'y', y)
    t.style.fill = fill
    t.style.fontSize = str(size)
    t.style.fontFamily = 'monospace'
    t.style.textAnchor = 'middle'
    t.innerHTML = text
    return t


def fill(f):
    global current_fill
    current_fill = f

def stroke(s):
    global current_stroke
    current_stroke = s
    
def poly(points, stroke='current', fill='current', opacity='current'):
    if stroke == 'current':
        stroke = current_stroke
    if fill == 'current':
        fill = current_fill
    if opacity == 'current':
        opaciry = current_opacity
    pts = ' '.join(f'{x},{y}' for x, y in points)
    p = document.createElementNS(svgNS, 'polygon')
    p.setAttributeNS(None, 'points', pts)
    if fill is not None:
        p.setAttributeNS(None, 'fill', fill)
    if stroke is not None:
        p.setAttributeNS(None, 'stroke', stroke)
    p.setAttributeNS(None, 'fill-opacity', opacity)
    return p

def add(element):
    canvas.appendChild(element)

def mouse_pressed(e):
    #if e.button == 0:   # left mouse button e.offsetX, e.offsetY
    canvas.innerHTML = ''
    add(rect(0, 0, width, height, fill='black'))
    for _ in range(3):
        for x in range(100, width, 100):
            for y in range(100, height, 100):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                add(star(x, y,
                    randint(5, 30),
                    randint(35, 75),
                    randint(3, 11),
                    fill='#{:02X}{:02X}{:02X}'.format(r, g, b),
                    opacity = 0.5,
                    ))

def star(cx, cy, ra, rb, n, **kwargs):
    passo = pi * 2 / n
    pts = []
    for i in range(n):  # enquanto o ângulo for menor que 2 * PI:
        ang = passo * i
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        pts.append((ax, ay))
        bx = cx + cos(ang + passo / 2.) * rb
        by = cy + sin(ang + passo / 2.) * rb
        pts.append((bx, by))
#         add(circle(ax, ay, 5))
#         add(circle(bx, by, 3))
    return poly(pts, **kwargs)

size(900, 900)
