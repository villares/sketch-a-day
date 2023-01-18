"""
Code for py5 (py5coding.org) imported mode
"""

def setup():
    size(1024, 1024)
    #no_loop()
    
def draw():
    random_seed(1)
    background(0)
    grid(0, 0, width, 4)
    #save_frame('###.png')

def grid(grid_x, grid_y, grid_size, n):
    cell_size = grid_size / n
    for i in range(n):
        x = width / 2 * sin((grid_x + i) * cell_size  + frame_count / 10e12) + width / 2
        for j in range(n):
            y = height / 2 * cos((grid_y + j) * cell_size + frame_count / 10e12) + height / 2
            if cell_size < 20:
                fill(x % 255, 200, y % 255)
                no_stroke()
                circle(x + cell_size / 2,
                       y + cell_size / 2,
                       cell_size)
            elif n == 1:
                fill(0, 0, 200)
                stroke(0)
                square(x, y, cell_size)
            else:
                next_n = int(random(1, 5))
                grid(x, y, cell_size, next_n)

def key_pressed():
    save_frame('###.png')
