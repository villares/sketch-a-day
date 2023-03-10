# based on
# https://scipython.com/blog/two-dimensional-collisions/

import py5
import numpy as np
from itertools import combinations

class Particle:

    def __init__(self, x, y, vx, vy, radius=0.01):
        """Initialize the particle's position, velocity, and radius.

        Any key-value pairs passed in the styles dictionary will be passed
        as arguments to Matplotlib's Circle patch constructor.

        """
        self.r = np.array((x, y))
        self.v = np.array((vx, vy))
        self.radius = radius

    # For convenience, map the components of the particle's position and
    # velocity vector onto the attributes x, y, vx and vy.
    @property
    def x(self):
        return self.r[0]

    @x.setter
    def x(self, value):
        self.r[0] = value

    @property
    def y(self):
        return self.r[1]

    @y.setter
    def y(self, value):
        self.r[1] = value

    @property
    def vx(self):
        return self.v[0]

    @vx.setter
    def vx(self, value):
        self.v[0] = value

    @property
    def vy(self):
        return self.v[1]

    @vy.setter
    def vy(self, value):
        self.v[1] = value

    def overlaps(self, other):
        """Does the circle of this Particle overlap that of other?"""

        return np.hypot(*(self.r - other.r)) < self.radius + other.radius

    def advance(self, dt):
        """Advance the Particle's position forward in time by dt."""

        self.r += self.v * dt

        # Make the Particles bounce off the walls
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx
        if self.x + self.radius > 1:
            self.x = 1-self.radius
            self.vx = -self.vx
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy
        if self.y + self.radius > 1:
            self.y = 1-self.radius
            self.vy = -self.vy


def setup():
    py5.size(600, 600)
    global particles, n
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    #init_particles(n, radius, styles)
    n = 200  # n
    radius = np.random.random(n) * 0.02 + 0.01

    particles = []
    for i, rad in enumerate(radius):
        # Try to find a random initial position for this particle.
        while True:
        # Choose x, y so that the Particle is entirely inside the
        # domain of the simulation.
            x, y = rad + (1 - 2*rad) * np.random.random(2)
            # Choose a random velocity (within some reasonable range of
            # values) for the Particle.
            vr = 0.1 * np.random.random() + 0.05
            vphi = 2*np.pi * np.random.random()
            vx, vy = vr * np.cos(vphi), vr * np.sin(vphi)
            particle = Particle(x, y, vx, vy, rad)
            # Check that the Particle doesn't overlap one that's already
            # been placed.
            for p2 in particles:
                if p2.overlaps(particle):
                    break
            else:
                particles.append(particle)
                break
#         particles.append(particle)
    py5.background(160, 100, 100)


def draw():
#     py5.background(160, 100, 100)
    py5.fill(160, 100, 100, 5)
    py5.rect(0, 0, py5.width, py5.height)
    dt = 0.03
    for i, p in enumerate(particles):
        p.advance(dt)
        py5.fill(p.radius * py5.width * 4, 200, 200, 255)
        py5.circle(p.x * py5.width, p.y * py5.width, py5.width * p.radius * 2)
    handle_collisions()


def handle_collisions():
    """Detect and handle any collisions between the Particles.

    When two Particles collide, they do so elastically: their velocities
    change such that both energy and momentum are conserved.

    """

    def change_velocities(p1, p2):
        """
        Particles p1 and p2 have collided elastically: update their
        velocities.

        """

        m1, m2 = p1.radius**2, p2.radius**2
        M = m1 + m2
        r1, r2 = p1.r, p2.r
        d = np.linalg.norm(r1 - r2)**2
        v1, v2 = p1.v, p2.v
        u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
        p1.v = u1
        p2.v = u2

    # We're going to need a sequence of all of the pairs of particles when
    # we are detecting collisions. combinations generates pairs of indexes
    # into the particles list of Particles on the fly.
    pairs = combinations(range(n), 2)
    for i, j in pairs:
        if particles[i].overlaps(particles[j]):
            change_velocities(particles[i], particles[j])


py5.run_sketch()
