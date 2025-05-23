import py5
from itertools import combinations
from functools import cache

N = 80
especies_n = 4
color_step = 256.0 / especies_n
leis = [[0] * especies_n for _ in range(especies_n)]
balls = []

def setup():
    global right, left, top, bottom, pairs
    py5.size(600, 400)  # displayWidth
    py5.no_smooth()

    right = py5.width + 10
    left = -10
    top = -10
    bottom = py5.height + 10
    py5.color_mode(py5.HSB)
    balls[:] = [Ball() for _ in range(N)]

    for j in range(especies_n):
        for i in range(especies_n):
            leis[i][j] = py5.random(-3, 3)
    print(leis)
    
    pairs = tuple((balls[i], balls[j]) for i, j in combinations(range(N), 2))
    
    #py5.launch_repeating_thread(balls_update, name='balls_update', time_delay=0.)

def draw():
    py5.background(0)
    py5.no_stroke()
    balls_update()
#     for ball_i in balls:
#         ball_i.display()
    py5.window_title(f'{py5.get_frame_rate():.1f}')


def balls_update():
    for ball_i, ball_j in pairs:
            forca = ball_i.pos - ball_j.pos
            dsq = forca.mag_sq
            if dsq < 10000:
                if(dsq < 10):
                    m = py5.remap(dsq, 10, 0, 0, 1)
                    if m < 0:
                        forca *= -1
                        m = -m
                    forca.mag = m
                else:
                    m = py5.remap(dsq, 10000, 0, 0, 0.001)
                    lm = leis[ball_i.especie][ball_j.especie] * m
                    if lm < 0:
                        forca *= -1
                        lm = -lm
                    forca.mag = lm
                ball_i.vel += forca
#    for b in balls:
#        b.tick()
#        b.display() # this won't work if balls_updadte in another thread..
    tuple(map(lambda b:b.tick() or b.display(), balls))

class Ball:

    def __init__(self):
        self.pos = py5.Py5Vector(py5.random(py5.width), py5.random(py5.height))
        self.vel = py5.Py5Vector(py5.random(-1, 1), py5.random(-1, 1))
        self.especie = int(py5.random(especies_n))

    def tick(self):
        self.pos += self.vel
        self.vel *= 0.99
        if self.pos.x > right:
            self.pos.x = left
        if self.pos.x < left:
            self.pos.x = right
        if self.pos.y > bottom:
            self.pos.y = top
        if self.pos.y < top:
            self.pos.y = bottom

        # adding display to tick()... breakes id used in separate thread
    def display(self):
        py5.fill(self.especie * color_step, 255, 255)
        py5.ellipse(self.pos.x, self.pos.y, 6, 6)

py5.run_sketch()

