# Based on
# https://github.com/roholazandie/boids/tree/master

import py5
import numpy as np

def setup():
    global flock
    py5.size(500, 500) 
    flock = [
        Boid(py5.random(py5.width),
             py5.random(py5.height))
        for _ in range(20)
        ]
    py5.stroke_weight(2)
    py5.stroke(255)

def draw():
    py5.background(30, 30, 47)
    for boid in flock:
        boid.update()
        
    py5.window_title(f'{py5.get_frame_rate():.2f}')

class Boid():

    max_force = 0.3
    max_force_sq = max_force ** 2
    max_speed = 5
    max_speed_sq = max_speed ** 2
    perception = 200
    perception_sq = perception ** 2


    def __init__(self, x, y):
        self.position = py5.Py5Vector(x, y)
 #       vec = py5.Py5Vector.random(2) - 0.5 * 10
        vec = (np.random.rand(2) - 0.5) * 10
        self.velocity = py5.Py5Vector(*vec)
        vec = (np.random.rand(2) - 0.5) / 2
        self.acceleration = py5.Py5Vector(*vec)
  
    def update(self):
        self.edges()
        self.apply_behaviour(flock)       
        self.position += self.velocity
        self.velocity += self.acceleration
        #limit
        if self.velocity.mag_sq > self.max_speed_sq:
            self.velocity.mag = self.max_speed

        py5.line(self.position.x,
                 self.position.y,
                 self.position.x + self.velocity.x * 5,
                 self.position.y + self.velocity.y * 5,
                 )


    def apply_behaviour(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.acceleration = alignment
        self.acceleration += cohesion
        self.acceleration += separation

    def edges(self):
        if self.position.x > py5.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = py5.width

        if self.position.y > py5.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = py5.height

    def align(self, boids):
        steering = py5.Py5Vector2D()
        total = 0
        avg_vector = py5.Py5Vector2D()
        for boid in boids:
            if (boid.position - self.position).mag_sq < self.perception_sq:
                avg_vector += boid.velocity
                total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = avg_vector.norm * self.max_speed
            steering = avg_vector - self.velocity

        return steering

    def cohesion(self, boids):
        steering = py5.Py5Vector2D()
        total = 0
        center_of_mass = py5.Py5Vector2D()
        for boid in boids:
            if (boid.position - self.position).mag_sq < self.perception_sq:
                center_of_mass += boid.position
                total += 1
        if total > 0:
            center_of_mass /= total
            vec_to_com = center_of_mass - self.position
            if vec_to_com.mag_sq > 0:
                vec_to_com.mag = self.max_speed
            steering = vec_to_com - self.velocity
            if steering.mag_sq > self.max_force_sq:
                steering.mag = self.max_force

        return steering

    def separation(self, boids):
        steering = py5.Py5Vector2D()
        total = 0
        near_vector = py5.Py5Vector2D()
        for boid in boids:
            if self != boid:
                diff = boid.position - self.position
                if diff.mag_sq < self.perception_sq:
                    near_vector += diff.norm
                    total += 1
        if total > 0:
            avg_vector = near_vector / total
            if steering.mag_sq > 0:
                avg_vector.mag = self.max_speed
            steering = avg_vector - self.velocity
            if steering.mag_sq > self.max_force_sq:
                steering.mag = self.max_force

        return steering
    
py5.run_sketch()