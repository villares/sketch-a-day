s_size = 100
COLORS = [color(200, 255, 0),
          color(200, 0, 0),
          color(0, 0, 255),
          ]

def setup():
    size(400, 400)
    blendMode(ADD) # DIFFERENCE # ECVLUSION
    rectMode(CENTER)
    init()
    
def init():
    global origin, target
    origin = []
    target = []
    for _ in COLORS:
        origin.append((width / 2, height / 2))
        target.append((random(s_size, width - s_size),
                       random(s_size, height - s_size)))

def draw():
    background(0)
    noFill()
    strokeWeight(5)
    t = .5 - cos(radians(frameCount % 360)) / 2. #map(mouseX, 0, width, 0, 1)
    for i, cor in enumerate(COLORS):
        stroke(cor)
        x, y = lerp_sequence(origin[i], target[i], t)    
        square(x, y, s_size) 
    if frameCount % 360 == 0:
        init()
    
def lerp_sequence(a, b, t):
    c = []
    for c_a, c_b in zip(a, b):
         c.append(lerp(c_a, c_b, t))
    return c
    
def keyPressed():
    init()
