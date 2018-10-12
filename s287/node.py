from random import choice

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - height / 2
        self.size_ = 1
        self.rot0 = choice((0,-HALF_PI, -PI))
        self.rot1 = choice((0, HALF_PI , PI, PI + HALF_PI))
        self.rot2 = self.rot0    
                        
    def plot(self, ang):
        """ draws node """
        inc = 1/31.
        with pushMatrix():
            translate(self.x, self.y)
            if abs(self.rot0 - self.rot1) > inc:
                self.rot0 += inc
            else:
               self.rot0 = self.rot1
            rotate(self.rot0)

            siz = Node.spacing * self.size_
            fill(200) 
            noStroke()
            rect(0, 0, siz, siz)            
            stroke(0, 100, 100)
            fill(0, 200, 100, 200)
            arc(siz/2, siz/2, siz/3*4, siz/3*4, PI, PI+HALF_PI)
            fill(200)
            arc(siz/2, siz/2, siz/3*2, siz/3*2, PI, PI+HALF_PI)
            fill(0, 200, 100, 200)
            arc(0, -siz/2, siz/3, siz/3, 0, PI)
            arc(-siz/2, 0, siz/3, siz/3, -HALF_PI, PI-HALF_PI)
            noFill()
            stroke(0, 0, 200)
            rect(0, 0, siz, siz)    

    @classmethod                                            
    def init_grid(cls, grid_size, border):
        cls.border = border
        cls.spacing = (width - cls.border * 2) / grid_size
        cls.nodes = []
        for x in range(grid_size):
            for y in range(grid_size):
                    new_node = cls(x, y)
                    cls.nodes.append(new_node)

    
            
