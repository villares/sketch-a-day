import py5

step = 40
axiom = '--F'
rules = {
#    'F': 'F[>+F-F+FO<]-F+[>-F+F-FO<]',
   'F': 'F[+F-F+FO]-F+[-F+F-FO]',

    }
angle = 22.5
iterations = 3
s = 2  # scale factor for exporting


def setup():
    py5.size(1200, 600)
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
    
    out = py5.create_graphics(py5.width * s, py5.height * s)
    py5.begin_record(out)
    out.scale(s)
    global angle
    py5.random_seed(1)
    py5.background(50, 50, 100)
    py5.stroke(200,200, 0)
    py5.stroke_weight(2)
    py5.translate(0, py5.height - step)
    #py5.text_size(step)
    py5.text_font(py5.create_font('Inconsolata Bold', step/2))
    
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
                py5.fill(220, 0, 0)
                py5.no_stroke()
                t = py5.random_choice((1, 0))
                for _ in range(5):
                    py5.rotate(py5.TAU / 5)
                    py5.text(t, 0, -step/8)

    py5.end_record()
    out.save('out.jpg')

        
py5.run_sketch(block=False)