from itertools import product, combinations

def setup():
    global combos
    size(400, 400, P3D)
    grid = list(product(range(-50, 51, 50),
                       repeat=2))
    combos = list(combinations(grid, 5))
    print(len(combos))
    
def draw():
    translate(200, 200)  
    ortho()
    rotateX(-atan(sin(radians(45))))
    rotateY(radians(45))
    background(200)
    i = frameCount % len(combos)
    cs = (combos + combos)[i:i+20]
    for z, positions in zip(range(-100, 101, 10), cs):
        pos = map(lambda p: p+(z,), positions)
        _ = list(map(element, pos))

def element(pos):
    x, y, z = pos
    push()
    fill(128 + z, 128 + x, 128 + y)
    translate(x, z, y)
    box(50, 5, 50)
    pop()
