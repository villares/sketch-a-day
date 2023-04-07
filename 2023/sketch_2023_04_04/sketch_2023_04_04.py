from random import choice

grid_size = 500
perts = ((0, 1, 2), (0, 2, 1), (1, 0, 2)) # Perturbations
colors = set()

x = y = 0

def setup():
    size(1500, 600)
    text_align(LEFT, CENTER)
    background(128)
    no_stroke()
    margin = 20
    r = 0.9
    for n in range(3):
        grid(margin, margin, grid_size - margin * 2, 5, perts[n], r, False)
        translate(grid_size, 0)


def draw():
    global x, y
    fill(*choice(list(colors)))
    square(x, y, 10)
    x += 10
    if x > width:
        x = 0
        y += 10
    if y > height:
        no_loop()



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
            colors.add((R, G, B))
            circle(x, y, w * reduction)
            fill(0)
            text(f'R:{R}\nG:{G}\nB:{B}\n', x, y) 
            