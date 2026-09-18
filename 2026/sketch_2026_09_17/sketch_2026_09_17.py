
from itertools import chain

import py5
from py5 import Py5Vector as V 

flock = []

def setup():
    py5.size(500, 500)
    py5.no_stroke()
    py5.fill(100)
    for _ in range(30):
        flock.append(Boid(350 + py5.random(-100, 100), 250
                          + py5.random(-100, 100)))

def draw():
    py5.background(200, 200, 255)
    with py5.begin_shape(py5.TRIANGLES):
        py5.vertices(list(chain.from_iterable(b.update() for b in flock)))
    py5.window_title(str(int(py5.get_frame_rate())))

def key_pressed():
    py5.save_frame('####.png')


class Boid:
    vel_maxima = 4
    forca_maxima = 0.2
    bolha_alinha = 100 
    bolha_separa = 20
    bolha_coesao = 100
    
    def __init__(self, x, y):
        self.pos = V(x, y)
        self.vel = V.random(2) * py5.random(1, 3)
        self.acc = V(0, 0)
        
    def update(self):
        
        self.acc += self.separation(flock)
        self.acc += self.alignment(flock)
        self.acc += self.cohesion(flock)

        self.vel += self.acc
        self.acc.set_mag(0)
        
        self.vel.set_limit(self.vel_maxima)
        self.pos += self.vel 
        self.pos.x = self.pos.x % py5.width
        self.pos.y = self.pos.y % py5.height
        
        #ppos = self.pos - self.vel * 3
        #return (self.pos.x, self.pos.y, ppos.x, ppos.y)
        
        perp = V(-self.vel.y, self.vel.x)
        if self.vel.mag_sq > 0:
            perp.normalize()
        esquerda = self.pos - self.vel * 4 + perp * 4
        direita = self.pos - self.vel * 4 - perp * 4
        return (self.pos, esquerda, direita)

    def cohesion(self, boids):
        steering = V(0, 0)
        vizinhos = 0
        soma_posicoes = V(0, 0)
        for boid in boids:
            if (self != boid and
                (boid.pos - self.pos).mag_sq < self.bolha_coesao ** 2):
                soma_posicoes += boid.pos
                vizinhos += 1
        if vizinhos:
            centro_massa = soma_posicoes / vizinhos
            direcao_ao_cm = centro_massa - self.pos
            direcao_ao_cm.set_mag(self.vel_maxima)
            steering = direcao_ao_cm - self.vel
            steering.set_limit(self.forca_maxima)
    
        return steering
    
    def alignment(self, boids):
        steering = V(0, 0)
        vizinhos = 0
        avg_V = V(0, 0)
        for boid in boids:
            dist_sq = (boid.pos - self.pos).mag_sq
            if self != boid and dist_sq < self.bolha_alinha ** 2:
                avg_V += boid.vel
                vizinhos += 1
        if vizinhos:
            avg_V /= vizinhos
            avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel
            
        return steering
        
    def separation(self, boids):
        steering = V(0, 0)
        vizinhos = 0
        avg_V = V(0, 0)
        for boid in boids:
            distance = (boid.pos - self.pos).mag
            if self != boid and distance < self.bolha_separa:
                diff = self.pos - boid.pos
                diff /= distance  # perigoso?
                avg_V += diff
                vizinhos += 1
        if vizinhos:
            avg_V / vizinhos
            if avg_V.mag_sq > 0:
                #avg_V = avg.V.norm * self.vel_maxima
                avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel
            steering.set_limit(self.forca_maxima)
            
        return steering
       
        
py5.run_sketch()    

