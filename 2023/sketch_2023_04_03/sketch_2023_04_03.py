grid_size = 500
perts = ((0, 1, 2), (0, 2, 1), (1, 0, 2)) # Perturbations

def setup():
    size(1500, 1000)
    text_align(LEFT, CENTER)
    background(128)
    no_stroke()
    margin = 70
    r = 0.7
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 3, perts[n], r, False)
        translate(grid_size, 0)
    translate(-grid_size * 3, 0)
    margin = 10
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 4, perts[n], r, False)
        translate(grid_size, 0)
    translate(-grid_size * 3, grid_size)
    margin = 70
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 3, perts[n], r, True)
        translate(grid_size, 0)
    translate(-grid_size * 3, 0)
    margin = 10
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 4, perts[n], r, True)
        translate(grid_size, 0)

    save('out_0.png')

def grid(xo, yo, largura_total, n, pert, reduction, color_margin):
    w = largura_total / n
    color_step = 255 / (n if color_margin else n-1)
    half_step = color_step / 2 if color_margin else 0
    text_size(w / 8)
    text_leading(w / 9)
    for j in range(n):
        x = xo + w * j + w / 2
        for i in range(n):
            y = yo + w * i + w / 2
            a = round(half_step + i * color_step)
            b = round(half_step + j * color_step)      
            c = round(255 - i * color_step -half_step)
            R, G, B = (a, b, c)[pert[0]], (a, b, c)[pert[1]], (a, b, c)[pert[2]]         
            fill(R, G, B) 
            circle(x, y, w * reduction)
            fill(0)
            text(f'R:{R}\nG:{G}\nB:{B}\n', x, y) 
            
