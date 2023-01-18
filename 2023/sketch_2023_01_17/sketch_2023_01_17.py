"""
Code for py5 (py5coding.org) imported mode

Recursive grid - I'm always grateful for Takao Shunsuke's inspiration.
"""

def setup():
    size(1024, 1024)
    no_loop()
    
def draw():
    background(0)
    grid(0, 0, width, 4)
    save_frame('###.png')

def grid(grid_x, grid_y, grid_size, n):
    cell_size = grid_size / n
    for i in range(n):
        x = grid_x + i * cell_size
        for j in range(n):
            y = grid_y + j * cell_size
            if cell_size < 20:
                fill(x % 255, 200, y % 255)
                circle(x + cell_size / 2,
                       y + cell_size / 2,
                       cell_size)
            elif n == 1:
                fill(0, 0, 200)
                square(x, y, cell_size)
            else:
                next_n = int(random(1, 5))
                grid(x, y, cell_size, next_n)

def key_pressed():
    redraw()
