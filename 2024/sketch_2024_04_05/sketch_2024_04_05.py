import py5
import numpy as np

s = 0.005
ygrid, xgrid = np.mgrid[15:780:10, 15:780:10]

def setup():
    py5.size(800, 800)
    py5.noise_seed(0)
    py5.no_stroke()
    py5.fill(255, 100)


def draw():
    py5.background(0)
    d = 12 + 12 * py5.os_noise(xgrid * s,
                                 ygrid * s,
                                 py5.frame_count * s * 2)
    my_circle(xgrid, ygrid, d)
    py5.window_title(str(round(py5.get_frame_rate(), 1)))

@np.vectorize
def my_circle(x, y, d):
    py5.circle(x + d, y + d, d * py5.sqrt(abs(x - y)/ 100))

def key_pressed():
    py5.save('out.png')

py5.run_sketch()