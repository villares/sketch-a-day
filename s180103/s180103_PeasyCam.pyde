""" Tetrahedrons + PeasyCam"""

add_library('peasycam')

T_LIST, ROT_X, ROT_Y = [], 0, 0
Z_MIN, Z_MAX = -800, 0

def setup():
    cam = PeasyCam(this, 100)
    hint(DISABLE_DEPTH_TEST)
    size(800, 800, P3D)
    for _ in range(100):
        x, y, z = random(0, width), random(0, height), random(Z_MIN, Z_MAX)
        T_LIST.append(Tetrahedron(x, y, z, 75))  # 75 is the size

def draw():
    global ROT_X, ROT_Y
    ROT_X += 0.005
    ROT_Y += 0.01
    background(0)
    strokeWeight(7)
    for tetra in T_LIST:
        # Draws only edges, or only faces if a key is pressed
        tetra.plot(ROT_X, ROT_Y, keyPressed)

class Tetrahedron():

    """ Tetrahedron """

    def __init__(self, x, y, z, radius):
        self.x, self.y, self.z = x, y, z
        self.radius = radius
        self.points = [PVector()] * 4
        # calculate geometry
        a = radius * 2 / 3.
        self.points[0] = PVector(+a, +a, +a)  # vertex 1
        self.points[1] = PVector(-a, -a, +a)  # vertex 2
        self.points[2] = PVector(-a, +a, -a)  # vertex 3
        self.points[3] = PVector(+a, -a, -a)  # vertex 4

    # draws tetrahedron
    def plot(self, rx=0, ry=0, showFaces=False):
        c = color(map(self.x, 0, width, 255, 0),
                  map(self.y, 0, height, 255, 0),
                  map(self.z, Z_MIN, Z_MAX, 0, 255), 100)
        if showFaces:
            noStroke()
            fill(c)
        else:
            noFill()
            stroke(c)
        with pushMatrix():
            translate(self.x, self.y, self.z)
            rotateX(ry)
            rotateY(rx)
            beginShape(TRIANGLE_STRIP)
            p = self.points
            vertex(p[0].x, p[0].y, p[0].z)  # vertex 1
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            vertex(p[2].x, p[2].y, p[2].z)  # vertex 3
            vertex(p[3].x, p[3].y, p[3].z)  # vertex 4
            vertex(p[0].x, p[0].y, p[0].z)  # vertex 1
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            vertex(p[3].x, p[3].y, p[3].z)  # vertex 4
            vertex(p[2].x, p[2].y, p[2].z)  # vertex 3
            vertex(p[1].x, p[1].y, p[1].z)  # vertex 2
            endShape(CLOSE)
