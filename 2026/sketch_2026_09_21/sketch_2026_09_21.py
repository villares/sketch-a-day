import numpy as np
import py5
from py5 import Py5Vector as V

N = 50

def setup():
    global color_ints
    py5.size(500, 500, py5.P3D)
    py5.no_stroke()
    for _ in range(N):
        Boid(250 + py5.random(-100, 100), 250 + py5.random(-100, 100))
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 255)
    Boid.init_flock_arrays()


def draw():
    py5.background('black')
    Boid.flock_update()
    py5.window_title(str(int(py5.get_frame_rate())))


def key_pressed():
    py5.save_frame('####.png')


class Boid:
    vel_maxima = 4
    forca_maxima = 0.3
    alignment_radius = 100
    separation_radius = 50
    cohesion_radius = 50

    flock = []
    flock_positions = None   # (N, 2)
    flock_vels = None        # (N, 2)
    diff = None               # (N, N, 2): diff[i, j] = pos_i - pos_j
    sq_dist = None            # (N, N)

    def __init__(self, x, y):
        self.pos = V(x, y)
        self.vel = V.random(2) * py5.random(1, 3)
        self.acc = V(0, 0)
        self.index = len(self.flock)
        self.flock.append(self)


    @classmethod
    def init_flock_arrays(cls):
        cls.flock_positions = np.array(
            [[b.pos.x, b.pos.y] for b in cls.flock], dtype=float)
        cls.flock_vels = np.array(
            [[b.vel.x, b.vel.y] for b in cls.flock], dtype=float)
         #cls.flock_update()
        cls.color_ints = np.array([py5.color(i) for i in range(255)])
        
    
    @classmethod
    def flock_update(cls):
        diff = (cls.flock_positions[:, np.newaxis, :]
                - cls.flock_positions[np.newaxis, :, :])
        cls.diff = diff
        cls.sq_dist = np.sum(diff ** 2, axis=-1)
        for b in cls.flock:
            b.update()
        positions = cls.flock_positions
        vels = cls.flock_vels
        perp = np.stack([-vels[:, 1], vels[:, 0]], axis=1)
        #norms = np.linalg.norm(perp, axis=1, keepdims=True)
        #norms[norms == 0] = 1  # to avoid division-by-zero
        #perp_unit = perp / norms
        esquerda = positions - vels * 4 + perp
        direita = positions - vels * 4 - perp
        all_vertices = np.stack([positions, esquerda, direita], axis=1).reshape(-1, 2)
        pc = (positions[:, 0] + positions[:, 1]) / 1000 * 255
        colors = cls.color_ints[np.repeat(pc, 3).astype(np.int8)]
        shp = py5.create_shape()
        shp.begin_shape(py5.TRIANGLES)
        shp.no_stroke()
        shp.vertices(all_vertices)
        shp.end_shape()
        shp.set_fills(colors)
        py5.shape(shp)


    def update(self):
        self.acc += self.separation()
        self.acc += self.alignment()
        self.acc += self.cohesion()
        self.vel += self.acc
        self.acc.set_mag(0)
        self.vel.set_limit(self.vel_maxima)
        self.pos += self.vel
        self.pos.x = self.pos.x % py5.width
        self.pos.y = self.pos.y % py5.height

        self.flock_positions[self.index] = (self.pos.x, self.pos.y)
        self.flock_vels[self.index] = (self.vel.x, self.vel.y)


    def cohesion(self):
        steering = V(0, 0)
        dist_row = self.sq_dist[self.index]
        mask = dist_row < self.cohesion_radius ** 2
        mask[self.index] = False  # exclui o próprio
        
        if mask.any():
            centro_massa = self.flock_positions[mask].mean(axis=0)
            direcao_ao_cm = V(*centro_massa) - self.pos
            direcao_ao_cm.set_mag(self.vel_maxima)
            steering = direcao_ao_cm - self.vel
            steering.set_limit(self.forca_maxima)

        return steering


    def alignment(self):
        steering = V(0, 0)
        dist_row = self.sq_dist[self.index]
        mask = dist_row < self.alignment_radius ** 2
        mask[self.index] = False  # exclude self

        if mask.any():
            avg_V = V(*self.flock_vels[mask].mean(axis=0))
            avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel

        return steering
    

    def separation(self):
        steering = V(0, 0)
        dist_sq = self.sq_dist[self.index]
        mask = (dist_sq > 0) & (dist_sq < self.separation_radius ** 2)

        if mask.any():
            distances = np.sqrt(dist_sq[mask])
            diff_vectors = self.diff[self.index][mask] / distances[:, np.newaxis]
            avg_V = V(*diff_vectors.mean(axis=0))
            if avg_V.mag_sq > 0:
                avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel
            steering.set_limit(self.forca_maxima)

        return steering


py5.run_sketch()
