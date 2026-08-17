# based on sketch_191216a.pyde

import py5
from py5_tools import animated_gif

def setup():
    global seed
    py5.size(800, 400, py5.P3D)
    py5.frame_rate(10)
    seed = 26876  # novaSemente()
    py5.color_mode(py5.HSB)
    animated_gif(
        'out.gif',
         frame_numbers=range(1, 91, 2),
         duration=0.166
    )

def draw():
    py5.background(255)
    py5.directional_light(255, 0, 255, 0, 0, 100)
    py5.directional_light(255, 0, 255, 0, 0, -100)
    py5.directional_light(255, 0, 255, 100, 100, 100)
    py5.no_stroke()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.radians(-22.5))
    r = py5.height / 2
    t = py5.radians(py5.frame_count)
    for i in range(36):
        py5.random_seed(seed + i % 9)
        for j, z in enumerate(range(-py5.width, py5.width, 40)):
            d = -1 if j % 2 else 1
            a = py5.radians(i * 10)
            x = r * py5.sin(a + t * d)
            y = r * py5.cos(a + t * d)
            w = py5.random(5, 23)
            py5.fill(w ** 3 / 65, 255, 255)
            b = py5.radians(py5.random(180))
            c = py5.radians(py5.random(180))
            caixa(x, y, z, w, rot_x=b, rot_y=c) #, rot_z=-a)

def key_pressed():
    global seed
    if py5.key == ' ':
        seed = nova_semente()
    elif py5.key == 's':
        py5.save_frame('###out.png')

def nova_semente():
    s = int(py5.random(1000000))
    print(f'seed: {s}')
    return s

# def cor_sorteada():
#     return py5.color(py5.random(256), py5.random(256), py5.random(256))

def caixa(x, y, z,
          w, h=None, d=None,
          rot_x=0, rot_y=0, rot_z=0):
    h = w if h is None else h
    d = w if d is None else d
    py5.push_matrix()
    py5.translate(x, y, z)
    py5.rotate_x(rot_x)
    py5.rotate_y(rot_y)
    py5.rotate_z(rot_z)
    py5.box(w, h, d)
    py5.pop_matrix()


py5.run_sketch()

