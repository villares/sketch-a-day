# Other L-System

count = 0
iterations = 8
stroke_len = 1100
angle_deg = 135
axiom = 'L'
sentence = axiom
rules = {
    'L': '+RF[-LFL]+',
    'R': '[-LF]+RFR-',
}

def setup():
    size(600, 600)
    global xo, yo, png
    png = createGraphics(width * 5, height * 5)
    xo, yo = 160, 460  # width / 2, height / 2 - 20
    generate(iterations)

def draw():
    beginRecord(png)
    smooth(4)
    noFill()
    colorMode(HSB)
    png.scale(5)
    strokeWeight(.2)
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))
    endRecord()

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence

def plot(angle):
    s = 0
    for i, c in enumerate(sentence):
        stroke(s % 256, 255, 255)
        if c == 'F':
            # stroke(255)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == '+':
            rotate(angle)
            s += 5
        elif c == '-':
            rotate(-angle)
            s -= 5
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()
        elif c == 'L':
            circle(0, 0, stroke_len / 10.0)
        elif c == 'R':
            circle(0, 0, stroke_len / 5.0)

def keyPressed():
    # global count
    # count += 1
    # png.save('{:0>4}.png'.format(count))
    # print count
    global angle_deg, xo, yo, stroke_len, iterations, sentence
    if key == '-':
        angle_deg -= 1.
        print("angle:" + str(angle_deg))
    if str(key) in "=+":
        angle_deg += 1
        print("angle:" + str(angle_deg))
    if key == 's':
        global count
        count += 1
        png.save('{}-{}.png'.format(angle_deg, iterations))
        print count
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
    print(xo, yo, stroke_len)
