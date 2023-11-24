import py5
import numpy as np

s = 0.005
ygrid, xgrid = np.mgrid[0:500:10, 0:500:10]


def setup():
    py5.size(500, 500, py5.P3D)
    py5.noise_seed(0)
    py5.color_mode(py5.HSB)


def draw():
    py5.background(0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2, py5.height / 2)
    py5.rotate_x(py5.QUARTER_PI)
    py5.translate(-py5.width / 2, -py5.height / 2, 0)
    #z = np.full(50, py5.frame_count * s)
    d = 128 + 128 * py5.os_noise(xgrid * s, ygrid * s, py5.frame_count * s)
    my_box(xgrid, ygrid, -200 + d / 2, 10, 10, d)
    py5.window_title(f'{py5.get_frame_rate():.1f}')


@np.vectorize
def my_box(x, y, z, *args):
    py5.push()
    py5.translate(x, y, z)
    py5.fill(args[-1] % 256, 200, 200)
    py5.box(*args)
    py5.pop()

def key_pressed():
    py5.print_line_profiler_stats()

py5.profile_draw()
py5.run_sketch()

