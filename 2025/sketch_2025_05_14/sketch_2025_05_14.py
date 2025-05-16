"""
Code for py5 (py5coding.org) imported mode

Recursive grid - I'm always grateful for Takao Shunsuke's inspiration.
"""

save_svg = False

def setup():
    size(1024 + 512, 512)
    no_loop()
    
def draw():
    output = create_graphics(width, height, SVG,
                    f'{frame_count}.svg')
    begin_record(output)
    color_mode(HSB)
    background(200)
    grid(0, 0, height, 4)
    grid(width / 3, 0, height, 4)
    grid(2 * width / 3, 0, height, 4)

    end_record()
    

def grid(grid_x, grid_y, grid_size, n):
    cell_size = grid_size / n
    for i in range(n):
        x = grid_x + i * cell_size
        for j in range(n):
            y = grid_y + j * cell_size
            if cell_size < 20:
                fill(cell_size * 10, 255, 150)
                no_stroke()
                circle(x + cell_size / 2,
                       y + cell_size / 2,
                       cell_size)
            elif n == 1:
                fill(128, 255, 150)
                no_stroke()
                square(x + 1, y + 1, cell_size - 2)
            else:
                next_n = int(random(1, 5))
                grid(x, y, cell_size, next_n)

def key_pressed():
    
    redraw()
   