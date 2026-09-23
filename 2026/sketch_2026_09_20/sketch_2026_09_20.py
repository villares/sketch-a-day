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
    Boid.init_flock_arrays()

    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 255)
    color_ints = np.array([py5.color(i) for i in range(255)])

def draw():
    py5.background('black')

    Boid.flock_update()
    positions = Boid.flock_positions
    vels = Boid.flock_vels
    perp = np.stack([-vels[:, 1], vels[:, 0]], axis=1)
    norms = np.linalg.norm(perp, axis=1, keepdims=True)
    norms[norms == 0] = 1  # to avoid division-by-zero
    perp_unit = perp / norms
    esquerda = positions - vels * 4 + perp_unit * 4
    direita = positions - vels * 4 - perp_unit * 4
    all_vertices = np.stack([positions, esquerda, direita], axis=1).reshape(-1, 2)
    pc = positions[:, 0] / 500 * 255
    colors = color_ints[np.repeat(pc, 3).astype(np.int8)]
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.no_stroke()
    shp.vertices(all_vertices)
    shp.end_shape()
    shp.set_fills(colors)
    py5.shape(shp)

    py5.window_title(str(int(py5.get_frame_rate())))


def key_pressed():
    py5.save_frame('####.png')


class Boid:
    vel_maxima = 4
    forca_maxima = 0.2
    bolha_alinha = 100
    bolha_separa = 20
    bolha_coesao = 100

    flock = []
    flock_positions = None   # (N, 2)
    flock_vels = None        # (N, 2)
    diff = None               # (N, N, 2): diff[i, j] = pos_i - pos_j
    sq_dist = None            # (N, N)

    def __init__(self, x, y):
        self.pos = V(x, y)
        self.vel = V.random(2) * py5.random(1, 3)
        self.acc = V(0, 0)
        self.index = len(Boid.flock)
        Boid.flock.append(self)

    @classmethod
    def init_flock_arrays(cls):
        cls.flock_positions = np.array(
            [[b.pos.x, b.pos.y] for b in cls.flock], dtype=float)
        cls.flock_vels = np.array(
            [[b.vel.x, b.vel.y] for b in cls.flock], dtype=float)
        cls.flock_update()

    @classmethod
    def flock_update(cls):
        diff = (cls.flock_positions[:, np.newaxis, :]
                - cls.flock_positions[np.newaxis, :, :])
        cls.diff = diff
        cls.sq_dist = np.sum(diff ** 2, axis=-1)
        for b in cls.flock:
            b.update()
#         cls.flock_headings = np.arctan2(
#             cls.flock_vels[:, 1], cls.flock_vels[:, 0]) % (2 * np.pi)

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

        Boid.flock_positions[self.index] = (self.pos.x, self.pos.y)
        Boid.flock_vels[self.index] = (self.vel.x, self.vel.y)

    def cohesion(self):
        steering = V(0, 0)
        vizinhos = 0
        soma_posicoes = V(0, 0)
        for boid in Boid.flock:
            if self is boid:
                continue
            if Boid.sq_dist[self.index, boid.index] < self.bolha_coesao ** 2:
                soma_posicoes += boid.pos
                vizinhos += 1
        if vizinhos:
            centro_massa = soma_posicoes / vizinhos
            direcao_ao_cm = centro_massa - self.pos
            direcao_ao_cm.set_mag(self.vel_maxima)
            steering = direcao_ao_cm - self.vel
            steering.set_limit(self.forca_maxima)

        return steering

    def alignment(self):
        steering = V(0, 0)
        vizinhos = 0
        avg_V = V(0, 0)
        for boid in Boid.flock:
            if self is boid:
                continue
            if Boid.sq_dist[self.index, boid.index] < self.bolha_alinha ** 2:
                avg_V += boid.vel
                vizinhos += 1
        if vizinhos:
            avg_V /= vizinhos
            avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel

        return steering

    def separation(self):
        steering = V(0, 0)
        vizinhos = 0
        avg_V = V(0, 0)
        for boid in Boid.flock:
            if self is boid:
                continue
            dist_sq = Boid.sq_dist[self.index, boid.index]
            if 0 < dist_sq < self.bolha_separa ** 2:
                distance = np.sqrt(dist_sq)
                dx, dy = Boid.diff[self.index, boid.index]  # self.pos - boid.pos
                avg_V += V(dx, dy) / distance
                vizinhos += 1
        if vizinhos:
            avg_V /= vizinhos
            if avg_V.mag_sq > 0:
                avg_V.set_mag(self.vel_maxima)
            steering = avg_V - self.vel
            steering.set_limit(self.forca_maxima)

        return steering


py5.run_sketch()
