import py5
import py5_tools 
import numpy as np

R = 500
step = 0.001
step2 = 0.0005
OFFY = 500
W = 50
N = 4

def setup():
    py5.size(500, 500)
    py5.os_noise_seed(2)
    # Export gif
    py5_tools.animated_gif('noise_walk.gif', duration=0.1,
                           frame_numbers=range(1, 361, 3))
    py5.background(5)


def draw():
    global nxs
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    pos_xxs, pos_xys, pos_yxs, pos_yys = [], [], [], []
    pos_zs, pos_ws = [], []
    for a in range(1, 361, 10):
        t = py5.radians(a)
        f = py5.radians(py5.frame_count)
        wx = py5.cos(t) * R
        wy = py5.sin(t) * R
        wz = py5.cos(f) * R 
        ww = py5.sin(f) * R 
        for i in range(N):
            pos_xxs.append(wx * step - OFFY)
            pos_xys.append(wy * step - OFFY)
            pos_yxs.append(wx * step + OFFY)
            pos_yys.append(wy * step + OFFY)
            pos_zs.append((i * W + wz) * step2)
            pos_ws.append((i * W + ww) * step2)
    npzs = np.array(pos_zs)
    npws = np.array(pos_ws)
    nxs = py5.os_noise(
        np.array(pos_xxs), np.array(pos_xys), npzs, npws
        ) * py5.width * 0.60
    nys = py5.os_noise(
        np.array(pos_yxs), np.array(pos_yys), npzs, npws
        ) * py5.height * 0.60
#     nzs = py5.os_noise(
#         np.array(pos_yxs), np.array(pos_yys), npzs, npws
#         ) * py5.height * 0.60
    py5.stroke(255)
    py5.stroke_weight(1)
    py5.lines(np.column_stack((nxs, nys, np.roll(nxs, 1), np.roll(nys, 1))))
    py5.stroke_weight(3)
    py5.stroke(255, 0, 0)
    py5.points(np.column_stack((nxs, nys)))
    
py5.run_sketch(block=False)


