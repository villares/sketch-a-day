"""
Code for py5 (py5coding.org) module mode

Back from last numpy particle study sketch_2023_03_14.py
"""

import numpy as np
import py5

num_particles = 500
boid_length = 1000   # as a multiplying factor of boid velocity vector
dt = 0.1

def setup():
    global positions, velocities #, pairs
    global scaled_heading, perpendiculars_a, perpendiculars_b
    py5.size(900, 900)
    positions = np.random.rand(num_particles, 2)
    angles = 2.0 * np.pi * np.random.random(num_particles)
    speed = 0.01
    velocities = np.stack((speed * np.cos(angles),
                           speed * np.sin(angles)), axis=1)
    
def draw():
    global positions
    py5.background(0)
    py5.stroke(255)
    py5.stroke_weight(2)
    # I wonder if I should work with scaled positions from the start...
    scaled_positions = positions * py5.width
    # the following could be on setup with static velocities, but I'm putting
    # it here because I'll have changing velocities at some point
    scaled_heading = velocities * boid_length
    perpendiculars_a = velocities[:,::-1].copy() * (boid_length / 3)
    perpendiculars_a[:, 0] = -perpendiculars_a[:, 0]
    perpendiculars_b = velocities[:,::-1].copy() * (boid_length / 3)
    perpendiculars_b[:, 1] = -perpendiculars_b[:, 1]
    # the arrow points
    right_points = scaled_positions + perpendiculars_a
    left_points = scaled_positions + perpendiculars_b
    head_points = scaled_positions + scaled_heading
#     # single direction line
#     py5.lines(np.hstack((scaled_positions, head_points)))
#     # two line arrows
#     py5.stroke('blue')
#     py5.lines(np.hstack((head_points, left_points)))
#     py5.stroke('green')
#     py5.lines(np.hstack((head_points, right_points)))
#     # draw particles as red dots
#     py5.stroke(py5.color(0, 255, 255))
#     py5.stroke_weight(3)
#     py5.points(scaled_positions)
    # drawing the boids as triangles
#    triangles = np.concatenate((left_points, right_points,head_points),
#                               axis=1).reshape(-1, 2)
    triangles = np.hstack(
        (left_points, right_points, head_points)).reshape(-1, 2)
    with py5.begin_shape(py5.TRIANGLES):
        py5.vertices(triangles)
    # Updating the "simulation"
    positions += dt * velocities # update positions
    positions %= 1 # wrap positions
    # Showing the frame rate on the windowt title
    py5.window_title(f'{py5.get_frame_rate():.1f}')

py5.run_sketch(block=False)