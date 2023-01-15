"""
Smooth Beziers via @introscopia

Code for py5 (py5coding.org) imported mode
"""
from random import choice

def setup():
   size(880, 600)
   no_loop()
   
def draw():
    background(240)
    translate(80, 100)
    C = 19
    L = 5
    for _ in range(5):
        for _ in range(C):
            N = 5 # Num points
            W = (-20, 20)
            H = (-40, -20, -20, 0, 0, 0, 20, 20, 40)
            pts = [(choice(W), choice(H)) for _ in range(N)]
            V = 5 # range of random variation
            ptsb = [(x + random(-V, V), y + random(-V, V)) for x, y in pts]
            fill(0)
            if random(10) > 1:
                smooth_bezier(pts + ptsb[::-1])
            translate(40, 0)
        translate(-40 * C, 100)
    save_frame('###.png')

def key_pressed():
    redraw()

def smooth_bezier(pts):
    """From @introscopia"""
    pts = [Py5Vector(*p) for p in pts]
    with begin_shape():
        vertex(*pts[0])
        for i in range(1, len(pts)):
            n = i + 1
            if n >= len(pts): n = 0
            p = i-1
            pp = i-2
            c1 = (pts[i] - pts[pp]) * 0.2 + pts[p]
            c2 = (pts[p] - pts[n]) * 0.2 + pts[i]
            bezier_vertex(c1.x, c1.y, c2.x, c2.y, pts[i].x, pts[i].y)
#             ellipse(c1.x, c1.y, 6, 6)
#             ellipse(c2.x, c2.y, 6, 6)
        c1 = (pts[0] - pts[-2]) * 0.2 + pts[-1]
        c2 = (pts[-1] - pts[1]) * 0.2 + pts[0]        
        bezier_vertex(c1.x, c1.y, c2.x, c2.y, pts[0].x, pts[0].y)

