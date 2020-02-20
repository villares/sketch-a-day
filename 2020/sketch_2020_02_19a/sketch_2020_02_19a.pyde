from arcs import *

def setup():
    size(500, 500)
    
def draw():
    background(0)
    arc_arrow(250, 250, 150, radians(mouseX), radians(mouseY))


def arc_arrow(x, y, radius, start_ang, sweep_ang, thickness=None):
    """
    Draws an arrow in a circular arc shape
    """
    if thickness is None:
        thickness = radius / 4
    beginShape()
    b_circle_arc(x, y, radius + thickness / 2,
                start_ang, sweep_ang, mode=2)
    vertex_on_arc(x, y, radius,
                start_ang + sweep_ang + .314 / 2)
    b_circle_arc(x, y, radius - thickness / 2,
                start_ang + sweep_ang, -sweep_ang, mode=2)
    vertex_on_arc(x, y, radius,
                start_ang + .314 / 2)
    endShape(CLOSE)
    
def vertex_on_arc(cx, cy, radius, angle):
    x = cx + radius * cos(angle)
    y = cy + radius * sin(angle)
    vertex(x, y)
