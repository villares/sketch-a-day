"""
polígonos recursivos - Alexandre B A Villares
abav.lugaralgum.com/lousa-magica
[Estudo não apresentado] Circuito Sesc de Artes 2018 

tecle 'h' para ajuda...
"""
from inputs import InputInterface

def setup():
    global input_interface
    size(600, 600)
    frame_rate(10)
    color_mode(HSB)  # makes it easy to cycle colors through Hues...
    no_fill()
    # escolhe a porta do Arduino ou reverte para sliders
    input_interface = InputInterface()

def draw():
    background(0)

    ang = remap(input_interface.analog_read(1), 0, 1023, PI / 6, TWO_PI / 3)  # ângulo
    depth_upper_limit = 2 + ang * 1.5  # change J's upper limit...
    dep = remap(input_interface.analog_read(2), 0, 1023, 1, depth_upper_limit)
                                       # 1 to 2 + ang * 1.5
    sat = remap(input_interface.analog_read(3), 0, 1023, 0, 255)  # saturação
    rot = remap(input_interface.analog_read(4), 0, 1023, 0, TWO_PI)  # 0 to TWO_PI # giro

    poly_shape(width / 2, height / 2, ang, dep, sat, rot)

    # Desenha e lê sliders se necessário
    input_interface.update()


def poly_shape(x, y, angle, depth, saturation_, rotation):
    H, S, B, A = (frame_count / 2 * depth) % 256, saturation_, 255, 100
    stroke(H, S, B, A)
    stroke_weight(depth * 10)
    with push_matrix():
        translate(x, y)
        rotate(rotation)
        radius = depth * 40
        # create a polygon on a ps PShape object
        ps = create_shape()
        ps.begin_shape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx, sy)
            a += angle
        ps.end_shape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # Draw the PShape
        if depth > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.get_vertex_count()):
                # for each vertex
                pv = ps.get_vertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, depth - 1, saturation_, rotation)


def key_pressed():
    if key == 'p':
        save_frame("lousa-03-####.png")
    if key == 'h':
        input_interface.help()

    input_interface.key_pressed()


def key_released():
    input_interface.key_released()
