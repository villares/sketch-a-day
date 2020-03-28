# Other L-System

iterations = 8
stroke_len = 2600
angle_deg = 105
axiom = 'L'
sentence = axiom
rules = {
    'L': '+RF-LFL+',
    'R': '-LF+RFR-',
}

def setup():
    size(700, 700)
    global xo, yo
    xo, yo = width / 2, height / 2 - 20
    strokeWeight(0.2)
    noFill()
    generate(iterations)

def draw():
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence

def plot(angle):
    for c in sentence:
        if c == 'F':
            stroke(255)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()

def keyPressed():
    global angle_deg, xo, yo, stroke_len, iterations, sentence
    if key == '-':
        angle_deg -= 1.
        print("angle:" + str(angle_deg))
    if str(key) in "=+":
        angle_deg += 1
        print("angle:" + str(angle_deg))
    if key == 's':
        saveFrame('angle{}-{}.png'.format(angle_deg, iterations))
    if key == '.':
        iterations += 1
        sentence = axiom
        generate(iterations)
        print("iterations:" + str(iterations))
    if key == ',':
        iterations -= 1
        sentence = axiom
        generate(iterations)
        print("iterations:" + str(iterations))
    if key == 'x':
        stroke_len *= 1.5
    if key == 'z':
        stroke_len /= 1.5
    if keyCode == LEFT:
        xo -= 50
    if keyCode == RIGHT:
        xo += 50
    if keyCode == UP:
        yo -= 50
    if keyCode == DOWN:
        yo += 50
