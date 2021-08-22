from random import choice

W = 60
grid = []
modules = dict()

def setup():
    size(600, 600)
    noFill()
    strokeWeight(2)
    generate_modules()
    grid[:] = 'abcdefg' #[choice('abcdefg') for _ in range(100)]
    
def draw():
    background(0)
    k = 0
    for i in range(10):
        for j in range(10):
            push()
            translate(i * W, j * W)
            if keyPressed:
                stroke(255)
                strokeWeight(0.5)
                rect(0, 0, W, W)
            if k < len(grid):
                draw_module(modules[grid[k]])
            pop()
            k += 1
    
def draw_module(module, o=5):
    w = W / 3
    for segment in module:
        for i in range(-2, 3):
            stroke(128 + 64 * i, 255, 128 - 64 * i)
            beginShape()
            for x, y in segment:
                vx = x * w + i * o if y == 0 or y == 3 else x * w
                vy = y * w + i * o if x == 0 or x == 3 else y * w
                vertex(vx, vy)
            endShape()
            
def h_flip(module):
    return tuple(tuple((3 - x, y) for x, y in segment)
                 for segment in module)
    
def d_flip(module):
    return tuple(tuple((y, x) for x, y in segment)
                 for segment in module)

def generate_modules():
    a = (
        ((1, 0), (0, 1)),
        ((2, 0), (1, 3)),
        ((3, 2), (2, 3)),
        )
    modules['a'] = a
    modules['b'] = h_flip(a)
    modules['c'] = (a[0], a[-1])
    modules['d'] = d_flip(a)
    modules['e'] = h_flip(d_flip(a))
    modules['f'] = h_flip((a[0], a[-1]))
    modules['g'] = h_flip((a[0], a[-1])) + (a[0], a[-1])
            
