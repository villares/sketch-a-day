"""
Slider code by Peter Farell 
htts://twitter.com/hackingmath
http://farrellpolymath.com/

Get the most recent version here:
https://github.com/hackingmath/python-sliders 
"""
# USAGE:
#>from slider import Slider
#
# Outside the setup function I created the slider object:
#
#>slider1 = Slider(0,20,6)
#
# You have to tell it the range of the slider (in this case 0 to 20)
# and the default value, when the program first runs (in this case, 6).
#
# Inside the setup function you give it a position on the screen:
#
#>slider1.position(20,20)
#
# Finally in the draw function you assign the value of the slider to a variable and work with it interactively. I just wanted to show it was returning and updating the value, so I just printed it out in the console:
#
#>num = slider1.value()
#>println(num)
#

class Slider:

    def __init__(self, low, high, default):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False

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
        stroke(0)
        rect(self.x + 60, self.y, 130, 20)
        # gray line behind slider
        strokeWeight(4)
        stroke(200)
        line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if dist(mouseX, mouseY, self.rectx + 5, self.recty + 10) < 20:
            fill(200)
            textSize(10)
            text(int(self.val), self.rectx, self.recty + 35)
            if mousePressed:
                self.rectx = mouseX
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