"""

"""

maxFrameCount = 200.0  # needs to be a float
a = 106
SIZE = 60

def setup():
    size(540, 540, P2D)
    stroke(255, 200, 0)
    frameRate(10)

def draw():
    global theta
    background(0)
    #fill(0, 100)
    #rect(0, 0, width, height)
    with pushMatrix():
        translate(width / 2, height / 2)
        t = frameCount / maxFrameCount
        theta = TWO_PI * t
        for x in range(-250, 251, 50):
            for y in range(-250, 251, 50):
                offSet = (x + y) * a
                sz2 = map(sin(-theta + offSet), -1, 1, 0, 35)
                strokeWeight(2)
                if (x + y) % 100 == 0:
                    fill(0, 200, 100, 100)
                    circ(x, y, 10, sz2)
                else:
                    fill(0, 128, 255, 100)
                    circ(x, y, 10, sz2)

def circ(x, y, rot1, rot2):
    with pushMatrix():
        translate(x, y)
        rotate(rot2) # + float(frameCount / 7))
        s = sin(rot2 + theta) # + float(frameCount / 11))
        ellipse(0, 0, SIZE, SIZE * s)
