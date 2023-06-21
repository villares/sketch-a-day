from itertools import product, combinations
import py5

def setup():
    global combos
    py5.size(400, 400, py5.P3D)
    grid = list(product(range(-75, 100, 50),
                        repeat=2))
    combos = list(combinations(grid, 2))
    print(len(combos)) # 120 for combos of 16 positions, 2 at a time
    py5.frame_rate(10)
    py5.color_mode(py5.HSB)

def draw():
    py5.translate(200, 225)
    py5.ortho()
    py5.rotate_x(-py5.atan(py5.sin(py5.radians(45))))
    py5.rotate_y(py5.radians(45))
    py5.background(0)
    i = py5.frame_count % len(combos)
    cs = (combos + combos)[i:i+10]
    for z, positions in zip(range(100, -101, -20), cs):
        py5.fill((255 + z + i * 20) % 255, 200, 200)                
        for pos in positions:
            element(pos + (z,))
    if py5.frame_count < len(combos) + 1:
        py5.save_frame('###.png')
    
def element(pos):
    x, y, z = pos
    with py5.push_matrix():
        py5.translate(x, z, y)  # note the inversion
        py5.box(50, 5, 50)

py5.run_sketch()
