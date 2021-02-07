# adapted from
# https://discourse.processing.org/t/text-reveal-along-a-path/1705/9

message = ("Lorem ipsum dolor sit amet,"
         + "consectetur adipiscing elit.")
charCount = len(message)
charCountToStep = 1.0 / float(charCount)

def setup():
    size(800, 800)
    smooth(8)
    randomizePoints()
    textSize(32)
    textAlign(CENTER, CENTER)
    textMode(MODEL)
    fonte = createFont("Tomorrow Light",52)
    textFont(fonte)

def draw():
    background(100)
    noFill()
    # stroke(0xff007fff)
    # bezier(ap0x, ap0y, 
    #     cp0x, cp0y, 
    #     cp1x, cp1y, 
    #     ap1x, ap1y)
    noStroke()
    fill(255)
    
    step0 = frameCount * 0.003
    
    for i in range(charCount):
        step1 = i * charCountToStep
        step2 = (step0 + step1) % 1.0
        
        x = bezierPoint(ap0x, cp0x, cp1x, ap1x, step2)
        y = bezierPoint(ap0y, cp0y, cp1y, ap1y, step2)
        
        tanx = bezierTangent(ap0x, cp0x, cp1x, ap1x, step2)
        tany = bezierTangent(ap0y, cp0y, cp1y, ap1y, step2)
        
        angle = atan2(tany, tanx)

        pushMatrix()
        translate(x, y)
        rotate(angle)
        text(message[i], 0.0, 0.0)
        popMatrix()

def mouseReleased():
    randomizePoints()

def randomizePoints():
    global halfw, halfh, ap0x, cp0x, cp1x, ap1x, ap0y, cp0y, cp1y, ap1y
    halfw = width * 0.5
    halfh = height * 0.5
    ap0x = random(0.0, halfw)
    cp0x = random(0.0, width)
    cp1x = random(0.0, width)
    ap1x = random(halfw, width)

    ap0y = random(0.0, halfh)
    cp0y = random(0.0, height)
    cp1y = random(0.0, height)
    ap1y = random(halfh, height)
