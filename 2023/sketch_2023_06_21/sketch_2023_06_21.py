from itertools import product, combinations
import py5

W = 80

def setup():
    global combos
    py5.size(600, 600, py5.P3D)
    #py5.pixel_density(2)
    xy = product(range(-1, 3, 1), repeat=2) # -1, 0, 1, 2
    grid = [(x * W - W / 2, y * W - W / 2) for x, y in xy]                    
    combos = list(combinations(grid, 2))
    print(len(combos)) # 120 for combos of 16 positions, 2 at a time
    py5.frame_rate(10)
    py5.color_mode(py5.HSB)

def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    py5.ortho()
    py5.rotate_x(-py5.atan(py5.sin(py5.radians(45))))
    py5.rotate_y(py5.radians(45))
    py5.background(0)
    f = (py5.frame_count - 1) % len(combos)
    combos_extended = combos + combos[:11]  # combos plus 11 from start
    combo_positions = combos_extended[f:f+11]  # slice of 11 combos start at f
    #combo_positions = [combos[(i + f) % len(combos)] for i in range(11)]
    for positions, z in zip(combo_positions, range(100, -101, -20)):
        py5.fill((255 + z - f * 20) % 255, 200, 200)                
        for pos in positions:
            element(pos + (z,), W)
    if py5.frame_count < len(combos) + 1:
        py5.save_frame('###.png')
    
def element(pos, w):
    x, y, z = pos
    with py5.push_matrix():
        py5.translate(x, z, y)  # note the inversion
        py5.box(w, w / 10, w)

py5.run_sketch()