import py5
from py5 import sin, cos, PI

def setup():
    py5.size(800, 800)
    py5.translate(400, 400)
    py5.background(24)
    py5.stroke(0)
    py5.fill(0)
    wave(390)
    py5.save('out.png')
    
def wave(r):
    vs = circle_arc_pts(0, 0, r, 0, py5.PI)        
    vs += reversed(circle_arc_pts(-r/2, 0, r/2, 0, py5.PI))
    vs += reversed(circle_arc_pts(r/2, 0, r/2, 0, py5.PI))
    with py5.begin_shape():
        py5.vertices(vs)
    if r > 20:
        with py5.push_matrix():
            py5.translate(-r/2, 0)
            py5.rotate(py5.PI/3)
            wave(r/2)
            py5.rotate(-py5.PI/3)
            py5.translate(r, 0)
            py5.rotate(py5.PI/2)
            wave(r/2)

def circle_arc_pts(x, y, radius, start, sweep):
    return arc_pts(x, y, radius * 2, radius * 2, start, start + sweep)

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24):
    sweep_angle = end_angle - start_angle
    pts_list = []
    step_angle = float(sweep_angle) / num_points    
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side or abs(va - end_angle) < 0.0001:
        pts_list.append((cx + cos(va) * w / 2.0,
                         cy + sin(va) * h / 2.0))
        va += step_angle
    return pts_list

py5.run_sketch()