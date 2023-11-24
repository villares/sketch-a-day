"""
Code for py5 (py5coding.org) module mode

"""

import numpy as np
import py5

num_particles = 500
boid_length = 1000   # as a multiplying factor of boid velocity vector
dt = 0.1

def setup():
    global position, velocity #, pairs
    global scaled_heading, perpend_a, perpend_b
    py5.size(900, 900)
    position = np.random.rand(num_particles, 2)
    angles = 2.0 * np.pi * np.random.random(num_particles)
    speed = 0.01
    velocity = np.stack((speed * np.cos(angles),
                           speed * np.sin(angles)), axis=1)
    
def draw():
    global position
    py5.background(0)
    # Updating the "simulation"
    dx = np.subtract.outer(position[:, 0], position[:, 0])
    dy = np.subtract.outer(position[:, 1], position[:, 1])
    distance = np.hypot(dx, dy)    
    mask_0 = (distance > 0)
    mask_1 = (distance < 25)
    mask_2 = (distance < 50)
    mask_1 *= mask_0
    mask_2 *= mask_0
    mask_3 = mask_2
    mask_1_count = np.maximum(mask_1.sum(axis=1), 1)
    mask_2_count = np.maximum(mask_2.sum(axis=1), 1)
    mask_3_count = mask_2_count
    
    position += dt * velocity # update position
    position %= 1 # wrap position
    # Showing the frame rate on the windowt title
    draw_boids(position, velocity)
    py5.window_title(f'{py5.get_frame_rate():.1f}')

def draw_boids(position, velocity):
    scaled_position = position * py5.width
    scaled_heading = velocity * boid_length
    perpend_a = velocity[:,::-1].copy() * (boid_length / 3)
    perpend_a[:, 0] = -perpend_a[:, 0]
    perpend_b = velocity[:,::-1].copy() * (boid_length / 3)
    perpend_b[:, 1] = -perpend_b[:, 1]
    # the arrow points
    right_points = scaled_position + perpend_a
    left_points = scaled_position + perpend_b
    head_points = scaled_position + scaled_heading
    triangles = np.hstack(
        (left_points, right_points, head_points)).reshape(-1, 2)
    py5.no_stroke()
    py5.fill(255)
    with py5.begin_shape(py5.TRIANGLES):
        py5.vertices(triangles)

py5.run_sketch(block=False)