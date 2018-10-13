from random import choice
from random import randint

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - height / 2
        self.size_ = 1
        self.rot0 = randint(1, 4)
        self.rot1 = randint(1, 2) + x
                                
    def plot(self, adv):
        """ draws node """
        with pushMatrix():
            translate(self.x, self.y)
            r = map(adv, 0, 1, self.rot0, self.rot1)
            rotate(r * HALF_PI)
            siz = Node.spacing * self.size_
            mid = siz/2
            strokeWeight(2)
            noFill() #stroke(0)
            stroke(0, 0, 200, 50)
            rect(0, 0, siz, siz)
            strokeWeight(2)
            stroke(100, 100, 000)
            arc(-siz/2, -siz/2, mid, mid, 0, HALF_PI)
            arc(-siz/2, -siz/2, siz+mid, siz, 0, HALF_PI)
            arc(-siz/2, -siz/2, siz, siz+mid, 0, HALF_PI)
            arc(siz/2, siz/2, siz+mid, siz+mid,PI, PI+HALF_PI)
            arc(siz/2, siz/2, mid, siz,PI, PI+HALF_PI)
            arc(siz/2, siz/2, siz, mid,PI, PI+HALF_PI)
            # if dist(mouseX - width/2, mouseY- height/2, 0, 0) < siz:
            # text("{:.2f}".format(r),0, 0)

    @classmethod                                            
    def init_grid(cls, grid_size, border):
        cls.border = border
        cls.spacing = (width - cls.border * 2) / grid_size
        cls.nodes = []
        for x in range(grid_size):
            for y in range(grid_size):
                    new_node = cls(x, y)
                    cls.nodes.append(new_node)

    
            
