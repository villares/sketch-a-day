# https://discourse.processing.org/t/fluid-fun-with-py5-and-numpy/47943

import py5
import numpy as np


def normalize(a):
    a_min = np.min(a)
    a_max = np.max(a)
    return (a - a_min) / (a_max - a_min)

def add_source(field, source, dt):
    field += dt * source


def set_boundary(boundary, field):
    if boundary == "u":
        # Left column.
        field[1:-1, 0] = -field[1:-1, 1]
        # Right column.
        field[1:-1, -1] = -field[1:-1, -2]
    else:
        # Left column.
        field[1:-1, 0] = field[1:-1, 1]
        # Right column.
        field[1:-1, -1] = field[1:-1, -2]

    if boundary == "v":
        # Bottom row.
        field[-1, 1:-1] = -field[-2, 1:-1]
        # Top row.
        field[0, 1:-1] = -field[1, 1:-1]
    else:
        # Bottom row.
        field[-1, 1:-1] = field[-2, 1:-1]
        # Top row.
        field[0, 1:-1] = field[1, 1:-1]

    # Bottom-left corner.
    field[-1, 0] = 0.5 * (field[-2, 0] + field[-1, 1])
    # Top-left corner.
    field[0, 0] = 0.5 * (field[1, 0] + field[0, 1])
    # Bottom-right corner.
    field[-1, -1] = 0.5 * (field[-1, -2] + field[-2, -1])
    # Top-right corner.
    field[0, -1] = 0.5 * (field[0, -2] + field[1, -1])


def diffuse(boundary, field, field_prev, diff, dt):
    N = field.shape[0] - 2
    a = dt * diff * N * N

    # Solve the system with Gauss-Seidel.
    for _ in range(20):
        # Get the field values at the neighboring grid cells.
        left = field_prev[1:-1, 0:-2]
        right = field_prev[1:-1, 2:]
        top = field_prev[0:-2, 1:-1]
        bottom = field_prev[2:, 1:-1]
        neighbors = left + right + top + bottom
        # Update the field.
        field[1:-1, 1:-1] = (field_prev[1:-1, 1:-1] + a * neighbors) / (1 + 4 * a)

    # Update the boundaries.
    set_boundary(boundary, field)


def advect(boundary, field, field_prev, u, v, dt):
    N = field.shape[0] - 2
    dt0 = dt * N

    # Create a coordinate grid.
    x = np.arange(1, N + 1)
    y = np.arange(1, N + 1)
    X, Y = np.meshgrid(x, y)

    # Calculate the coordinates of particles' points of origin.
    xo = X - dt0 * u[1:-1, 1:-1]
    yo = Y - dt0 * v[1:-1, 1:-1]

    # Constrain the coordinates to the grid interior.
    xo = np.clip(xo, 0.5, N + 0.5)
    yo = np.clip(yo, 0.5, N + 0.5)

    # Calculate the indices of the grid cells surrounding the
    # point of origin.
    xl = xo.astype(int)
    xr = xl + 1
    yt = yo.astype(int)
    yb = yt + 1

    # Calculate the interpolation weights for surrounding grid cells.
    wr = xo - xl
    wl = 1 - wr
    wb = yo - yt
    wt = 1 - wb

    # Get the field values at the surrounding grid cells.
    f_tl = field_prev[yt.ravel(), xl.ravel()].reshape(N, N)
    f_tr = field_prev[yt.ravel(), xr.ravel()].reshape(N, N)
    f_bl = field_prev[yb.ravel(), xl.ravel()].reshape(N, N)
    f_br = field_prev[yb.ravel(), xr.ravel()].reshape(N, N)

    # Update the field
    field[1:-1, 1:-1] = wl * (wb * f_bl + wt * f_tl) + wr * (wb * f_br + wt * f_tr)

    # Update the boundaries.
    set_boundary(boundary, field)


