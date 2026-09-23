import py5

K = { 
    'a': 3,
    's': 4,
    'd': 5,
    'f': 6,
} 

def setup():
    py5.size(600, 600)
    py5.stroke_weight(5)
    
def draw():
    py5.background(128)
    w = 30
    h = w // 2
    for y in range(0, py5.height, h):
        offset_x = ((y // K['a']) % K['s'] == 0)
        py5.stroke(255 if offset_x else 0)
        for x in range(0, py5.width , w):
            py5.line(x + h * offset_x, y,
                     x + h + h * offset_x, y) 
    for x in range(0, py5.width, h):
        offset_y = ((x // K['d']) % K['f'] == 0)
        py5.stroke(255 if offset_y else 0)
        for y in range(0, py5.height, w):
            py5.line(x, y + h * offset_y,
                     x, y + h + h * offset_y) 
    py5.no_loop( )

def key_typed():
    if py5.key == 'p':
        py5.save_frame('{0}-{1}-{2}-{3}.png'.format(*K.values()))
    elif py5.key in 'ASDF':
        K[py5.key.lower()] += 1
        print(py5.key, K)
    elif py5.key in 'asdf':
        K[py5.key] -= 1 if K[py5.key] > 1 else 0
        print(py5.key, K)
    py5.redraw()        

py5.run_sketch()



