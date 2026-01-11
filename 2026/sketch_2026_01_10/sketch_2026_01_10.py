import py5

STEP = 50
nodes = {(0, 0): (0, 0)}
unvisited = [(0, 0)]

def setup():
    py5.size(800, 800)
    py5.stroke(255, 100)
    start()
    
def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    for (aA, dA), (aB, dB) in nodes.items():
        polar_line(aA, dA, aB, dB)

def polar_line(aA, dA, aB, dB):
    xA = py5.cos(aA) * dA
    yA = py5.sin(aA) * dA
    xB = py5.cos(aB) * dB
    yB = py5.sin(aB) * dB
    py5.line(xA, yA, xB, yB)    

def start():
    new_unvisited = []
    while unvisited:
        aA, dA = unvisited.pop()
        for a_offset in (0, 30):
            aB = aA + py5.radians(a_offset + py5.random(-5, 5))
            dB = dA + STEP + py5.random(-25, 25)
            nodes[aB, dB] = (aA, dA)
            new_unvisited.append((aB, dB))
    unvisited[:] = new_unvisited
    print(len(unvisited))
    
def key_pressed():
    if py5.key == ' ':
        start()
    else:
        py5.save_frame(f'###.png')

py5.run_sketch(block=False)