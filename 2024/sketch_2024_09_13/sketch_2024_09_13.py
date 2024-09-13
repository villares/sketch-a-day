# based on Jim Bumgardner's 10/6/2011 sketch
# https://openprocessing.org/sketch/41142

import py5
from py5 import sin, cos, asin, PI, TWO_PI, radians

Z_OFFSET = -100
MAX_POINTS = 100000
num_points = 1000

rotation_x = 0
rotation_y = 0
velocity_x = 0
velocity_y = 0
 
phi = (py5.sqrt(5)+ 1) / 2 - 1  # golden ratio
ga = phi * 2 * PI           # golden angle
 
sphere_pts = []
add_pts = False
 
def setup():
    global R
    py5.size(600, 600, py5.P3D)
    py5.color_mode(py5.HSB, 1, 1, 1)
    R = 0.8 * py5.height / 2
    update_sphere()
          
def draw():
    global rotation_x, rotation_y, velocity_x, velocity_y
    global num_points
    
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2, Z_OFFSET)   
    t =  py5.millis() * 0.01
    py5.rotate_x(radians(rotation_x)) 
    py5.rotate_y(radians(270 - rotation_y - t))
    py5.stroke_weight(3)

    for lat, lon in sphere_pts:
        x = R * cos(lat) * cos(lon)
        y = R * cos(lat) * sin(lon)
        z = R * sin(lat)
        #lum =  (cos(lon + PI / 3 + radians(270 - rotation_y - t)) + 1) / 2
        mz = py5.model_z(x, y, z)
        lum = 1 + mz / 600
        #py5.stroke((lon + PI) / TWO_PI, 0.5 * lum, 0.2 + lum * 0.8)
        py5.stroke((lon + PI) / TWO_PI, 1, lum)
        py5.point(x, y, z)

    rotation_x += velocity_x
    rotation_y += velocity_y
    velocity_x *= 0.95
    velocity_y *= 0.95
    
    if py5.is_mouse_pressed:
        velocity_x += (py5.mouse_y - py5.pmouse_y) * 0.01
        velocity_y -= (py5.mouse_x - py5.pmouse_x) * 0.01

    if add_pts:
        num_points += 1
        num_points = min(num_points, MAX_POINTS)
        update_sphere()

def update_sphere():
    sphere_pts.clear()
    for i in range(num_points):
        lon = ga * i / TWO_PI
        lon -= py5.floor(lon)
        lon *= TWO_PI
        if lon >  PI:
            lon -= TWO_PI 
        # Convert dome height (which is proportional to surface area) to latitude
        lat = asin(-1 + 2 * i / float(num_points))
        sphere_pts.append((lat, lon))  

def key_pressed():
    global add_pts
    add_pts = not add_pts

py5.run_sketch()
