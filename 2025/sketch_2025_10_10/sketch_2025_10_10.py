import py5
import py5_tools

axiom = "F"
rules = {"F": "F[+F-F0]-F+[-F+F0]"}

step = 4
angle = 22.5
iterations = 4  # repeticoes (voltas na aplicação das regraas)
xo, yo = 50, 90
seqs = []

def setup():
    py5.size(800, 800, py5.P3D)
    #py5.no_smooth()
    py5.stroke_weight(0.5)
    py5.text_align(py5.CENTER, py5.TOP)
    py5.text_size(12)
    py5.fill(100, 100, 255)
    py5.color_mode(py5.HSB)
    py5.random_seed(1)
    generate_all()
    py5_tools.animated_gif('out.gif', frame_numbers=range(1, 46), duration=0.3)

def generate_all():
    seqs.clear()
    for k in range(64):
        rules = new_rules()
        seqs.append(generate())
        
def generate():
    starting_sequence = axiom
    for i in range(iterations):
        sequence = ""
        for symbol in starting_sequence:
            sequence += rules.get(symbol, symbol)
        starting_sequence = sequence
    return sequence

def draw():
    py5.background(240)
    k = 0
    for i in range(8):
        x = i * 100
        for j in range(8):
            y = j * 100
            py5.text(rules['F'], x + xo, y + yo)
            draw_sequence(seqs[k], x + xo, y + yo)
            k += 1
            
def draw_sequence(sequence, x, y):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate_y(py5.radians(py5.frame_count * 8))
        for i, symbol in enumerate(sequence):
            if symbol == "F":
                py5.rotate_y(py5.radians(angle))
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
            if symbol == '0':
                with py5.push_style():
                    py5.fill(i % 255, 200, 200)
                    py5.no_stroke()
                    py5.circle(0, 0, step / 2)

def key_pressed():
    if py5.key == ' ':
        generate_all()
    elif py5.key == 's':
        py5.save_frame(f'###.png')
        
def new_rules():
    while True:
        new_rule = ''.join(py5.random_permutation(rules['F']))
        if check_rule(new_rule):
            rules['F'] = new_rule
            break        
    return rules
        
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