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
                   2 : False, # - back
                   3 : False, # _ front
                   4 : False,
                   5 : False,
                  }
    def plot(self):
        """ draws box """
        if self.cor:
            noFill() #stroke(0)
            stroke(self.cor)
            with pushMatrix():
                translate(self.x, self.y, self.z)
                self.rect(0, 0, Node.spacing * self.size_, Node.spacing * self.size_)
                
    def rect(self, x, y, w, h):
        rectMode(CENTER)
        #rect(x, y, w/2, h/2)
        tlX, tlY = x - w/2, y - h/2
        trX, trY = x + w/2, y - h/2
        blX, blY = x - w/2, y + h/2
        brX, brY = x + w/2, y + h/2
        if not self.nb[0]: line(tlX, tlY, blX, blY)
        if not self.nb[1]: line(trX, trY, brX, brY)
        if not self.nb[2]: line(tlX, tlY, trX, trY)
        if not self.nb[3]: line(blX, blY, brX, brY)
         
