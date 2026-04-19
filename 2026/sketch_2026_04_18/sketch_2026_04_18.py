# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org
# Experiment inspired by the "Particle Life" strategies
# Presented by John @introscopia at Noite de Processing

import py5
import numpy as np
from scipy.spatial import cKDTree

N = 250  # number of particles
species_n = 5  # number of species
color_step = 256 / species_n
interaction_dist = 100  # interaction distance limit
psq = 3  # "squared" particle size 

particles = []

#np.random.seed(1)
#py5.random_seed(1)
force_rules = np.random.uniform(-3, 3, (species_n, species_n))

def setup():
    py5.size(600, 600)
    py5.no_smooth()
    py5.color_mode(py5.HSB)
    py5.stroke_weight(3)
    py5.stroke_cap(py5.PROJECT)

    particles[:] = (Particle() for _ in range(N))
    print(force_rules)    


def predraw_update():
    global tree, positions
    tree = cKDTree(tuple(p.pos for p in particles))
    positions = tuple([] for _ in range(species_n)) # empty lists for positions
    for particle in particles:
        particle.update()  # will advance simulation and fill the position lists
        
def draw():
    py5.background(20, 255, 20)
    for i in range(species_n):
        py5.stroke(i * color_step, 255, 255)
        py5.points(positions[i])
        
    py5.window_title(f'{py5.get_frame_rate():.1f}')

class Particle:
    #__slots__ = ('pos', 'vel', 'species')
    
    def __init__(self):
        self.pos = np.array([py5.random(py5.width), py5.random(py5.height)])
        self.vel = np.array([py5.random(-1, 1), py5.random(-1, 1)])
        self.species = int(py5.random(species_n))

    def update(self):
        self.pos = (self.pos + self.vel) % np.array((py5.width, py5.height))
        self.vel *= 0.95
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
                    lm = force_rules[self.species][other.species] * m
                    if lm < 0:
                        force *= -1
                        lm = -lm
                    force_mag = lm
                self.vel += force * force_mag
        positions[self.species].append(self.pos)


py5.run_sketch()

