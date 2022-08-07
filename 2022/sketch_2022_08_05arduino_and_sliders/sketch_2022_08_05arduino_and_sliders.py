import py5

"""
Based on sketch s115 from 2018
"""
from inputs import InputInterface

def setup():
    global input_interface
    py5.size(600, 600)
    py5.no_fill()  # sem preenchimento
    py5.frame_rate(30)
    py5.stroke_weight(3)
    py5.color_mode(py5.HSB)
    # Ask user for Arduino port, uses slider if none is selected`
    input_interface = InputInterface()


def draw():
    py5.background(200, 150, 100)  # fundo escuro
    elements = []
    # 0 a 63 linhas e colunas na grade
    grid_elem = int(input_interface.analog_read(1) / 16)
    # 0 a 63 tamanho base dos quadrados
    elem_size = int(input_interface.analog_read(2) / 16)
    # escala a randomização do tamanho
    rand_size = int(input_interface.analog_read(3) / 16)
    # escala a randomização da posição
    rand_posi = int(input_interface.analog_read(4) / 16)
    # trava a random entre os ciclos de draw
    # mas varia com o número de colunas na grade
    py5.random_seed(int(input_interface.analog_read(1) / 4))
    # espaçamento entre os elementos
    spac_size = py5.width / (grid_elem + 1)
    v = spac_size * 1.5
    h = spac_size * py5.sqrt(3)
    for ix in range(-1, grid_elem + 1):
        for iy in range(-1, grid_elem + 1):
            if iy % 2:
                x = ix * h + h / 4
            else:
                x = ix * h - h / 4
            if ix % 2:
                es = elem_size
            else:
                es = -elem_size
            y = iy * v
            for i in range(2):
                final_size = es * (i + 0.5)
                C = py5.color(py5.remap(final_size, -100, 100, 0, 255),
                              255, 255, 100)
                o_x = rand_posi * py5.random(-1, 1)
                o_y = rand_posi * py5.random(-1, 1)
                elements.append((C, x + o_x, y + o_y, final_size))
    # three layers of elements
    for e0, e1 in zip(elements[0::2], elements[1::2]):
        st0, x0, y0, es0 = e0
        st1, x1, y1, es1 = e1
        fs0 = es0 + rand_size * py5.random(-1, 1)
        fs1 = es1 + rand_size * py5.random(-1, 1)
        for i in range(5):
            x, y = py5.lerp(x0, x1, .25 * i), py5.lerp(y0, y1, .25 * i)
            fs = py5.lerp(fs0, fs1, .25 * i)
            st = py5.lerp(128, 255, .25 * i)
            with py5.push_matrix():
                py5.translate(x, y)
                py5.rotate(fs)
                py5.stroke(st)
                hexagon(0, 0, fs)

    input_interface.update()


def hexagon(x, y, r):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.begin_shape()
        for i in range(6):
            sx = py5.cos(i * py5.TWO_PI / 6) * r
            sy = py5.sin(i * py5.TWO_PI / 6) * r
            py5.vertex(sx, sy)
        py5.end_shape(py5.CLOSE)

def key_pressed():
    if py5.key == 'p':
        py5.save_frame("hexgrid-s115-####.png")
    if py5.key == 'h':
        input_interface.help()

    input_interface.key_pressed()


def key_released():
    input_interface.key_released()


py5.run_sketch()



