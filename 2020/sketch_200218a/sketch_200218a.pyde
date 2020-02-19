from arcs import *
size(500, 500)
def vertex_on_arc(cx, cy, radius, angle):
    x = cx + radius * cos(angle)
    y = cy + radius * sin(angle)
    vertex(x, y)
beginShape()
b_circle_arc(250, 250, 200,
             -QUARTER_PI, HALF_PI, mode=2)
vertex_on_arc(250, 250, 175,
              HALF_PI-QUARTER_PI + .314 / 2)
b_circle_arc(250, 250, 150,
             HALF_PI-QUARTER_PI, -HALF_PI, mode=2)
vertex_on_arc(250, 250, 175,
              -QUARTER_PI + .314 / 2)
endShape(CLOSE)
