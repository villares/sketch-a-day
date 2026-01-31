from random import sample, seed

axiom = 'X'
rules = {
    'X': 'F[-F[X0]+X0]F[+F[X0]-X0]',
    'F': 'FF',
}

step = 5  
angle = 22.5
iterations = 5  # repeticoes (voltas na aplicação das regraas)

def setup():
    size(900, 900)
    no_loop()
    stroke_weight(0.5)
    text_align(CENTER, TOP)
    text_size(width / 100)
    fill(100, 100, 255)

def generate(axiom, rules):
    global sequence
    starting_sequence = axiom
    for i in range(iterations):
        sequence = ""
        for symbol in starting_sequence:
            sequence += rules.get(symbol, symbol)
        starting_sequence = sequence

def draw():
    background(0)
    stroke(255)
    fill(255)
    s = frame_count
    print(s)
    seed(s)
    N = 8
    W = width
    new_rule()
    text(rules['X'], W / 2, W * 0.95)
    draw_sequence(W / 2, W * 0.95)
    save_frame(f'LSystems-{str(s).zfill(3)}.png')

   
   
def draw_sequence(x, y):
    with push_matrix():
        translate(x, y)
        for symbol in sequence:
            if symbol == "F":
                line(0, 0, 0, -step)  # desenha uma linha
                translate(0, -step)   # move a origem 
            if symbol == "+":
                rotate(radians(angle)) 
            if symbol == "-":
                rotate(radians(-angle))  
            if symbol == "[":
                push_matrix()  # grava o estado (posição e ângulo)
            if symbol == "]":
                pop_matrix()   # volta ao último estado gravado
            if symbol == '0':          
                circle(0, 0, step / 2)

def key_pressed():
    if key == ' ':
        redraw()
        
def new_rule():
    while True:
        new_rule = ''.join(sample(rules['X'], len(rules['X'])))
        if check_rule(new_rule):
            rules['X'] = new_rule
            break        
    generate(axiom, rules)
        
def check_rule(rule):
    push_count = 0
    for symbol in rule:
        if symbol == '[':
            push_count +=1
        elif symbol == ']':
            push_count -=1    
        if push_count < 0:
            return False
    if push_count != 0: # This shouldn't be needed with permutations
        return False    # that always have balanced [s and ]s.
    return True


        
    
    


