# size(2020, 950, PDF, 'out.pdf')

# An L-System made with Python and py5 <py5coding.org>

size(950, 950)
background(255)
stroke(0)
stroke_weight(2)

step = 40
axiom = 'F'
rules = {'F': 'F[+F-F0]-F[-F+F0]'}
angle = 15
iterations = 4

starting_sequence = axiom
for i in range(iterations):
    sequence = ''
    for symbol in starting_sequence:
        sequence = sequence + rules.get(symbol, symbol)
    starting_sequence = sequence
    
translate(width * 0.3, height * 0.5)
for symbol in sequence:
    if symbol == 'F':
        line(0, 0, 0, -step)
        translate(0, -step)
    elif symbol == '+':
        rotate(radians(-angle))
    elif symbol == '-':
        rotate(radians(angle))
    elif symbol == '[':
        push_matrix()
    elif symbol == ']':
        pop_matrix()
    elif symbol == '0':
        with push_style():
            fill(255, 0, 0)
            no_stroke()
            circle(0, 0, step / 5)

save('out.png')
#exit_sketch()
