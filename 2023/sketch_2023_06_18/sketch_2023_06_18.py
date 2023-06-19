from itertools import product, combinations

def setup():
    global combos
    size(400, 400, P3D)
    grid = list(product(range(-75, 100, 50),
                       repeat=2))
    combos = list(combinations(grid, 5))
    print(len(combos))
    frame_rate(10)
    color_mode(HSB)
    
def draw():
    translate(200, 225)  
    ortho()
    rotate_x(-atan(sin(radians(45))))
    rotate_y(radians(45))

    background(200)
    i = frame_count % len(combos)
    cs = (combos + combos)[i:i+10]
    for z, positions in zip(range(-100, 101, 20), cs):
        
        fill((255 + z) % 255, 200, 200)
        pos_plus_z = map(lambda p: p+(z,), positions)
        for pos in pos_plus_z:
            element(pos)

def element(pos):
    x, y, z = pos
    push()
    translate(x, z, y)
    box(50, 5, 50)
    pop()
