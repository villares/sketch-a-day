# add_library('GifAnimation')
# from gif_animation_helper import gif_export

# Other L-System

iterations = 11
base_len = 350
angle_deg = 0
axiom = 'L'
rules = {
    'L': '-RF[-L]',
    'R': '+LF[+R]',
}

def setup():
    size(500, 500)
    global xo, yo
    xo, yo = width / 2, height / 2
    strokeWeight(1)
    noFill()
    generate(iterations)

def draw():
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))
    resetMatrix()
    
    # debug
    # rectMode(CORNERS)
    # rect(min_x, min_y, max_x, max_y)
    # rectMode(CORNER)
    
    # draw text with rules & other infos
    fill(0, 200); noStroke()
    rect(0, height - 80, width, 80)
    fill(255)
    t = "rules = {} axiom: '{}'\niterations:{} ang:{} stroke-len:{} sentence: {}"
    t = t.format(rules, axiom, iterations, angle_deg, int(stroke_len), len(sentence))
    textSize(18)
    text(t, 10, height - 50)

def generate(n):
    """ Main L-System rule application function """
    global stroke_len, sentence
    sentence = axiom
    for _ in range(n):
        # stroke_len *= 0.5  # make stroke_len shorter (old method)
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)  # apply substitution rule from dict
        sentence = next_sentence
    # make stroke_len shorter (new method)
    stroke_len = base_len * 2. / sqrt(len(sentence) + iterations + 10) 
        
def plot(angle):
    """ Draw sentence - 'drawing rules' """
    record_limits(reset=True)  # init zoom limits       
    for c in sentence:
        if c == 'F':
            stroke(255)
            line(0, 0, 0, -stroke_len) # draw white line
            translate(0, -stroke_len) # move
        elif c == 'L':
            stroke(255, 0, 0)
            noFill()
            line(0, 0, 0, -stroke_len / 3) # red does not move!
        elif c == 'R':
            stroke(0, 0, 255)
            line(0, 0, 0, -stroke_len / 3) # blue does not move! 
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
        # circle(0, 0, 15)
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)
    else:
        max_x = min_x = screenX(0, 0)
        max_y = min_y = screenY(0, 0)


def keyPressed():
    global angle_deg, xo, yo, stroke_len, iterations
    if key == '-':
        angle_deg -= 1.
    if str(key) in "=+":
        angle_deg += 1
    if key == 's':
        gif_export(GifMaker, "animation")
        # saveFrame('angle{}-{}.png'.format(angle_deg, iterations))
    if key == 'q':
        gif_export(GifMaker, "animation", finish=True)
    if key == '.':
        iterations += 1
        generate(iterations)
    if key == ',':
        iterations -= 1
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
    if key == ' ':
        # print(max_x, max_y, min_x, min_y)
        dx = max_x - min_x
        dy = max_y - min_y
        if dx > width - 25 or dy > height - 25:
            print(dx, dy)
            stroke_len /= 1.1
        else:
            if max_x > width:
                xo -= 25
            elif min_x < 0:
                xo += 25
            if max_y > height:
                yo -= 25
            elif min_y < 0:
                yo += 25
            
        
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
