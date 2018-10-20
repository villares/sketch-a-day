class Node():
    nodes = []
    grid = dict()
    ver = set()

    def __init__(self, x, y, z):
        self.ix = x
        self.iy = y
        self.iz = z
        self.x = Node.border + Node.spacing / 2 + x * Node.spacing - width / 2
        self.y = Node.border + Node.spacing / 2 + y * Node.spacing - width / 2
        self.z = Node.border + Node.spacing / 2 + z * Node.spacing - width / 2
        self.size_ = 1
        self.cor = None
        self.nb = {0 : False, # |* left 
                   1 : False, # *| right
                   2 : False, # - top
                   3 : False, # _ bottom
                   4 : False,
                   5 : False,
                  }

        self.borders = []
        
    def plot(self):
        """ draws node """
        if self.cor:
            noFill() #stroke(0)
            stroke(self.cor)
            with pushMatrix():
                translate(0, 0, self.z)
                #rect(0, 0, Node.spacing * self.size_, Node.spacing * self.size_)
                self.draw_borders()
                
    def draw_borders(self):
        if self.borders:
            for x1, y1, x2, y2 in self.borders:
                line(x1, y1, x2, y2)
                
                                                
    def update_nbs(self):
        nb0 = Node.grid.get((self.ix-1, self.iy, self.iz))
        self.nb[0] = True if nb0 and nb0.cor else False
        nb1 = Node.grid.get((self.ix+1, self.iy, self.iz))
        self.nb[1] = True if nb1 and nb1.cor else False
        nb2 = Node.grid.get((self.ix, self.iy-1, self.iz))
        self.nb[2] = True if nb2 and nb2.cor else False
        nb3 = Node.grid.get((self.ix, self.iy+1, self.iz))
        self.nb[3] = True if nb3 and nb3.cor else False
        nb4 = Node.grid.get((self.ix, self.iy, self.iz-1))
        self.nb[4] = True if nb4 and nb4.cor else False
        nb5 = Node.grid.get((self.ix, self.iy, self.iz+1))
        self.nb[5] = True if nb5 and nb5.cor else False
        
        b = self.borders
        w = h = Node.spacing * self.size_
        tlX, tlY = self.x - w/2, self.y - h/2
        trX, trY = self.x + w/2, self.y - h/2
        blX, blY = self.x - w/2, self.y + h/2
        brX, brY = self.x + w/2, self.y + h/2
        if not self.nb[0]: b.append((tlX, tlY, blX, blY))
        if not self.nb[1]: b.append((trX, trY, brX, brY))
        if not self.nb[2]: b.append((tlX, tlY, trX, trY))
        if not self.nb[3]: b.append((blX, blY, brX, brY))
        
        for x1, y1, x2, y2 in self.borders:
                Node.ver.append(((x1, y1, self.z, self.iz),
                                (x2, y2, self.z, self.iz)))
 
