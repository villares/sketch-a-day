import py5
import numpy as np

s = 0.005
ygrid, xgrid = np.mgrid[5:500:10, 5:500:10]
grid = np.mgrid[5:500:10, 5:500:10].T.reshape(-1, 2)

def setup():
    py5.size(500, 500, py5.P3D)
    py5.noise_seed(0)
    #py5.no_stroke()
    py5.color_mode(py5.HSB)


def draw():
    py5.translate(0, 250)
    py5.rotate_x(py5.QUARTER_PI / 2)
    py5.translate(0, -300)
    py5.background(200)
    d = 128 + 128 * py5.os_noise(xgrid * s,
                                 ygrid * s,
                                 py5.frame_count * s * 2)
    dd = np.dstack((d, d))
    #py5.points(grid + d)
    my_circle(xgrid, ygrid, d / 20, d)
    py5.window_title(str(round(py5.get_frame_rate(), 1)))

@np.vectorize
def my_circle(x, y, d, c):
    py5.stroke(py5.color(c, 255, 128))
    py5.stroke_weight(d)
    py5.point(x, y, d)

py5.run_sketch()
