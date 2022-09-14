from itertools import product, combinations
from villares.helpers import save_png_with_src

w = 20  # width base-value for single element
th = w * sqrt(3) / 2  # triangle height
all_colors = (
    color(0),
    color(200, 100, 0),
    color(100, 0, 200),
    color(0, 200, 100),
    color(200, 200, 0),
    color(200, 0, 200),
    color(0, 200, 200),
    color(255),
)

def setup():
    size(660, 680)
    no_stroke()
    rect_mode(CENTER)
    shapes = (t, s, c)  # triangle, square, circle (shape drawing functions)
    color_combos = list(combinations(range(len(all_colors)), 2))
    all_combos = set()
    for selected_colors in color_combos:
        options = (tuple((func, color_index)
                         for color_index in selected_colors)
                   for func in shapes)
        combos = list(product(*options))  # *options unpacks it as serveral args
        all_combos.update(combos)
    print(f'Combinations: {len(all_combos)}')
    translate(w / 2, w / 4)
    x = y = w
    for combo in sorted(all_combos, key=sorting_func):
        for shape_func, ci in combo:
            fill(all_colors[ci])
            shape_func(x, y)
            x += w
        x -= w * 3
        y += w * 1.5
        if y > height -  w:
            y = w
            x += w * 4
    save_png_with_src()
    save_frame('sketch_2022_09_13.png')

def sorting_func(combo):
    return sum(ci * (len(all_colors) ** i) for i, (shp, ci)
               in enumerate(reversed(combo)))
    
def t(x, y):
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def s(x, y):
    square(x, y, w * 0.85),
   
def c(x, y):
    circle(x, y, w)
        