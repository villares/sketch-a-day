from itertools import product, combinations

w = 30  # width base-value for single element
th = w * sqrt(3) / 2  # triangle height

def setup():
    size(130 * 8, 500)
    no_stroke()
    rect_mode(CENTER)

    shapes = (t, s, c)  # triangle, square, circle (shape drawing functions)
    all_colors = (
        color(0),
        color(255),
        color(200, 200, 0),
        color(200, 0, 200),
        color(0, 200, 200),
    )
    color_combos = list(combinations(all_colors, 2))
    translate(w, w / 2)
    y = w
    for selected_colors in color_combos:
        #selected_colors = color_combos[0]
        options = (tuple((func, cc) for cc in selected_colors) for func in shapes)
        combos = list(product(*options))  # *on_offs unpacks it as serveral args
        print(f'Combinations: {len(combos)}')
        x = w
        for combo in combos:
            for func, color_choice in combo:
                draw_element(color_choice, func, x, y)  # False * 255 is 0 (black)
                x += w
            x += w
        y += w * 1.5
    save_frame('out.png')
    
def draw_element(c, shape_func, x, y):
    fill(c)
    shape_func(x, y)

def t(x, y):
    triangle(x - w / 2, y + th / 2, x + w / 2, y + th / 2, x, y - th / 2)
    
def s(x, y):
    square(x, y, w * 0.85),
   
def c(x, y):
    circle(x, y, w)
        
    