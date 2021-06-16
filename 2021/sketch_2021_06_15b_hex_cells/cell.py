class MockCell:
    state = 0

class Cell():

    board = dict()
    NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))    
    W = 30
    H = sin(radians(60)) * W
    
    def __init__(self, i, j):
        self.__class__.board[(i, j)] = self
        self.i = i
        self.j = j
        self.state = int(random(2))
        self.x = i * self.W * 1.5 + self.W
        if i % 2 == 0:
            self.y = j * self.H * 2 + self.H
        else:
            self.y = j * self.H * 2 + self.H * 2

    def display(self):
        fill((self.i * 15) % 256, (self.j * 16) % 256, 128 + 128 * self.state)
        with pushMatrix():
            translate(self.x, self.y)
            noStroke()
            self.hexagon(self.W, self.H)
            live_nbs = self.calc_nbs()
            fill(live_nbs * 32)
            self.hexagon(self.W / 2, self.H / 2)
            fill(255)
            textAlign(CENTER, CENTER)
            # text("{}".format(live_nbs), 0, 0)
            # text("{}, {}".format(self.i, self.j), 0, 0)
            # circle(0, 0, 10)
            noFill()
    
    def calc_nbs(self):
        # BROKEN!
        return sum(self.board.get((self.i + io, self.j + jo), MockCell()).state for io, jo in self.NBS)
            
                              
    @staticmethod
    def hexagon(w, h):
        # h expected to be sin(radians(60)) * w 
        with beginShape():
                vertex(-w, 0)
                vertex(-w / 2, -h)
                vertex(w / 2, -h)
                vertex(w, 0)
                vertex(w - w / 2, h)
                vertex(-w / 2, h)
                vertex(-w, 0)
    
