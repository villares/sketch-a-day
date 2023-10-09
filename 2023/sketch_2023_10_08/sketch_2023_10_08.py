from villares.helpers import save_png_with_src

l_system = {
    'axiom': 'X',
    'rules': {
        'X': '[F-[FX+FX]]B[F+[FX-FX]]',
        'F': 'FF',
    },
    'step': 3.5,
    'angle': 60,  # degrees
    'iter_num': 6,
}
def setup():
    global resulting_string
    size(800, 800)
    initial_string = l_system['axiom']
    rules = l_system['rules']
    for _ in range(l_system['iter_num']):
        resulting_string = ''
        for symbol in initial_string:
            substituir = rules.get(symbol, symbol)
            resulting_string = resulting_string + substituir
        # print(initial_string, resulting_string)
        initial_string = resulting_string
    print(len(resulting_string))

def draw():
    background(240, 240, 220)
    stroke_weight(3)
    angle = l_system['angle']
    step = l_system['step']
    translate(width / 2, height * 0.9)
    ca = 0
    for i, symbol in enumerate(resulting_string):
        if symbol == 'X':   
            pass
        elif symbol == 'F': 
            stroke(0, ca % 255, 128)
            line(0, 0, 0, -step)
            translate(0, -step)
        elif symbol == 'B':
            no_stroke()
            fill(0, 0, 100)
            circle(0, 0, step)
        elif symbol == '+':
            rotate(radians(-angle)) #+ random(-5, 5)))
            ca -= angle
        elif symbol == '-':
            rotate(radians(+angle)) #+ random(-5, 5)))
            ca += angle
        elif symbol == '[':
            push_matrix()
        elif symbol == ']':
            pop_matrix()
            
def key_pressed():
    save_png_with_src(context=str(l_system))   # f'{__file__[:-3]}.png')
