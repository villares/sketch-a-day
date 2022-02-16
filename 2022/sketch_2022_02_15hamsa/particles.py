from collections import deque
from random import choice

step = 8

class Particle:
    
    F = 5000

    def __init__(self, position, PS):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(random(-1, 1) / 5, random(-1, 1) / 5)
        self.position = position.copy()
        self.history = deque(maxlen=15)
        self.mass = random(5, 25)
        self.tam = choice((10, 15, 20))
        self.time_to_live = self.tam * 2
        self.PS = PS

    def run(self):
        self.update()
        self.display()

    def applyForce(self, force):
        # print self.acceleration
        self.acceleration += force / self.mass

    def update(self):
        for p in self.PS.particles:
            if p is self:
                break
            else:
                dir = self.position - p.position
                # Distance between objects
                d = dir.mag()
                # Normalize direction vector
                dir.normalize()
                # Keep distance within a reasonable range
                d = constrain(d, 1, 100)
                # Repelling force is inversely proportional to distance
                force = 1 * self.F / (d * d)
                # print force
                force = constrain(force, 0, 50)
                # if force > 10:
                #     print force
                # Get force vector -= 1: magnitude * direction
                dir *= force
    
                self.applyForce(dir)    
                p.applyForce(dir * -1)
    
        self.history.append(self.position.copy())
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration.setMag(0)
        #self.time_to_live -= 1
        self.velocity *= .95
         
         
        self.position.x = self.position.x // step * step 
        self.position.y = self.position.y // step * step 
       
        if self.position.x > width - 150:
            self.position.x = + 150
            self.history.clear()
        if self.position.x < 150:
            self.position.x = width - 150
            self.history.clear()
        if self.position.y > height - 50:
            self.position.y = 50
            self.history.clear()
        if self.position.y < 50:
            self.position.y = height - 50
            self.history.clear()



    def display(self):
        colorMode(HSB)
        strokeWeight(self.tam)
        if len(self.history) > 2:
            h = list(enumerate(reversed(self.history)))
            for i, pa in h[1:]:
                _, pb = h[i-1]
                if i % 2 == 0 and i != len(h) - 1:
                    stroke(80)#stroke(50, 200, 200)
                else:
                    stroke(self.tam * 3 - 20, 255, 255)
                strokeWeight(self.tam)
                line(pa[0], pa[1], pb[0], pb[1])
            fill(self.tam * 2, 255, 200)
            _, ph = h[0]
            noStroke()
            # strokeWeight(1)
            # stroke(0)
            fill(255)
            circle(ph[0], ph[1], self.tam)
            fill(80)
            circle(ph[0], ph[1], self.tam * 0.33)
            
    
    def isDead(self):
        if self.time_to_live < 0.0:
            return True
        else:
            return False

class ParticleSystem():

    def __init__(self, position):
        self.origin = position
        self.particles = []

    def addParticle(self, pos=None):
        pos = pos or self.origin
        self.particles.append(Particle(pos, self))

    def applyForce(self, force):
        for p in self.particles:
            p.applyForce(force)

    def applyGravity(self):
        for p in self.particles:
            p.applyForce(gravity * p.mass)

    def applyRepeller(self, r):
        for p in self.particles:
            force = r.calculateRepelForce(p)
            p.applyForce(force)

    def run(self, force=None):
        for p in reversed(self.particles):
            p.run()
            
            if force is not None:
                self.applyForce(force)
            
            if p.isDead():
                self.particles.remove(p)
