import py5
import py5_tools

black = py5.color(0)
white = py5.color(255)

def setup():
    global img
    py5.size(600, 600, py5.P3D)
    img = py5.load_image('auto.jpg')


def draw():
    py5.background(black)
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_x(py5.radians(15))
    py5.translate(-py5.width / 2, -py5.height / 2 - 40, 0)

    py5.no_fill()
    #py5.fill(0)
    py5.stroke(255)    
    num = 50
    s = py5.width / num
    for fila in range(num):
        for coluna in range(-20, num + 20):  # 0, 1, ... 9
            x = int(coluna * s)
            y = int(fila * s)
            z = 0
            px = img.get_pixels(int(x / 1.5), int(y / 1.5))
            b = py5.brightness(px) / 255 * s
            caixa(x, y, z, b)

def key_pressed():
    py5.save_frame('out.png')

def caixa(x, y, z, s):
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(s)
        
py5.run_sketch(block=False)

