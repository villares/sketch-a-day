import py5

axiom = "X"
rules = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }

step = 3
angle = 25
iterations = 4  # repeticoes (voltas na aplicação das regraas)
xo, yo = 50, 90

def setup():
    py5.size(1000, 1000)
    #py5.no_smooth()
    py5.no_loop()
    py5.stroke_weight(0.5)
    py5.text_align(py5.CENTER, py5.TOP)
    py5.text_size(12)
    py5.fill(100, 100, 255)

def generate(axiom, rules):
    global sequence
    starting_sequence = axiom
    for i in range(iterations):
        sequence = ""
        for symbol in starting_sequence:
            sequence += rules.get(symbol, symbol)
        starting_sequence = sequence

def draw():
    py5.background(255, 255, 240)
    for i in range(10):
        x = i * 100
        for j in range(10):
            y = j * 100
            new_rule()
            py5.text(rules['X'], x + xo, y + yo)
            draw_sequence(x + xo, y + yo)
            
def draw_sequence(x, y):
    with py5.push_matrix():
        py5.translate(x, y)
        for symbol in sequence:
            if symbol == "F":
                py5.line(0, 0, 0, -step)  # desenha uma linha
                py5.translate(0, -step)   # move a origem 
            if symbol == "+":
                py5.rotate(py5.radians(angle)) 
            if symbol == "-":
                py5.rotate(py5.radians(-angle))  
            if symbol == "[":
                py5.push_matrix()  # grava o estado (posição e ângulo)
            if symbol == "]":
                py5.pop_matrix()   # volta ao último estado gravado

def key_pressed():
    if py5.key == ' ':
        py5.redraw()
    elif py5.key == 's':
        py5.save_frame(f'###.png')
        
def new_rule():
    while True:
        new_rule = ''.join(py5.random_permutation(rules['X']))
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


        
    
    
    

py5.run_sketch(block=False)