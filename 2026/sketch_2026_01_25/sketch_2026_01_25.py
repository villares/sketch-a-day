import py5_tools

axiom = 'X'
rules = {
    'X': 'F+[[X0]-FX]-F[[X0]+FX]-X0',
    'F': 'FF',
}
angle = 22.5
step = 8
num_iter = 5

def setup():
    size(800, 800)
    generate_string()
    
def generate_string():
    global result
    starting_string = axiom
    for i in range(num_iter):
        result = ''
        for symbol in starting_string:
            result += rules.get(symbol, symbol)
        starting_string = result
    print(len(result))
    
def draw():
    background(240, 250, 240)
    translate(400, 800)
    for symbol in result:
        if symbol == 'F':
            stroke(0)
            line(0, 0, 0, -step)
            translate(0, -step)
        elif symbol == '-':
            rotate(radians(angle))
        elif symbol == '+':
            rotate(radians(-angle))
        elif symbol == '[':
            push_matrix()
        elif symbol == ']':
            pop_matrix()
        elif symbol == '0':
            no_stroke()
            fill(128, 0, 128)
            circle(0, 0, step * 0.5)
   
def key_pressed():  # esperada pelo framework/biblioteca
    # executada quando alguém aperta uma tecla
    global angle, step, num_iter
    if key == 'a':
        angle += 1
    elif key == 'z':
        angle -= 1
    elif key == 'd':
        num_iter += 1
        generate_string()
        return
    elif key == 'c':
        num_iter -= 1
        generate_string()
        return
    elif key == 's':
        step *=  1.1
    elif key == 'x':
        step /= 1.1
        
    print(f'ângulo: {angle} passo: {step}')
        
   