def project(u, v, u0, v0):
    N = u.shape[0] - 2
    h = 1 / N

    # Update v0 and reset u0.
    du = u[1:-1, 2:] - u[1:-1, 0:-2]
    dv = v[2:, 1:-1] - v[0:-2, 1:-1]
    v0[1:-1, 1:-1] = -0.5 * h * (du + dv)
    u0[1:-1, 1:-1] = 0

    # Update the boundaries.
    set_boundary(None, v0)
    set_boundary(None, u0)

    # Calculate u0 with Gauss-Seidel.
    for _ in range(20):
        # Get the field values at the neighboring grid cells.
        left = u0[1:-1, 0:-2]
        right = u0[1:-1, 2:]
        top = u0[0:-2, 1:-1]
        bottom = u0[2:, 1:-1]
        neighbors = left + right + top + bottom
        # Update the field.
        u0[1:-1, 1:-1] = (v0[1:-1, 1:-1] + neighbors) / 4
        # Update the boundary.
        set_boundary(None, u0)

    # Update the velocities.
    u[1:-1, 1:-1] -= 0.5 * (u0[1:-1, 2:] - u0[1:-1, 0:-2]) / h
    v[1:-1, 1:-1] -= 0.5 * (u0[2:, 1:-1] - u0[0:-2, 1:-1]) / h

    # Update the boundaries.
    set_boundary("u", u)
    set_boundary("v", v)


def dens_step(field, field_prev, u, v, diff, dt):
    add_source(field, field_prev, dt)

    # Go backward in time.
    field, field_prev = field_prev, field
    diffuse(None, field, field_prev, diff, dt)

    # Go forward in time.
    field, field_prev = field_prev, field
    advect(None, field, field_prev, u, v, dt)


def vel_step(u, v, u0, v0, visc, dt):
    add_source(u, u0, dt)
    add_source(v, v0, dt)

    # Go backward in time.
    u, u0 = u0, u
    diffuse("u", u, u0, visc, dt)
    v, v0 = v0, v
    diffuse("v", v, v0, visc, dt)
    project(u, v, u0, v0)

    # Go forward in time.
    u, u0 = u0, u
    v, v0 = v0, v
    advect("u", u, u0, u0, v0, dt)
    advect("v", v, v0, u0, v0, dt)
    project(u, v, u0, v0)


# Simulation setup.
N = 400
dt = 1
diff = 0.1
visc = 0.001

# Velocity arrays.
u_prev = np.zeros((N + 2, N + 2))
u = np.zeros((N + 2, N + 2))
v_prev = np.zeros((N + 2, N + 2))
v = np.zeros((N + 2, N + 2))

# Density arrays.
dens_prev = np.zeros((N + 2, N + 2))
dens = np.zeros((N + 2, N + 2))


def setup():
    py5.size(N, N)
    py5.pixel_density(1)


def draw():
    # Reset sources.
    dens_prev[:, :] = 0
    u_prev[:, :] = 0
    v_prev[:, :] = 0

    # Get the mouse coordinates.
    mx = np.clip(py5.mouse_x, 1, N).astype(int)
    my = np.clip(py5.mouse_y, 1, N).astype(int)

    # Add sources.
    u_prev[my - 1 : my + 1, mx - 1 : mx + 1] = np.random.uniform(-1, 1)
    v_prev[my - 1 : my + 1, mx - 1 : mx + 1] = -1
    dens_prev[my - 1 : my + 1, mx - 1 : mx + 1] = 100

    # Update the simulation.
    vel_step(u, v, u_prev, v_prev, visc, dt)
    dens_step(dens, dens_prev, u, v, diff, dt)

    # Normalize the variable to be drawn.
    D = normalize(dens[1:-1, 1:-1])

    # Scale the values for display.
    D *= 255

    # Display the RGB array.
    py5.load_np_pixels()
    py5.np_pixels[:, :, 1] = 128 # red channel
    py5.np_pixels[:, :, 2] = 128 # green channel
    py5.np_pixels[:, :, 3] = D # blue channel
    py5.update_np_pixels()

    py5.window_title(str(round(py5.get_frame_rate(), 1)))

py5.run_sketch()