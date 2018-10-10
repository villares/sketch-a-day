from random import choice

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - height / 2
        self.size_ = 1
        self.cor = color(0, 0, 200)
        self.rot = choice((0, HALF_PI, PI, PI + HALF_PI))
        
    def plot(self, ang):
        """ draws node """
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot + ang)
            noFill() #stroke(0)
            stroke(self.cor)
            siz = Node.spacing * self.size_
            rect(0, 0, siz, siz)
            line(-siz/2, -siz/2, siz/2, siz/2)

            
