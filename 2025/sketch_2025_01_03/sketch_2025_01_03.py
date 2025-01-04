import py5
from py5 import sin, cos, PI

def setup():
    py5.size(800, 800)
    py5.translate(400, 400)
    py5.background(0)
    py5.no_stroke()
    wave(390)
    
def wave(r):
    py5.fill(255 - r / 2)
    with py5.begin_closed_shape():
        py5.vertices(circle_arc_pts(0, 0, r, 0, py5.PI))
    if r > 4:
        with py5.push_matrix():
            py5.translate(-r/2, 0)
            py5.rotate(PI / 3)
            wave(r/2)
            py5.rotate(-PI / 3)
            py5.translate(r, 0)
            wave(r/2)

def circle_arc_pts(x, y, radius, start_ang, sweep_ang, **kwargs):
    return arc_pts(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang, **kwargs)

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24, seg_len=None):
    sweep_angle = end_angle - start_angle
    if abs(sweep_angle) < 0.0001:
        return [(cx + cos(start_angle) * w / 2.0, cy + sin(start_angle) * h / 2.0)]
    if seg_len:
        num_points = abs(sweep_angle * (w + h) / 4) / seg_len
    pts_list = []
    step_angle = float(sweep_angle) / num_points    
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side or abs(va - end_angle) < 0.0001:
        pts_list.append((cx + cos(va) * w / 2.0, cy + sin(va) * h / 2.0))
        va += step_angle
    return pts_list

py5.run_sketch()