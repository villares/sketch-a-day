# this is a py5 "imported mode" sketch, you'll need the py5 runner tool
# learn more at https://py5coding.org

def setup():
    size(1600, 800)
    no_stroke()
    rect_mode(CENTER)
    rows = 50
    cols = 100
    f = 0.3
    grid_size = width / cols
    max_size = grid_size - 2
    color_mode(CMAP, mpl_cmaps.VIRIDIS, max_size * max_size)
    background('black')
    for row in range(rows):  # 0, 1, 2 ... rows - 1
        y = row * grid_size + grid_size / 2
        for col in range(cols):  # 0, 1, 2, ... cols - 1
            x = col * grid_size + grid_size / 2
            w = grid_size / 2 + max_size / 2 * cos(radians(x) * f)
            h = grid_size / 2 + max_size / 2 * sin(radians(y) * f)
            fill(w * h)
            rect(x, y, w, h)
            w = grid_size / 2 + max_size / 2 * sin(radians(x) * f) 
            h = grid_size / 2 + max_size / 2 * cos(radians(y) * f)
            fill(w * h)
            rect(x, y, w, h)
            
    save('out.png')



