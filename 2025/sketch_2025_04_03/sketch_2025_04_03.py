import py5

step = 9
axiom = 'F'
rules = {
#    'F': 'F[>+F-F+FO<]-F+[>-F+F-FO<]',
   'F': 'F[+F-F+FO]-F+[-F+F-FO]',

    }
angle = 30
iterations = 4

def setup():
    py5.size(600, 600)
    calculate_sequence()

def calculate_sequence():
    global sequence
    starting_sequence = axiom
    for i in range(iterations):
        sequence = ''
        for symbol in starting_sequence:
            sequence = sequence + rules.get(symbol, symbol)
        starting_sequence = sequence
    print(len(sequence))
    
def draw():
    global angle
    py5.background(0)
    py5.stroke(255, 200)
    py5.translate(py5.width / 6, py5.height - 100)
    
    for symbol in sequence:
        if symbol == 'F':
            py5.line(0, 0, 0, -step)
            py5.translate(0, -step)
        elif symbol == '+':
            py5.rotate(py5.radians(-angle))
        elif symbol == '-':
            py5.rotate(py5.radians(angle))
        elif symbol == '[':
            py5.push_matrix()
        elif symbol == ']':
            py5.pop_matrix()
        elif symbol == 'O':
            with py5.push_style():
                py5.fill(255, 0, 0)
                py5.no_stroke()
                py5.circle(0, 0, step / 2)
#         elif symbol == '>':
#             angle += 5
#         elif symbol == '<':
#             angle -= 5


def key_pressed():
    py5.save_frame('###.png')
            
        
py5.run_sketch(block=False)