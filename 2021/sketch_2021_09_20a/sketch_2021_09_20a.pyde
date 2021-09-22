axiom = 'X'
rules = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'S',  
    'S': 'SF'    
    }
step = 15
angle = 25 # angle in degrees
iterations = 5

def setup():
    global result
    size(600, 600, P3D)
    strokeWeight(2)
    starting_phrase = axiom
    for _ in range(iterations):
        result = ''
        for symbol in starting_phrase:
            replacement = rules.get(symbol, symbol)
            result = result + replacement
        #print(starting_phrase, result)
        starting_phrase = result    
    print(len(result))
    
def draw():
    background(200, 200, 150)
    translate(width / 2, height * 0.90)
    # translate(0, height * 0.45)  # 3d in p5js starts centered
    rotateY(frameCount / 50.0)
    for symbol in result:
        if symbol == 'X':   # se symbol for igual a 'X'
            pass
        elif symbol in 'FS':   # else if 
                line(0, 0, 0, -step)
                translate(0, -step)
                rotateY(radians(-angle))
        elif symbol == '+':
            rotate(radians(-angle)) # + random(-5, 5)))
        elif symbol == '-':
            rotate(radians(+angle)) # + random(-5, 5)))
        elif symbol == '[':
            pushMatrix()
        elif symbol == ']':
            popMatrix()
