SIN_60 = sqrt(3) * 0.5  # sin(radians(60))
W = 200
H = SIN_60 * W 

import py5_tools

def setup():
    size(800, 780)
    no_stroke()
    py5_tools.animated_gif(filename='out.gif', frame_numbers=range(0, 360, 2), duration=0.1)

def draw():
    background(0, 0, 128)
    for i in range(-1, 6):
        for j in range(-1, 5): 
            x, y = ij_to_xy(i, j)
            hex(x, y, 100 * sin(radians(frame_count)), 100 * cos(radians(frame_count)), [0, 255])

def ij_to_xy(i, j):
    OX, OY = W / 2, H / 2 
    if i % 2 == 0:
        y = j * H  + OY
    else:
        y = j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def hex(x, y, raio_a, raio_b, cores=[0]):
    cores = cores * 6
    passo = TWO_PI / 6
    for i in range(6):
        ang = passo * i
        x0 = x + cos(ang) * raio_a
        y0 = y + sin(ang) * raio_a
        x1 = x + cos(ang + passo) * raio_a
        y1 = y + sin(ang + passo) * raio_a
        x2 = x + cos(ang + passo) * raio_b
        y2 = y + sin(ang + passo) * raio_b
        x3 = x + cos(ang) * raio_b
        y3 = y + sin(ang) * raio_b
        fill(cores[i])
        quad(x0, y0, x1, y1, x2, y2, x3, y3)

