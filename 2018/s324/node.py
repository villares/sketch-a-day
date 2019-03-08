from random import choice
from arcs import quarter_circle, half_circle, circle_arc

class Node():
    nodes = []
 
    def __init__(self, x, y):
        self.x = Node.border + Node.spacing / 2. + x * Node.spacing - width / 2.
        self.y = Node.border + Node.spacing / 2. + y * Node.spacing - height / 2.
        self.size_ = 1
        self.rot0 = choice((0, HALF_PI)) #, PI, PI + HALF_PI))
        self.rot1 = choice((HALF_PI , PI)) #, PI + HALF_PI))
        self.type = choice(("a", "c", "b", "c", "d", "d", "e" ))
        
    def plot(self, ang):
        """ draws node """
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.rot1)    
            noFill() #stroke(0)
            siz = Node.spacing * self.size_
            t = 5 * cos(ang)
            l = siz / 2.
            a = l / 2. - t 
            c = l / 2. + t
            # stroke(0, 0, 200, 50)
            # rect(0, 0, siz, siz)
            stroke(0, 50, 100)
            for i in range(-4, 5, 4): # (-28, 29, 7):
                stroke((frameCount +  i * 8) % 256, 255, 255)
                if self.type == "a":
                    #quarter_circle(l, l, siz - c + i, TOP + LEFT)
                    #quarter_circle(l, -l, siz - c + i, BOTTOM + LEFT) 
                    i *= -1
                    quarter_circle(l, l, c + i, TOP + LEFT)
                    quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)                
                    quarter_circle(-l, l, c + i, TOP + RIGHT)
                    quarter_circle(l, -l, c + i, BOTTOM + LEFT) 
                elif self.type == "b":
                    half_circle(-l, 0, a + i, RIGHT)
                    half_circle(l, 0, a + i, LEFT)                    
                    half_circle(0, l, a + i, TOP)
                    half_circle(0, -l, a + i, BOTTOM)
                elif self.type == "c":
                    half_circle(l, 0, a + i, LEFT)
                    half_circle(-l, 0, a + i, RIGHT)
                    line(a + i, -l, a + i, l)
                    i *= -1
                    line(-a + i, -l, -a + i, l)
                elif self.type == "d":
                    quarter_circle(-l, l, siz - c + i, TOP + RIGHT)
                    quarter_circle(l, -l, siz - c + i, BOTTOM + LEFT) 
                    i *= -1
                    quarter_circle(-l, l, c + i, TOP + RIGHT)
                    quarter_circle(l, -l, c + i, BOTTOM + LEFT) 
                else:    
                    line(-l, a + i, l, a + i)
                    line(a + i, -l, a + i, l)
                    i *= -1
                    line(-l, -a + i, l, -a + i)
                    line(-a + i, -l, -a + i, l)
                

    @classmethod                                            
    def init_grid(cls, grid_size, border):
        cls.border = border
        cls.spacing = (width - cls.border * 2) / grid_size
        cls.nodes = []
        for x in range(grid_size):
            for y in range(grid_size):
                    new_node = cls(x, y)
                    cls.nodes.append(new_node)

    
            
