class Node():
    nodes = []
    grid = dict()

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
    def plot(self):
        """ draws node """
        if self.cor:
            noFill() #stroke(0)
            stroke(self.cor)
            with pushMatrix():
                translate(self.x, self.y, self.z)
                self.lines(0, 0, Node.spacing * self.size_, Node.spacing * self.size_)
                
    def lines(self, x, y, w, h):
        rectMode(CENTER)
        rect(x, y, w/2, h/2)
        tlX, tlY = x - w/2, y - h/2
        trX, trY = x + w/2, y - h/2
        blX, blY = x - w/2, y + h/2
        brX, brY = x + w/2, y + h/2
        if not self.nb[0]: line(tlX, tlY, blX, blY)
        if not self.nb[1]: line(trX, trY, brX, brY)
        if not self.nb[2]: line(tlX, tlY, trX, trY)
        if not self.nb[3]: line(blX, blY, brX, brY)
        if self.nb[4]: line(x, y, 0, x, y, -w/2)
        if self.nb[5]: line(x, y, 0, x, y, w/2)
        
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
