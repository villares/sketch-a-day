"""
L-System

Code for py5 (py5coding.org) imported mode
"""

axiom = 'X'
rules = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
    }
step = 10
ang = 2 / (sqrt(5) + 1)
iterations = 5

def setup():
    global result
    size(900, 900, P3D)
    starting_string = axiom
    for _ in range(iterations):
        result = ''
        for symbol in starting_string:
            result = result + rules.get(symbol, symbol)
        starting_string = result
    print(len(result))

def draw():
    background(210, 210, 150)
    translate(width / 2, height * 0.95)
    rotate_y(radians(frame_count * 2.0))
    for symbol in result:
        if symbol == 'X': 
            no_stroke()
            fill(200, 0, 0)
            circle(0, 0, 10)
        elif symbol == 'F':
            stroke_weight(3)
            stroke(0)
            line(0, 0, 0, -step)
            translate(0, -step)
            rotate_y(ang)
        elif symbol == '+':
            rotate(-ang)
        elif symbol == '-':
            rotate(+ang)
        elif symbol == '[':
            push_matrix()
        elif symbol == ']':
            pop_matrix()
            
    if frame_count <= 180 and frame_count % 5 == 0:
        save_frame('###.png')