# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

n = 5
nc = 9 #  3, 5, 6, 7, 9, 10
a = 101
b = 100
#c = 2

def setup():
    py5.size(800, 800)
    py5.no_smooth()
    py5.no_stroke()
    py5.color_mode(py5.CMAP, 'tab20b', 255)
    
def f(x, y):
    return (y % a) ^ (x % b) #* (x + y * c)

def draw():
    w =  int(py5.width / n) 
    for x in range(w):
        for y in range(w):
            r = f(x, y) 
            py5.fill((r % nc) * (255/(nc - 1)))
            py5.square(x * n, y * n, n)
    py5.no_loop()


def key_pressed():
    py5.redraw()
    if py5.key == 's':
        py5.save_frame(f'{a}-{b}-nc{nc}.png')

py5.run_sketch(block=False)