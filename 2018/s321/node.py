from random import choice

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - height / 2
        self.size_ = 1
        self.rot0 = choice((0, HALF_PI)) #, PI, PI + HALF_PI))
        self.rot1 = choice((HALF_PI , PI)) #, PI + HALF_PI))
        self.type = choice(("a", "b", "a"))
        
    def plot(self, ang):
        """ draws node """
        with pushMatrix():
            translate(self.x, self.y)
            d = abs(self.rot0 + ang - self.rot1)
            if d >= 0.30:
                rotate(self.rot0 + ang)
            else:
                self.rot0 = self.rot1 - ang
                rotate(self.rot1)    
            noFill() #stroke(0)
            stroke(0, 0, 200, 50)
            siz = Node.spacing * self.size_
            #rect(0, 0, siz, siz)
            # line(-siz/2, -siz/2, siz/2, siz/2)
            stroke(0, 100, 100)
            for i in range(-10,11,10): # (-28, 29, 7):
                if self.type == "a":
                    arc(-siz/2., -siz/2., siz+i, siz+i, 0, HALF_PI)
                    arc(siz/2., siz/2., siz+i, siz+i, PI, PI+HALF_PI)
                else:
                    line(-siz/2., i/2., siz/2., i/2.)
                    line(i/2., -siz/2., i/2., siz/2.)

                

    @classmethod                                            
    def init_grid(cls, grid_size, border):
        cls.border = border
        cls.spacing = (width - cls.border * 2) / grid_size
        cls.nodes = []
        for x in range(grid_size):
            for y in range(grid_size):
                    new_node = cls(x, y)
                    cls.nodes.append(new_node)

    
            