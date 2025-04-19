from py5_tools import animated_gif

def setup():
    global img
    size(700, 300)
    background(0)
    no_stroke()
    frame_rate(10)
    f = create_font('Tomorrow ExtraBold', 140)
    img = create_graphics(width, height)
    img.begin_draw()
    img.smooth()
    img.text_font(f)
    img.text_size(120)
    img.text_leading(100)
    img.text_align(CENTER, CENTER)
    img.text('LETRAS\nEPECIAIS', width / 2, height / 2)
    img.end_draw()
    
    animated_gif('out.gif', duration=0.1, frame_numbers=range(1, 21))
    
def draw():
    background(100)
    step = 8
    for x in range(0, width, step): 
        for y in range(0, height, step):
            xc, yc = step / 2 + x, step / 2 + y
            px = img.get_pixels(int(xc), int(yc))
            if px != 0:
                draw_grid(x, y, step)

def draw_grid(x, y, step):
    random_spark = 0 if random(100) > 1 else random(255)
    grid_positions = (
        (0, 0, color(255, 0, 0)),
        (0, 1, color(0, 255, 0)),
        (1, 1, color(0, 0, 255)),
        (1, 0, random_spark)
    )
    for xo, yo, fill_color in grid_positions:
        fill(fill_color)
        rect(x + xo * step / 2, y + yo * step / 2, step / 2, step / 2)


