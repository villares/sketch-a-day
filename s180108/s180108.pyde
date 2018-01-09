from PlatonicSolids import *

NUM_COLS, NUM_ROWS = 5, 5
NUM_CELLS = NUM_COLS * NUM_ROWS
solids = []
r_x = 0
r_y = 0

def setup():
    global CELL_SIZE
    size(500, 500, P3D)
    CELL_SIZE = width / NUM_COLS
    strokeWeight(5)
    noFill()
    colorMode(HSB)
    for i in range(NUM_CELLS):
        s = PlatonicFactory(int(random(5)))    # Instancia aleatoriamente um dos sólidos 
        c = color(random(256), 200, 200, 128)  # random HSB translucent colors
        s.c = c # Tasca cor no sólido! Só os gerados na Factory tem o método p/ usar
        solids.append(s)

def draw():
    global r_x, r_y
    # translate(-width/2, -height/2) # may need to use with PeasyCam
    r_x += 0.02  # x rotation speed
    r_y += 0.01  # y rotation speed
    background(255)  # clear frame with white
    # lights() # use this if you use filled faces
    for i in range(NUM_CELLS):
        x, y = x_y_from_i(i, NUM_COLS, NUM_ROWS)
        cx, cy = CELL_SIZE / 2 + x * CELL_SIZE, CELL_SIZE / 2 + y * CELL_SIZE
        with pushMatrix():
            d = dist(mouseX, mouseY, cx, cy)
            translate(cx, cy)
            if d < 80:
                rotateX(r_y)
                rotateY(r_x)
            # cuidado, só os sólidos criados pela PlatonicFactory tem .platonic_stroke()
            # tava aprendendo a fazer isso de acrescentar métodos
            # podia ter sido resolvido com stroke(solids[i].c)
            solids[i].platonic_stroke()
            solids[i].create()
    if (frameCount < 200): saveFrame("###.tga")

def x_y_from_i(i, max_x, max_y):
    return i % max_x, (i / max_x) % max_y
