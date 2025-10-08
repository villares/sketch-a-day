import py5

axiom = "X"
rules = {"X": "F+[[X]-X]-F[-FX]+X",
          "F": "FF"
          }

step = 10
angle = 25
iterations = 4  # repeticoes (voltas na aplicação das regraas)
xo, yo = 300, 500

def setup():
    py5.size(600, 600)
    generate(axiom, rules)

def generate(axiom, rules):
    global sequence
    starting_sequence = axiom
    for i in range(iterations):
        sequence = ""
        for symbol in starting_sequence:
            sequence += rules.get(symbol, symbol)
        starting_sequence = sequence
    print(len(sequence))

def draw():
    py5.background(240, 240, 250)
    py5.translate(xo, yo)
    try:
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
    except Exception as e:
        print(e)

def key_pressed():
    if py5.key == ' ':
        rules['X'] = ''.join(py5.random_permutation(rules['X']))
        generate(axiom, rules)
    elif py5.key == 's':
        py5.save_frame(f'{rules["X"]}.png')

py5.run_sketch(block=False)