# adapted from Khan Academy that adapts Dan Shiffman, natureofcode.com
# https://pt.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-particle-systems/a/particle-systems-with-forces
# now ported to Processing Python mode

def setup():
    global gravity, particleSystem, repeller
    size(400, 400)
    gravity = PVector(0, 0.2)
    particleSystem = ParticleSystem(PVector(width / 2, 50))
    repeller = Repeller(width / 2, 280)


def draw():
    background(214, 255, 171)
    particleSystem.applyGravity()
    particleSystem.applyRepeller(repeller)
    repeller.display()
    particleSystem.addParticle()
    particleSystem.run()
    fill(0)
    text(len(particleSystem.particles), 20, 380)
    # text(frameRate, 20, 390)


class Repeller:

    def __init__(self, x, y):
        self.power = 398.0
        self.position = PVector(x, y)

    def display(self):
        stroke(255)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 32, 32)

    def calculateRepelForce(self, p):
        # Calculate direction of force
        dir = self.position - p.position
        # Distance between objects
        d = dir.mag()
        # Normalize direction vector
        dir.normalize()
        # Keep distance within a reasonable range
        d = constrain(d, 1, 100)
        # Repelling force is inversely proportional to distance
        force = -1 * self.power / (d * d)
        # Get force vector -= 1> magnitude * direction
        dir.mult(force)
        return dir


class Particle:

    def __init__(self, position):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(random(-1, 1) / 5, 0)
        self.position = position.copy()
        self.timeToLive = 255.0
        self.mass = random(5, 20)

    def run(self):
        self.update()
        self.display()

    def applyForce(self, force):
        self.acceleration.add(force / self.mass)

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.timeToLive -= 1

    def display(self):
        stroke(0, 0, 0, self.timeToLive)
        strokeWeight(2)
        fill(255, 0, 0, self.timeToLive)
        ellipse(self.position.x, self.position.y, self.mass, self.mass)

    def isDead(self):
        if (self.timeToLive < 0.0 or self.position.y > 410):
            return True
        else:
            return False

class ParticleSystem():

    def __init__(self, position):
        self.origin = position
        self.particles = []

    def addParticle(self):
        self.particles.append(Particle(self.origin))

    def applyForce(self, f):
        for p in self.particles:
            p.applyForce(f)

    def applyGravity(self):
        for p in self.particles:
            p.applyForce(gravity * p.mass)

    def applyRepeller(self, r):
        for p in self.particles:
            force = r.calculateRepelForce(p)
            p.applyForce(force)

    def run(self):
        for p in reversed(self.particles):
            p.run()
            if p.isDead():
                self.particles.remove(p)
        # for i in reversed(range(len(self.particles))):
        #     p = self.particles[i]
        #     p.run()
        #     if p.isDead():
        #         del self.particles[i]
