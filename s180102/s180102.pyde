# Many Stars 3D
#(c)2018 Alexandre B A Villares
# https://abav.lugaralgum.com

add_library('peasycam') # Para fazer o orbit!
STAR_LIST, Z_INICIAL, Z_MAX = [], (-4000, -400), 1500

def setup():
    cam = PeasyCam(this, 100)
    size(800, 800, P3D)
    noFill()
    strokeWeight(5)
    for i in range(200):  # duzentas estrelinhas X, Y, r1, r2, número de pontas (sorteados)
        x, y, n = random(-width, width), random(-height, height), int(random(3, 30)) 
        STAR_LIST.append(Star(x, y, random(20, 60), random(50, 120), n))

def draw():
    background(0)
    for star in STAR_LIST:
        star.plot()

class Star():

    def __init__(self, x, y, radius1, radius2, npoints):
        self.x, self.y, self.z = x, y, random(Z_INICIAL[0], Z_INICIAL[1]) # pos Z sorteada
        self.radius1, self.radius2 = radius1, radius2
        self.angle = TWO_PI / npoints # ângulo entre vértices (internos ou externos)
        self.halfAngle = self.angle / 2.0 # meio ângulo
        self.color = color(random(256), random(256), random(256), 120) # cor sorteada

    def plot(self):
        with pushMatrix():
            translate(self.x, self.y, self.z)
            rotate(frameCount / 100.0)  # giro da estrela 
            stroke(self.color)
            beginShape()
            self.radius3 = 5 + self.radius2 * sin(frameCount / 100.0) # raio externo varia
            a, b = 0, self.halfAngle # ângulo do primeire e segundo vértice
            while a < TWO_PI:
                vertex(cos(a) * self.radius3, sin(a) * self.radius3)
                vertex(cos(b) * self.radius1, sin(b) * self.radius1)
                a += self.angle
                b += self.angle
            endShape(CLOSE)
        self.z += 3           # anda com a estrela em Z
        if self.z > Z_MAX:    # quando passa de um certo valor é jogada para trás
            self.z = Z_INICIAL[0] + Z_MAX - Z_INICIAL[1] # evita buracos na distribuição