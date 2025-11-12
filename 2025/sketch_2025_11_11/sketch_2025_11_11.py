import py5
import numpy as np
from scipy.spatial import cKDTree

N = 200  # number of balls
ESPECIES_N = 5  # number of species
COLOR_STEP = 256 / ESPECIES_N
interaction_dist = 100


balls = []
force_rules = np.random.uniform(-3, 3, (ESPECIES_N, ESPECIES_N))
psq = 10

def setup():
    py5.size(800, 800)
    py5.no_smooth()
    py5.color_mode(py5.HSB)
    py5.stroke_weight(5)
    py5.stroke_cap(py5.PROJECT)

    balls[:] = (Ball() for _ in range(N))    
    print(force_rules)
    
    py5.background(32)
    py5.fill(32, 32)

def draw():
    py5.no_stroke()
    py5.rect(0, 0, py5.width, py5.height)
    positions = np.array([ball.pos for ball in balls])
    tree = cKDTree(positions)
    
    for i, ball in enumerate(balls):
        ball.tick()
        ball.display()
        for nearby_idx in tree.query_ball_point(ball.pos, r=interaction_dist):
            if nearby_idx != i:
                nearby_ball = balls[nearby_idx]
                force = ball.pos - nearby_ball.pos
                dsq = np.sum(force ** 2)
                if dsq < interaction_dist ** 2:
                    if dsq < psq:
                        m = py5.remap(dsq, psq, 0, 0, 1)
                        if m < 0:
                            force *= -1
                            m = -m
                        force_mag = m
                    else:
                        m = py5.remap(dsq, 10000, 0, 0, 0.001)
                        lm = force_rules[ball.especie][nearby_ball.especie] * m
                        if lm < 0:
                            force *= -1
                            lm = -lm
                        force_mag = lm
                    ball.vel += force * force_mag
        
    py5.window_title(f'{py5.get_frame_rate():.1f}')

class Ball:
    def __init__(self):
        self.pos = np.array([py5.random(py5.width), py5.random(py5.height)])
        self.vel = np.array([py5.random(-1, 1), py5.random(-1, 1)])
        self.especie = int(py5.random(ESPECIES_N))

    def tick(self):
        self.pos = (self.pos + self.vel) % np.array((py5.width, py5.height))
        self.vel *= 0.95

    def display(self):
        py5.stroke(self.especie * COLOR_STEP, 255, 255)
        py5.point(self.pos[0], self.pos[1])


py5.run_sketch()

