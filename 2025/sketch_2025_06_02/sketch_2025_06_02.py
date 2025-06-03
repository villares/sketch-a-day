"""
Code for py5 (py5coding.org) imported mode

Recursive grid - I'm always grateful for Takao Shunsuke's inspiration.
"""

save_svg = False

def setup():
    size(512, 512)
    color_mode(HSB)
    background(0)
    grid(0, 0, height, 4)
    save('out.png')    

def grid(grid_x, grid_y, grid_size, n):
    cell_size = grid_size / n
    for i in range(n):
        x = grid_x + i * cell_size
        for j in range(n):
            y = grid_y + j * cell_size
            if cell_size < 12:
                fill(cell_size * 10, 255, 150)
                no_stroke()
                circle(x + cell_size / 2,
                       y + cell_size / 2,
                       cell_size-1)
            elif n == 1:
                fill(cell_size * 10, 50, 150)
                no_stroke()
                square(x + 1, y + 1, cell_size - 2)
            else:
                next_n = int(random(1, 5))
                grid(x, y, cell_size, next_n)

   

