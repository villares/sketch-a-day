import py5_tools

def setup():
    global ta
    size(500, 500)
    #no_smooth()
    f = create_font('Tomorrow Bold', 48)    
    ta = create_graphics(width, height)
    ta.begin_draw()
    #ta.background(100, 0, 0)
    ta.text_font(f)
    ta.text_size(160)
    ta.text_leading(120)
    ta.text_align(CENTER, CENTER)
    ta.text('Hello\nSesc', width / 2, height / 2)    
    ta.end_draw()
    py5_tools.animated_gif('out.gif', duration=0.1, frame_numbers=range(1, 16))

def draw ():
    background(0)
    #image(ta, 50, 50) # para debug
    no_stroke()
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            px = ta.get_pixels(x, y)
            # -1 == py5.color(255) >>> True
            if px == color(255):
                fill(random(255), random(255), 128)
                circle(x, y, random(2, 10))