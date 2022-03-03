# testing arcs.py
# should update https://github.com/villares/villares/blob/main/arcs.py

from arcs import arc_augmented_poly, arc_filleted_poly
from line_geometry import draw_poly


def setup():
    global mh, mv
    size(500, 500)
    mh, mv = width / 2, height / 2
    cursor(CROSS)

def draw():

    background(0, 128, 32)  # it's better to leave the background out!
    pts = [(100, 100), (400, 150),  (400, 400), (mouse_x, mouse_y)]
    fill(255, 100)
    draw_poly(pts)
    arc_augmented_poly(pts)
    arc_filleted_poly(pts, [50] * len(pts))