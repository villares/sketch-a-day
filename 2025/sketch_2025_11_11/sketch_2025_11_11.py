# Experiment inspired by the "Particle Life" strategies
# Presented by John @introscopia at Noite de Processing

import py5
import numpy as np
from scipy.spatial import cKDTree

N = 200  # number of particles
especies_n = 5  # number of species
color_step = 256 / especies_n
interaction_dist = 100  # interaction distance limit
psq = 10  # "squared" particle size 

particles = []
force_rules = np.random.uniform(-3, 3, (especies_n, especies_n))

def setup():
    py5.size(800, 800)
    py5.no_smooth()
    py5.color_mode(py5.HSB)
    py5.stroke_weight(5)
    py5.stroke_cap(py5.PROJECT)

    particles[:] = (Particle() for _ in range(N))    
    print(force_rules)
    
    py5.background(32)
    py5.fill(32, 32)

def draw():
    global tree
    py5.no_stroke()
    py5.rect(0, 0, py5.width, py5.height)
    # positions = np.array(tuple(p.pos for p in particles))
    tree = cKDTree(tuple(p.pos for p in particles))
    for p in particles:
        p.update()
        
    py5.window_title(f'{py5.get_frame_rate():.1f}')

class Particle:
    def __init__(self):
        self.pos = np.array([py5.random(py5.width), py5.random(py5.height)])
        self.vel = np.array([py5.random(-1, 1), py5.random(-1, 1)])
        self.especie = int(py5.random(especies_n))

    def update(self):
        self.pos = (self.pos + self.vel) % np.array((py5.width, py5.height))
        self.vel *= 0.95
        self.interact()
        self.display()

    def interact(self):
        for i in tree.query_ball_point(self.pos, r=interaction_dist):
            other = particles[i]
            force = self.pos - other.pos
            dsq = np.sum(force ** 2)
            if dsq < interaction_dist ** 2:
                if dsq < psq:
                    m = py5.remap(dsq, psq, 0, 0, 1)
                    if m < 0:
                        force *= -1
                        m = -m
                    force_mag = m
                else:
                    m = py5.remap(dsq, interaction_dist ** 2, 0, 0, 0.001)
                    lm = force_rules[self.especie][other.especie] * m
                    if lm < 0:
                        force *= -1
                        lm = -lm
                    force_mag = lm
                self.vel += force * force_mag
                
    def display(self):
        py5.stroke(self.especie * color_step, 255, 255)
        py5.point(*self.pos)

py5.run_sketch()
