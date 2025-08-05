import py5
import py5_tools 

R = 200
step = 0.001

def setup():
    py5.size(500, 500)
    py5.stroke_weight(2)
    py5.os_noise_seed(1)
    # Export gif
    py5_tools.animated_gif('noise_walk.gif', duration=0.05,
                           frame_numbers=range(1 + 360, 361 + 360, 3))
    py5.background(5)


def draw():
    py5.no_stroke()
    py5.fill(0, py5.random_int(3, 7))
    py5.rect(0,0, py5.width, py5.height)
    py5.translate(py5.width / 2, py5.height / 2)
    f = py5.radians(py5.frame_count)
    wx = py5.cos(f) * R + R
    wy = py5.sin(f) * R + R
    py5.stroke(255)
    for wz in range(50):
        ni = py5.os_noise(wx * step, wy * step, wz * step * 50)
        nj = py5.os_noise(R + wx * step, -R + wy * step, wz * step * 50 )    
        nx = py5.width * ni / 2
        ny = py5.height * nj / 2
        py5.point(nx, ny)
    #print(ni, nj)
    
py5.run_sketch(block=False)
