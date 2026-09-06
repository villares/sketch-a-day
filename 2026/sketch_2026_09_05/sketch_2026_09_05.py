import py5

A = 15
B = 13
C = 15
D = 13

def setup():
    py5.size(600, 600)
    py5.stroke_weight(3)
    
def draw():
    py5.background(200, 200, 210)
    w = 20
    h = w // 2
    for y in range(0, py5.height, h):
        o = h * ((y // A) % B == 0) #py5.random_choice((0, 1))
        for x in range(0, py5.width , w):
            py5.line(o + x, y, o + x + h, y) 
    for x in range(0, py5.width, h):
        o = h * ((x // C) % D == 0) #py5.random_choice((0, 1))
        for y in range(0, py5.height, w):
            py5.line(x, o + y, x,o + y + h) 
    py5.no_loop()

def key_pressed():
    if py5.key == ' ':
        py5.redraw()
    elif py5.key == 's':
        py5.save_frame(f'{A}-{B}-{C}-{D}.png')
    
py5.run_sketch()




