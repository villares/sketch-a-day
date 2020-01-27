"""
Sphere math from David Pena's Esfera example.
(Uniform random distribution on the surface of a sphere)
"""
add_library('VideoExport')

points = []
num_points = 3200
off = rx = 0
noise_scale = 0.001

def setup():
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()
    videoExport.setFrameRate(7)

    global radius
    size(720, 720, P3D)
    radius = int(height * .60)
    colorMode(HSB)
    strokeWeight(3)

    for z in range(-radius, radius, 20):
        for a in range(180):
            points.append(Point(float(z),
                                radians(a * 2)))

def draw():
    global rx, off
    background(0)
    translate(width / 2, height / 2)
    off += 0.02  # walks on noise space!
    rx += 0.02  # simple rotation on Y axis
    rotateY(rx)

    for Point in points:
        Point.plot()

    videoExport.saveFrame()
    if rx >= TWO_PI:
        videoExport.endMovie()
        exit()

class Point():

    def __init__(self, z, phi):
        self.z = z  # random(-radius, radius)
        self.phi = phi  # random(TWO_PI)
        self.theta = asin(self.z / radius)

    def plot(self):
        nx = radius + radius * cos(self.theta) * cos(off + self.phi)
        ny = radius + radius * cos(self.theta) * sin(off + self.phi)
        nz = radius + radius * sin(off + self.theta)
        n = radius * noise(nx * noise_scale,
                           ny * noise_scale,
                           nz * noise_scale)
        x = n * cos(self.theta) * cos(self.phi)
        y = n * cos(self.theta) * sin(self.phi)
        z = n * sin(self.theta)
        mz = modelZ(x, y, z)
        strokeWeight(map(mz, -radius, radius, 0.1, 10))
        stroke(map(n, radius * .2, radius * .8, 0, 255),
               255, 255)
        point(x, y, z)
