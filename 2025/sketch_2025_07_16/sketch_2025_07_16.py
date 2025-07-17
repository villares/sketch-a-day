# An L-System made with Python and py5 in static/imported mode style
# Learn more at https://py5coding.org/content/py5_modes.html
from py5_tools import animated_gif

step = 45
axiom = 'F'
rules = {'F': 'F[+>F-<F0][-<F-<F0]'}
angle = 22.5
iterations = 5

def setup():
    global sequence
    size(950, 950, P3D)
    sphere_detail(3)
    stroke(0)
    stroke_weight(2)
    animated_gif('out.gif', duration=0.1, frame_numbers=range(1, 361, 10))

    starting_sequence = axiom
    for i in range(iterations):
        sequence = ''
        for symbol in starting_sequence:
            sequence = sequence + rules.get(symbol, symbol)
        starting_sequence = sequence

def draw():
    background(255)
    translate(width * 0.5, height * 0.7)
    rotate_y(radians(frame_count))
    for symbol in sequence:
        if symbol == 'F':
            line(0, 0, 0, -step)
            translate(0, -step)
        elif symbol == '+':
            rotate(radians(-angle))
        elif symbol == '-':
            rotate(radians(angle))
        elif symbol == '>':
            rotate_y(radians(-angle))
        elif symbol == '<':
            rotate_y(radians(angle))
        elif symbol == '[':
            push_matrix()
        elif symbol == ']':
            pop_matrix()
        elif symbol == '0':
            with push():
                fill(255, 0, 0)
                no_stroke()
                sphere(step / 10)

def key_pressed():
    save('out.png')
