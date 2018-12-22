from random import choice
from arcs import quarter_circle, half_circle, circle_arc

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - height / 2
        self.size_ = 1
        self.rot0 = choice((0, HALF_PI)) #, PI, PI + HALF_PI))
        self.rot1 = choice((HALF_PI , PI)) #, PI + HALF_PI))
        self.type = choice(("a", "b"))
        
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
            siz = Node.spacing * self.size_
            l = siz / 2.
            a = l / 2. - 1
            c = l / 2. + 1
            # stroke(0, 0, 200, 50)
            # rect(0, 0, siz, siz)
            for i in range(-4, 5, 4): # (-28, 29, 7):
                stroke(32, 64 + i * 8, 64 - i * 8)
                if self.type == "a":
                    quarter_circle(l, l, c + i, TOP + LEFT)
                    quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)                
                    quarter_circle(-l, l, c + i, TOP + RIGHT)
                    quarter_circle(l, -l, c + i, BOTTOM + LEFT) 
                else: #self.type == "b":
                    half_circle(-l, 0, a - i, RIGHT)
                    half_circle(l, 0, a - i, LEFT)                    
                    half_circle(0, l, a - i, TOP)
                    half_circle(0, -l, a - i, BOTTOM)
                # else:
                #     line(-l, a + i, l, a + i)
                #     line(a + i, -l, a + i, l)
                #     line(-l, -a + i, l, -a + i)
                #     line(-a + i, -l, -a + i, l)
                

    @classmethod                                            
    def init_grid(cls, grid_size, border):
        cls.border = border
        cls.spacing = (width - cls.border * 2) / grid_size
        cls.nodes = []
        for x in range(grid_size):
            for y in range(grid_size):
                    new_node = cls(x, y)
                    cls.nodes.append(new_node)

    
            
