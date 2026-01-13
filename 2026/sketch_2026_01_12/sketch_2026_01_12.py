import py5
import py5_tools

black = py5.color(0)

def setup():
    global osb
    py5.size(600, 600, py5.P3D)
    f = py5.create_font('Tomorrow Bold', 130)
    # offscreen buffer
    osb = py5.create_graphics(600, 600)
    osb.no_smooth() # can only be used before begin_draw()
    osb.begin_draw()
    osb.background(black)
    osb.fill(255)
    osb.text_font(f)
    osb.text_align(py5.CENTER, py5.CENTER)
    osb.text('genuary', 300, 300)
    osb.end_draw()

def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_x(py5.radians(15))
    py5.translate(-py5.width / 2, -py5.height / 2 - 40, 0)

    py5.no_fill()
    #py5.fill(0)
    py5.stroke(255)    
    num = 60
    s = py5.width / num 
    for fila in range(num):
        for coluna in range(-20, num + 20):  # 0, 1, ... 9
            x = int(coluna * s)
            y = int(fila * s)
            z = 0
            if osb.get_pixels(x, y) != py5.color(255):
                caixa(x, y, z, s)

def key_pressed():
    py5.save_frame('out.png')

def caixa(x, y, z, s):
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(s)
        
py5.run_sketch(block=False)

