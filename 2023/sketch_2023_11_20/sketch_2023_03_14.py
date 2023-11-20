"""
Code for py5 (py5coding.org) module mode
"""

from itertools import product, combinations
import numpy as np
import py5

num_species = 4
num_particles = 500
dt = 0.1

def setup():
    global positions, velocities, species, species_masks, radius, pairs
    py5.size(900, 900)
    py5.color_mode(py5.HSB)
    positions = np.random.rand(num_particles, 2)
    angles = 2.0 * np.pi * np.random.random(num_particles)
    speed = 0.01
    velocities = np.stack((speed * np.cos(angles),
                           speed * np.sin(angles)), axis=1)
    species = np.random.randint(0, num_species, size=num_particles)
    species_masks = [(species == i, i) for i in range(num_species)] 
    pairs = np.array(list(combinations(range(num_particles), 2)))
    
def draw():
    global positions
    py5.background(0)
    difference_vectors = positions[pairs[:, 1]] - positions[pairs[:, 0]]
    #squared_distances = np.sum(difference_vectors**2, axis=1)
    squared_distances = np.einsum('ij,ij->i', difference_vectors, difference_vectors)
    # assuming a  square canvas... for drawing
    scaled_positions = positions * py5.width
    # find particles that are close to each other
    selected_pairs = pairs[squared_distances < 1 / 400]
    if selected_pairs.any():
        py5.stroke(255)
        py5.stroke_weight(1)
        py5.lines(np.hstack((scaled_positions[selected_pairs[:, 0]],
                             scaled_positions[selected_pairs[:, 1]])))
    # draw particles
    for mask, i in species_masks:
        py5.stroke(py5.color(i * 256 / num_species, 255, 255))
        py5.stroke_weight(5 + i * 2)
        py5.points(scaled_positions[mask])

    positions += dt * velocities # update positions
    positions %= 1 # wrap positions
    py5.window_title(f'{py5.get_frame_rate():.1f}')

py5.run_sketch()
