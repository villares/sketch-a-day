# Other L-System

iterations = 10
base_len = 350
angle_deg = 45
axiom = 'L'
sentence = axiom
rules = {
    'L': '-RF[-L]',
    'R': '+LF[+R]',
}

def setup():
    size(700, 700)
    global xo, yo
    xo, yo = width / 2, height / 2 - 20
    strokeWeight(0.5)
    noFill()
    generate(iterations)

def draw():
    background(0)
    translate(xo, yo)
    record_limits(reset=True)        
    plot(radians(angle_deg))
    resetMatrix()
    fill(0, 200); noStroke()
    rect(0, height - 80, width, 80)
    fill(255)
    t = "rules = {} axiom: '{}'\niterations:{} angle:{} stroke-len:{} sentence len: {}"
    t = t.format(rules, axiom, iterations, angle_deg, int(stroke_len), len(sentence))
    textSize(20)
    text(t, 10, height - 50)

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        # stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence
    stroke_len = base_len * 2. / sqrt(len(sentence) + iterations + 10) 
        
def plot(angle):
    for c in sentence:
        if c == 'F':
            stroke(255)
            line(0, 0, 0, -stroke_len) # draw white line
            translate(0, -stroke_len) # move
        elif c == 'L':
            stroke(255, 0, 0)
            noFill()
            circle(0, 0, stroke_len / 10) # red does not move!
        elif c == 'R':
            stroke(0, 0, 255)
            circle(0, 0, stroke_len / 10) # blue does not move! 
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()
    record_limits()        
            
def record_limits(reset=None):
    global max_x, max_y, min_x, min_y
    if reset is None:
        x = screenX(0, 0)
        y = screenY(0, 0)
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)
    else:
        max_x = min_x = max_y = min_y = 0


def keyPressed():
    global angle_deg, xo, yo, stroke_len, iterations, sentence
    print(max_x, max_y, min_x, min_y)
    if key == '-':
        angle_deg -= 1.
    if str(key) in "=+":
        angle_deg += 1
    if key == 's':
        saveFrame('angle{}-{}.png'.format(angle_deg, iterations))
    if key == '.':
        iterations += 1
        sentence = axiom
        generate(iterations)
    if key == ',':
        iterations -= 1
        sentence = axiom
        generate(iterations)
    if key == 'a':
        stroke_len *= 1.1
    if key == 'z':
        stroke_len /= 1.1
    if keyCode == LEFT:
        xo -= 50
    if keyCode == RIGHT:
        xo += 50
    if keyCode == UP:
        yo -= 50
    if keyCode == DOWN:
        yo += 50
        
        
def settings():
    """ print markdown to add at the sketc-a-day page"""
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
