# -----------------------------------------------------------------------------
# Copyright (2017) Alexandre B A Villares - BSD license
# Numpy flocking with py5
#
# Based on the boids flocking example from "From Pytnon to Numpy"
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import py5

class Flock:
    def __init__(self, count):
        self.min_velocity = 0.5 / py5.width
        self.max_velocity = 2.0 / py5.width
        self.max_acceleration = 0.03 / py5.width
        self.velocity = np.zeros((count, 2), dtype=np.float32)
        self.position = np.zeros((count, 2), dtype=np.float32)

        angle = np.random.uniform(0, 2*np.pi, count)
        self.velocity[:, 0] = np.cos(angle)
        self.velocity[:, 1] = np.sin(angle)
        angle = np.random.uniform(0, 2*np.pi, count)
        radius = np.random.uniform(0, 1, count) / 4
        self.position[:, 0] = 0.5 + np.cos(angle)*radius
        self.position[:, 1] = 0.5 + np.sin(angle)*radius

    def run(self):
        position = self.position
        velocity = self.velocity
        min_velocity = self.min_velocity
        max_velocity = self.max_velocity
        max_acceleration = self.max_acceleration
        n = len(position)

        dx = np.subtract.outer(position[:, 0], position[:, 0])
        dy = np.subtract.outer(position[:, 1], position[:, 1])
        distance = np.hypot(dx, dy)
        print(distance.shape)
        # Compute common distance masks
        mask_0 = (distance > 0)
        mask_1 = (distance < 25 / py5.width)
        mask_2 = (distance < 50 / py5.width)
        mask_1 *= mask_0
        mask_2 *= mask_0
        mask_3 = mask_2
        mask_1_count = np.maximum(mask_1.sum(axis=1), 1)
        mask_2_count = np.maximum(mask_2.sum(axis=1), 1)
        mask_3_count = mask_2_count

        # Separation
        mask, count = mask_1, mask_1_count
        target = np.dstack((dx, dy))
        target = np.divide(target, distance.reshape(n, n, 1)**2, out=target,
                           where=distance.reshape(n, n, 1) != 0)
        steer = (target*mask.reshape(n, n, 1)).sum(axis=1)/count.reshape(n, 1)
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = max_velocity*np.divide(steer, norm, out=steer,
                                       where=norm != 0)
        steer -= velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)

        separation = steer

        # Alignment
        # ---------------------------------------------------------------------
        # Compute target
        mask, count = mask_2, mask_2_count
        target = np.dot(mask, velocity)/count.reshape(n, 1)

        # Compute steering
        norm = np.sqrt((target*target).sum(axis=1)).reshape(n, 1)
        target = max_velocity * np.divide(target, norm, out=target,
                                          where=norm != 0)
        steer = target - velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)
        alignment = steer

        # Cohesion
        # ---------------------------------------------------------------------
        # Compute target
        mask, count = mask_3, mask_3_count
        target = np.dot(mask, position)/count.reshape(n, 1)

        # Compute steering
        desired = target - position
        norm = np.sqrt((desired*desired).sum(axis=1)).reshape(n, 1)
        desired *= max_velocity / norm
        steer = desired - velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)
        cohesion = steer

        # ---------------------------------------------------------------------
        acceleration = 1.5 * separation + alignment + cohesion
        velocity += acceleration

        norm = np.sqrt((velocity*velocity).sum(axis=1)).reshape(n, 1)
        velocity = np.multiply(velocity, max_velocity/norm, out=velocity,
                               where=norm > max_velocity)
        velocity = np.multiply(velocity, min_velocity/norm, out=velocity,
                               where=norm < min_velocity)
        position += velocity

        # Wraparound
        position += (1, 1)
        position %= (1, 1)


def setup():
    global flock
    py5.size(640, 640)
    N = 500
    flock = Flock(N)

def draw():
    py5.background(0)
    flock.run()
    boid_length = 10
    position = flock.position * py5.width
    #mags =  np.sqrt(np.sum(flock.velocity**2, axis=1))
    #norm_vel = flock.velocity / mags[:,None]
    norm_vel = flock.velocity / np.linalg.norm(
        flock.velocity,axis=1, keepdims=True)
    heading = norm_vel * boid_length
    perpend_a = norm_vel[:,::-1].copy() * (boid_length / 3)
    perpend_a[:, 0] = -perpend_a[:, 0]
    perpend_b = norm_vel[:,::-1].copy() * (boid_length / 3)
    perpend_b[:, 1] = -perpend_b[:, 1]
    # the arrow points
    right_points = position + perpend_a
    left_points = position + perpend_b
    head_points = position + heading
    triangles = np.hstack(
        (left_points, right_points, head_points)).reshape(-1, 2)
    py5.no_stroke()
    py5.fill(255)
    with py5.begin_shape(py5.TRIANGLES):
        py5.vertices(triangles)
    py5.window_title(f'{py5.get_frame_rate():.1f}')


py5.run_sketch(block=False)
