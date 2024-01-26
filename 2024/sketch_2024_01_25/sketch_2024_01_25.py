SIN_60 = sqrt(3) * 0.5  # sin(radians(60))
W = 100
H = SIN_60 * W 

import py5_tools

def setup():
    size(800, 780)
    no_stroke()
    color_mode(HSB)
    py5_tools.animated_gif(filename='out.gif', frame_numbers=range(0, 180, 2), duration=0.1)

def draw():
    background(0, 0, 128)
    for i in range(-1, 12):
        for j in range(-1, 10): 
            x, y = ij_to_xy(i, j)
            hex(x, y, W/2,
                [color(32 + 18 * i, 255, 255),
                 color(220 - 18 * j, 255, 255)],
                i * (j + frame_count // 10))

def ij_to_xy(i, j):
    OX, OY = W / 2, H / 2 
    if i % 2 == 0:
        y = j * H  + OY
    else:
        y = j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def hex(x, y, radius, colors, rot=0):
    passo = TWO_PI / 6
    for i in (0, 3):
        ang = passo * i + rot * radians(60)
        x0 = x + cos(ang) * radius
        y0 = y + sin(ang) * radius
        x1 = x + cos(ang + passo) * radius
        y1 = y + sin(ang + passo) * radius
        x2 = x + cos(ang + passo * 2) * radius
        y2 = y + sin(ang + passo * 2) * radius
        x3 = x + cos(ang + passo * 3) * radius
        y3 = y + sin(ang + passo * 3) * radius
        fill(colors[i//3])
        quad(x0, y0, x1, y1, x2, y2, x3, y3)


