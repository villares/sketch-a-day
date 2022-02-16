from random import sample, seed, shuffle, choice
# add_library('video')    # import processing.video.*
# add_library('opencv_processing') # import gab.opencv.*

from particles import ParticleSystem
debug = False
gravity = 0.20

mode = 0
nodes = {}
node_list = []
step = 20
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = []
play = False


def setup():
    size(640, 480)
    print(width, height)
    strokeWeight(5)
    setup_seed(14220)
    start_nodes()
    create_system()
            
def start_nodes(mode=0):
    global w, h
    w = width // step // 2
    h = height // step // 2
    nodes.clear()
    if mode == 0:
        nodes.update({(int(random(-w, w)), h): None for _ in range(10)})
    elif mode == 2 or mode == 3:
        nodes.update({(int(random(-w, w)), int(random(-h, h))): None for _ in range(5)}) 
    node_list[:] = list(nodes.keys())
            
def draw():
    background(0)
    translate(width / 2, height / 2)    
    a = 255
    if mode == 0:
        if play: grow()
    if mode == 1:
        drop_nodes(speed=50, from_start=True)
    if mode == 2:
        a = max(0, 255 - len(nodes)/10.0)
        if play and frameCount % 10 == 0: grow()
    if mode == 3:
        if play and frameCount % 10 == 0: grow()        
    if mode == 4:
        drop_nodes(speed=30)
    if mode in (0, 1, 2, 3, 4, 5):
        draw_nodes(a)        
    if mode == 5 or mode == 6:
        push()
        translate(-width / 2, -height /2)
        particles.run(PVector(random(-1, 1), random(-1, 1)))   
        pop()
    if mode == 6:
        drop_nodes(speed=5)
    
def drop_nodes(speed, from_start=False):
    for _ in range(speed):
        if node_list:
            if from_start:
                n = node_list.pop(0)
            else:
                n = node_list.pop()
            nodes.pop(n)
                
def draw_nodes(a=255):
    for n, v in nodes.items():
        xa, ya = n
        if v:
            xb, yb, c = v
        else:
            continue
        stroke(c, a)
        line(xa * step, ya * step, xb * step, yb * step)
        if dist(mouseX - width / 2, mouseY - height / 2, xa * step, ya * step) < 5:
            text(str((xa, ya)), xa * step, ya * step)
            
def grow():    
    global nbs
    # i = len(nodes) % 5
    nbs_a = sample(NBS, 2)
    nbs_b = sample(NBS, 6)
    nbs[:] = nbs_a, nbs_b 
    nks = nodes.keys()
    #nks.sort()  # hmmm. not that nice
    shuffle(nks)
    for i, (x, y) in enumerate(nodes.keys()):
        colorMode(RGB)
        c = color(0, 255 - i % 128, i * 16 % 255)
        nbs_y = choice((nbs[1], nbs[0])) #if y > 0 else nbs[1]
        for nx, ny in nbs_y:
            xnx, yny = x + nx, y + ny
            visible = dist(0, 0, xnx, yny) < w * 0.66
            if visible and (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c)
                node_list.append((xnx, yny))
    
def setup_seed(s=None):
    global random_seed
    if s is None:
        random_seed = int(random(100000))
    else:
        random_seed = s
    seed(random_seed)       # Python's random
    randomSeed(random_seed) # Processing's random
   # print(random_seed)
    

    
def create_system():
    global particles
    colorMode(HSB)
    particles = ParticleSystem(PVector(width / 2, 50))
    for _ in range(15):
        particles.addParticle(PVector(random(width), random(height)))

def captureEvent(c):
    if debug:
        print(frameCount, frameRate)
    c.read()


def keyPressed():
    global play, mode, debug
    if str(key) in '0123456789':
        mode = int(key)
    if key == ' ':
        play = not play
        print(play)
    elif key == '0':
        setup_seed()
        start_nodes(mode)
        play = True
    elif key == '1':
        play = False
    elif key == '2' or key == '3':
        setup_seed()
        start_nodes(mode)
        play = True    
                
    elif key == 'd':
        debug = not debug
    if key == ENTER:
         create_system()
