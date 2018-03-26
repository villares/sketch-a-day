"""
Slider code based on Peter Farell's htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/
"""

class Slider:

    def __init__(self, low, high, default, more_key, less_key):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.more = more_key
        self.less = less_key

    def position(self, x, y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + map(self.val, self.low, self.high, 0, 120)
        self.recty = self.y - 10

    def value(self):
        '''updates the slider and returns value'''
        pushStyle()
        rectMode(CENTER)
        # black translucid rect behind slider
        fill(0, 100)
        noStroke()
        rect(self.x + 60, self.y, 130, 20)
        # gray line behind slider
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if (self.x < mouseX < self.x + 120 and
                self.y < mouseY < self.y + 20):
            fill(250)
            textSize(10)
            text(str(self.val), self.rectx, self.recty + 35)
            if mousePressed:
                self.rectx = mouseX

        # key usage
        if keyPressed:
            if key == self.more:
                self.rectx += 1
            if key == self.less:
                self.rectx -= 1

        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        # draw rectangle
        strokeWeight(1)
        fill(255)
        rect(self.rectx, self.recty + 10, 10, 20)
        self.val = map(self.rectx, self.x, self.x + 120, self.low, self.high)
        # draw label
        popStyle()
        return self.val
