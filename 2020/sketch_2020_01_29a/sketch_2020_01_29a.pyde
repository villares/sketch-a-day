"""
Noise sphere mais regular
"""
from __future__ import division

add_library('VideoExport')

points = []
num_points = 3200
noise_offset = rotation = 0
noise_scale = 0.001
noiseSeed(1000)

def setup():
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()
    videoExport.setFrameRate(7)

    global radius
    size(720, 720, P3D)
    radius = int(height * .60)
    strokeWeight(3)

    for theta in range(-90, 91, 5):
        r = 96 - abs(theta)
        for a in range(r):
            points.append(Point(radians(theta),
                                radians(360 / r * a)))

def draw():
    global rotation, noise_offset
    background(220, 220, 200)
    translate(width / 2, height / 2)
    # rotation += 0.02  # simple rotation on Y axis
    # rotateY(rotation)
    noise_offset += 0.01  # walks on noise space!

    for Point in points:
        Point.plot(noise_offset, noise_scale)

    videoExport.saveFrame()
    if noise_offset >= TWO_PI:
        videoExport.endMovie()
        exit()

class Point():

    def __init__(self, theta, phi):
        self.theta = theta  # was asin(self.z / radius)
        self.phi = phi

    def plot(self, n_offset, n_scale):
        nx = radius * (1 + cos(self.theta) * cos(n_offset + self.phi))
        ny = radius * (1 + cos(self.theta) * sin(n_offset + self.phi))
        nz = radius * (1 + sin(n_offset + self.theta))
        n = radius * noise(nx * n_scale,
                           ny * n_scale,
                           nz * n_scale)
        z = n * cos(self.theta) * cos(self.phi)
        x = n * cos(self.theta) * sin(self.phi)
        y = n * sin(self.theta)
        mz = modelZ(x, y, z)
        strokeWeight(map(mz, -radius, radius, 0.1, 10))
        stroke(128 - 128 * sin(n / 20.))
        # stroke(map(n, radius * .2, radius * .8, 0, 255) ) #,
               # 255, 255)
        point(x, y, z)
