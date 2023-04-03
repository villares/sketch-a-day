margin = 20
grid_size = 500
perms = ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))

def setup():
    size(1500, 1000)
    text_align(LEFT, CENTER)
    background(128)
    no_stroke()
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 4, perms[n])
        with push_matrix():
            translate(0, grid_size)
            grid(margin, margin, grid_size - margin * 2, 4, perms[n + 3])
        translate(grid_size, 0)
    save('out_0.png')

def grid(xo, yo, largura_total, n, perm):
    w = largura_total / n
    color_step = 255 / n
    half_step = color_step / 2
    text_size(w / 8)
    text_leading(w / 9)
    for j in range(n):
        x = xo + w * j + w / 2
        for i in range(n):
            y = yo + w * i + w / 2
            a = round(half_step + i * color_step)
            b = round(half_step + j * color_step)      
            c = round(255 - i * color_step -half_step)
            R, G, B = (a, b, c)[perm[0]], (a, b, c)[perm[1]], (a, b, c)[perm[2]]         
            fill(R, G, B) 
            circle(x, y, w * 0.98)
            fill(255)
            text(f'R:{R}\nG:{G}\nB:{B}\n', x, y) 
            
