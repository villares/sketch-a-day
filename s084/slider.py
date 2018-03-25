class Slider:
    def __init__(self,low,high,default):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        
    def position(self,x,y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        #the position of the rect you slide:
        self.rectx = self.x + map(self.val,self.low,self.high,0,120)
        self.recty = self.y - 10
        
    def value(self):
        '''updates the slider and returns value'''
        #gray line behind slider

        fill(0)
        rect(self.x,self.y-10,120, 20)
        strokeWeight(4)
        stroke(200)
        line(self.x,self.y,self.x + 120,self.y)
        #press mouse to move slider
        if mousePressed and dist(mouseX,mouseY,self.rectx,self.recty) < 20:
            self.rectx = mouseX
        #constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        #draw rectangle
        strokeWeight(1)
        stroke(0)
        fill(self.val, 200, 200)
        rect(self.rectx,self.recty,10,20)
        self.val = map(self.rectx,self.x,self.x + 120,self.low,self.high)
        #draw label
        fill(0)
        textSize(10)
        text(int(self.val),self.rectx,self.recty + 35)
        return self.val